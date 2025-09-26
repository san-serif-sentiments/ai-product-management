"""Retrieval utilities for AI Reading."""

from __future__ import annotations

import json
import math
from dataclasses import dataclass
from pathlib import Path
from typing import Dict, List, Sequence

from .config import load_settings
from .text import tokenize


@dataclass
class RetrievalResult:
    query: str
    documents: Sequence[str]
    metadatas: Sequence[Dict[str, str]]
    scores: Sequence[float]


def load_index(path: Path, collection: str) -> Dict[str, object]:
    index_path = path / f"{collection}.json"
    if not index_path.exists():
        raise FileNotFoundError(f"Vector index not found at {index_path}")
    with index_path.open("r", encoding="utf-8") as handle:
        return json.load(handle)


def cosine_similarity(vec_a: Dict[str, float], vec_b: Dict[str, float]) -> float:
    if not vec_a or not vec_b:
        return 0.0
    shared_keys = set(vec_a).intersection(vec_b)
    numerator = sum(vec_a[key] * vec_b[key] for key in shared_keys)
    norm_a = math.sqrt(sum(value * value for value in vec_a.values()))
    norm_b = math.sqrt(sum(value * value for value in vec_b.values()))
    if norm_a == 0 or norm_b == 0:
        return 0.0
    return numerator / (norm_a * norm_b)


def query_index(query: str, top_k: int = 3, vector_path: str | None = None, collection: str = "ai-reading") -> RetrievalResult:
    settings = load_settings(vector_path=vector_path)
    payload = load_index(settings.vector_store.path, collection)
    idf: Dict[str, float] = {k: float(v) for k, v in payload.get("idf", {}).items()}

    query_tokens = tokenize(query)
    if not query_tokens:
        return RetrievalResult(query=query, documents=[], metadatas=[], scores=[])

    tf: Dict[str, float] = {}
    for token in query_tokens:
        tf[token] = tf.get(token, 0) + 1
    total = sum(tf.values()) or 1
    tf = {token: count / total for token, count in tf.items()}
    query_vector = {token: tf_val * idf.get(token, 1.0) for token, tf_val in tf.items()}

    scored: List[tuple[float, Dict[str, str], str]] = []
    for entry in payload.get("documents", []):
        vector = {k: float(v) for k, v in entry.get("vector", {}).items()}
        score = cosine_similarity(query_vector, vector)
        scored.append((score, entry.get("metadata", {}), entry.get("text", "")))

    scored.sort(key=lambda item: item[0], reverse=True)
    top_results = scored[:top_k]

    return RetrievalResult(
        query=query,
        documents=[text for _, _, text in top_results],
        metadatas=[metadata for _, metadata, _ in top_results],
        scores=[score for score, _, _ in top_results],
    )
