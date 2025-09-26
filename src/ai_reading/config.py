"""Configuration helpers for AI Reading."""

from __future__ import annotations

from dataclasses import dataclass, field
from pathlib import Path
from typing import Dict, Optional

BASE_DIR = Path(__file__).resolve().parent.parent.parent
DEFAULT_DATA_DIR = BASE_DIR / "data"
DEFAULT_VECTOR_DIR = BASE_DIR / "data" / "vectors" / "ingest"
DEFAULT_LOG_DIR = BASE_DIR / "logs"


@dataclass
class InferenceSettings:
    provider: str = "ollama"
    default_llm: str = "mistral:instruct"
    embedding_model: str = "local-bow"


@dataclass
class VectorStoreSettings:
    name: str = "ai-reading"
    path: Path = DEFAULT_VECTOR_DIR
    metadata: Dict[str, str] = field(default_factory=lambda: {"similarity": "cosine"})


@dataclass
class LoggingSettings:
    path: Path = DEFAULT_LOG_DIR


@dataclass
class PipelineSettings:
    data_dir: Path = DEFAULT_DATA_DIR
    inference: InferenceSettings = field(default_factory=InferenceSettings)
    vector_store: VectorStoreSettings = field(default_factory=VectorStoreSettings)
    logging: LoggingSettings = field(default_factory=LoggingSettings)


def load_settings(vector_path: Optional[str] = None) -> PipelineSettings:
    settings = PipelineSettings()
    if vector_path:
        settings.vector_store.path = Path(vector_path).expanduser().resolve()
    settings.logging.path.mkdir(parents=True, exist_ok=True)
    settings.vector_store.path.mkdir(parents=True, exist_ok=True)
    return settings
