"""Generate adoption metrics report."""

from __future__ import annotations

import argparse
from pathlib import Path

from ai_reading.metrics import export_summary, load_events, render_summary, summarize_events


def main() -> None:
    parser = argparse.ArgumentParser(description="AI Reading adoption metrics")
    parser.add_argument("--log-path", default="logs/usage.jsonl", help="Usage log path")
    parser.add_argument("--output", default="logs/adoption-summary.json", help="Output JSON path")
    args = parser.parse_args()

    events = load_events(Path(args.log_path))
    summary = summarize_events(events)
    if not summary:
        print("No usage events found.")
        return
    render_summary(summary)
    export_summary(summary, Path(args.output))


if __name__ == "__main__":
    main()
