"""Document ingestion pipeline for AI Reading (offline friendly)."""

from __future__ import annotations

import json
from dataclasses import dataclass
from datetime import datetime
from pathlib import Path
from typing import Dict, Iterable, List, Sequence, Tuple

from .config import PipelineSettings, load_settings
from .text import chunk_markdown, tokenize


@dataclass
class Document:
    metadata: Dict[str, str]
    content: str
    source_path: Path


@dataclass
class DocumentChunk:
    id: str
    text: str
    metadata: Dict[str, str]
    vector: Dict[str, float]


@dataclass
class IngestionResult:
    processed: int
    inserted: int
    skipped: int
    collection: str
    vector_path: Path
    log_file: Path


FRONT_MATTER_DELIMITER = "---"


def parse_front_matter(raw_text: str) -> Tuple[Dict[str, str], str]:
    lines = raw_text.splitlines()
    metadata: Dict[str, str] = {}
    content_lines: List[str] = []

    if lines and lines[0].strip() == FRONT_MATTER_DELIMITER:
        end_index = 1
        while end_index < len(lines) and lines[end_index].strip() != FRONT_MATTER_DELIMITER:
            line = lines[end_index]
            if ":" in line:
                key, value = line.split(":", 1)
                metadata[key.strip()] = value.strip()
            end_index += 1
        content_lines = lines[end_index + 1 :]
    else:
        content_lines = lines

    return metadata, "\n".join(content_lines)


def load_documents(files: Iterable[Path]) -> List[Document]:
    documents: List[Document] = []
    for path in files:
        raw_text = path.read_text(encoding="utf-8")
        metadata, content = parse_front_matter(raw_text)
        metadata.setdefault("title", path.stem)
        metadata.setdefault("source_path", str(path))
        metadata.setdefault("ingested_at", datetime.utcnow().isoformat())
        documents.append(Document(metadata=metadata, content=content, source_path=path))
    return documents


def compute_term_frequency(tokens: Sequence[str]) -> Dict[str, float]:
    counts: Dict[str, int] = {}
    for token in tokens:
        counts[token] = counts.get(token, 0) + 1
    total = sum(counts.values()) or 1
    return {token: count / total for token, count in counts.items()}


def prepare_chunks(document: Document, chunk_size: int, overlap: int) -> List[DocumentChunk]:
    raw_chunks = chunk_markdown(document.content, chunk_size=chunk_size, overlap=overlap)
    prepared: List[DocumentChunk] = []
    for idx, chunk in enumerate(raw_chunks):
        tokens = tokenize(chunk)
        tf = compute_term_frequency(tokens)
        metadata = dict(document.metadata)
        metadata.update({"chunk_index": str(idx), "chunk_count": str(len(raw_chunks))})
        prepared.append(
            DocumentChunk(
                id=f"{metadata['title']}-{idx}",
                text=chunk,
                metadata=metadata,
                vector=tf,
            )
        )
    return prepared


def build_index(chunks: List[DocumentChunk]) -> Tuple[Dict[str, Dict[str, float]], Dict[str, float]]:
    doc_freq: Dict[str, int] = {}
    for chunk in chunks:
        for token in chunk.vector:
            doc_freq[token] = doc_freq.get(token, 0) + 1
    total_docs = max(len(chunks), 1)
    idf = {token: 1.0 + math.log(total_docs / (1 + freq)) for token, freq in doc_freq.items()}
    vectors: Dict[str, Dict[str, float]] = {}
    for chunk in chunks:
        vectors[chunk.id] = {token: weight * idf.get(token, 1.0) for token, weight in chunk.vector.items()}
    return vectors, idf


import math

def ingest_documents(
    source_dir: Path,
    settings: PipelineSettings,
    collection_name: str = "ai-reading",
    chunk_size: int = 400,
    overlap: int = 80,
) -> IngestionResult:
    files = sorted(source_dir.glob("*.md"))
    if not files:
        raise FileNotFoundError(f"No markdown files found in {source_dir}")

    documents = load_documents(files)
    chunks: List[DocumentChunk] = []
    for doc in documents:
        chunks.extend(prepare_chunks(doc, chunk_size=chunk_size, overlap=overlap))

    existing_index_path = settings.vector_store.path / f"{collection_name}.json"
    existing_ids: List[str] = []
    if existing_index_path.exists():
        with existing_index_path.open("r", encoding="utf-8") as handle:
            payload = json.load(handle)
            existing_ids = [entry["id"] for entry in payload.get("documents", [])]

    new_chunks = [chunk for chunk in chunks if chunk.id not in existing_ids]
    skipped = len(chunks) - len(new_chunks)

    vectors, idf = build_index(chunks)

    documents_payload = [
        {
            "id": chunk.id,
            "text": chunk.text,
            "metadata": chunk.metadata,
            "vector": vectors.get(chunk.id, chunk.vector),
        }
        for chunk in chunks
    ]

    index_payload = {
        "collection": collection_name,
        "created_at": datetime.utcnow().isoformat(),
        "idf": idf,
        "documents": documents_payload,
    }

    existing_index_path.parent.mkdir(parents=True, exist_ok=True)
    with existing_index_path.open("w", encoding="utf-8") as handle:
        json.dump(index_payload, handle, indent=2)

    log_path = settings.logging.path / f"ingest-{datetime.utcnow().strftime('%Y%m%d-%H%M%S')}.json"
    log_path.write_text(
        json.dumps(
            {
                "processed": len(documents),
                "chunks": len(chunks),
                "inserted": len(new_chunks),
                "skipped": skipped,
                "collection": collection_name,
            },
            indent=2,
        ),
        encoding="utf-8",
    )

    return IngestionResult(
        processed=len(documents),
        inserted=len(new_chunks),
        skipped=skipped,
        collection=collection_name,
        vector_path=settings.vector_store.path,
        log_file=log_path,
    )


def run_cli(source: str, vector_path: str | None = None, chunk_size: int = 400, overlap: int = 80) -> IngestionResult:
    settings = load_settings(vector_path=vector_path)
    source_dir = Path(source)
    if not source_dir.exists():
        raise FileNotFoundError(f"Source directory not found: {source}")
    return ingest_documents(source_dir=source_dir, settings=settings, chunk_size=chunk_size, overlap=overlap)
