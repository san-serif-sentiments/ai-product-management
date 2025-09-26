"""Text utilities for AI Reading."""

from __future__ import annotations

import re
from typing import Iterable, List


def chunk_markdown(text: str, chunk_size: int = 400, overlap: int = 80) -> List[str]:
    """Split text into overlapping chunks based on characters."""

    if chunk_size <= 0:
        raise ValueError("chunk_size must be positive")

    if overlap >= chunk_size:
        raise ValueError("overlap must be smaller than chunk_size")

    normalized = _normalize_whitespace(text)
    chunks: List[str] = []
    start = 0
    while start < len(normalized):
        end = start + chunk_size
        chunk = normalized[start:end]
        chunks.append(chunk.strip())
        start = end - overlap
        if start < 0:
            start = 0
        if start >= len(normalized):
            break
    return [chunk for chunk in chunks if chunk]


def _normalize_whitespace(text: str) -> str:
    return " ".join(text.split())


def sliding_window(items: Iterable[str], window: int) -> List[str]:
    buffer: List[str] = []
    result: List[str] = []
    for item in items:
        buffer.append(item)
        if len(buffer) == window:
            result.append(" ".join(buffer))
            buffer.pop(0)
    if buffer:
        result.append(" ".join(buffer))
    return result


TOKEN_PATTERN = re.compile(r"[A-Za-z0-9]+")


def tokenize(text: str) -> List[str]:
    """Lowercase alphanumeric tokenizer."""

    return [match.group(0).lower() for match in TOKEN_PATTERN.finditer(text)]
