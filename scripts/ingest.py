"""Run ingestion pipeline from command line."""

from __future__ import annotations

import argparse

from ai_reading.ingest import run_cli


def main() -> None:
    parser = argparse.ArgumentParser(description="AI Reading ingestion runner")
    parser.add_argument("--source", default="data/samples", help="Directory containing markdown docs")
    parser.add_argument("--vector-path", default=None, help="Vector database path override")
    parser.add_argument("--chunk-size", type=int, default=400)
    parser.add_argument("--overlap", type=int, default=80)
    args = parser.parse_args()
    run_cli(source=args.source, vector_path=args.vector_path, chunk_size=args.chunk_size, overlap=args.overlap)


if __name__ == "__main__":
    main()
