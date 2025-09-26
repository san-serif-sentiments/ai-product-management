"""AI Reading local-first RAG toolkit."""

from importlib.metadata import version, PackageNotFoundError

try:
    __version__ = version("ai-reading")
except PackageNotFoundError:  # pragma: no cover - during local development
    __version__ = "0.0.0"

__all__ = ["__version__"]
