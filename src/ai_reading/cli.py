"""Command-line entry points for AI Reading."""

from __future__ import annotations

import argparse
import json
from datetime import datetime, timezone
from pathlib import Path

from . import __version__
from .ingest import run_cli as run_ingestion
from .metrics import export_summary, load_events, render_summary, summarize_events
from .retrieval import query_index


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(prog="ai-reading", description="AI Reading command line interface")
    parser.add_argument("--version", action="version", version=f"ai-reading {__version__}")

    subparsers = parser.add_subparsers(dest="command")

    ingest_parser = subparsers.add_parser("ingest", help="Ingest markdown documents")
    ingest_parser.add_argument("--source", default="data/samples", help="Directory containing markdown documents")
    ingest_parser.add_argument("--vector-path", default=None, help="Override vector path")
    ingest_parser.add_argument("--chunk-size", type=int, default=400, help="Chunk size in characters")
    ingest_parser.add_argument("--overlap", type=int, default=80, help="Chunk overlap in characters")

    query_parser = subparsers.add_parser("query", help="Query vector index")
    query_parser.add_argument("prompt", help="Query prompt")
    query_parser.add_argument("--top-k", type=int, default=3, help="Number of results")
    query_parser.add_argument("--vector-path", default=None, help="Override vector path")

    adoption_parser = subparsers.add_parser("adoption-report", help="Generate adoption summary")
    adoption_parser.add_argument("--log-path", default="logs/usage.jsonl", help="Usage log path")
    adoption_parser.add_argument("--output", default="logs/adoption-summary.json", help="Output JSON path")

    init_parser = subparsers.add_parser("init-usage-log", help="Create sample usage log")
    init_parser.add_argument("--destination", default="logs/usage.jsonl", help="Destination path")

    return parser


def command_ingest(args: argparse.Namespace) -> None:
    result = run_ingestion(
        source=args.source,
        vector_path=args.vector_path,
        chunk_size=args.chunk_size,
        overlap=args.overlap,
    )
    print("Ingestion complete")
    print(f"Processed: {result.processed}\nInserted: {result.inserted}\nSkipped: {result.skipped}")
    print(f"Vector path: {result.vector_path}\nLog file: {result.log_file}")


def command_query(args: argparse.Namespace) -> None:
    result = query_index(query=args.prompt, top_k=args.top_k, vector_path=args.vector_path)
    if not result.documents:
        print("No results found.")
        return
    for idx, (score, metadata, text) in enumerate(zip(result.scores, result.metadatas, result.documents), start=1):
        print(f"\nResult {idx} | score={score:.4f}")
        print(f"Source: {metadata.get('source_path', 'unknown')}")
        preview = text[:400].replace("\n", " ")
        print(preview + ("..." if len(text) > 400 else ""))


def command_adoption_report(args: argparse.Namespace) -> None:
    events = load_events(Path(args.log_path))
    summary = summarize_events(events)
    if not summary:
        print("No usage events found.")
        return
    render_summary(summary)
    export_summary(summary, Path(args.output))
    print(f"Adoption summary written to {args.output}")


def command_init_usage_log(args: argparse.Namespace) -> None:
    dest_path = Path(args.destination)
    dest_path.parent.mkdir(parents=True, exist_ok=True)
    sample_events = [
        {
            "timestamp": datetime.now(timezone.utc).isoformat(),
            "user_role": "ai-business-analyst",
            "query_type": "policy",
            "latency_ms": 3200,
            "rating": 4.6,
        },
        {
            "timestamp": datetime.now(timezone.utc).isoformat(),
            "user_role": "ai-program-manager",
            "query_type": "governance",
            "latency_ms": 5100,
            "rating": 4.2,
        },
        {
            "timestamp": datetime.now(timezone.utc).isoformat(),
            "user_role": "manager-of-ai",
            "query_type": "adoption",
            "latency_ms": 4700,
            "rating": 4.8,
        },
    ]
    with dest_path.open("w", encoding="utf-8") as handle:
        for event in sample_events:
            handle.write(json.dumps(event) + "\n")
    print(f"Sample usage log written to {dest_path}")


def main(argv: list[str] | None = None) -> None:
    parser = build_parser()
    args = parser.parse_args(argv)
    if not args.command:
        parser.print_help()
        return
    if args.command == "ingest":
        command_ingest(args)
    elif args.command == "query":
        command_query(args)
    elif args.command == "adoption-report":
        command_adoption_report(args)
    elif args.command == "init-usage-log":
        command_init_usage_log(args)
    else:
        parser.print_help()


if __name__ == "__main__":
    main()
