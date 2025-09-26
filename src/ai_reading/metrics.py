"""Adoption metrics utilities."""

from __future__ import annotations

import json
from collections import defaultdict
from dataclasses import dataclass
from datetime import datetime
from pathlib import Path
from statistics import mean
from typing import Dict, Iterable, List


@dataclass
class UsageEvent:
    timestamp: datetime
    user_role: str
    query_type: str
    latency_ms: float
    rating: float


def load_events(path: Path) -> List[UsageEvent]:
    events: List[UsageEvent] = []
    if not path.exists():
        return events
    with path.open("r", encoding="utf-8") as handle:
        for line in handle:
            if not line.strip():
                continue
            record = json.loads(line)
            events.append(
                UsageEvent(
                    timestamp=datetime.fromisoformat(record["timestamp"]),
                    user_role=record["user_role"],
                    query_type=record.get("query_type", "general"),
                    latency_ms=float(record.get("latency_ms", 0)),
                    rating=float(record.get("rating", 0)),
                )
            )
    return events


def summarize_events(events: Iterable[UsageEvent]) -> Dict[str, Dict[str, float]]:
    buckets: Dict[str, Dict[str, List[float]]] = defaultdict(lambda: defaultdict(list))
    summary: Dict[str, Dict[str, float]] = {}

    for event in events:
        buckets[event.user_role]["latency"].append(event.latency_ms)
        buckets[event.user_role]["rating"].append(event.rating)

    for role, metrics in buckets.items():
        summary[role] = {
            "avg_latency_ms": mean(metrics["latency"]) if metrics["latency"] else 0.0,
            "avg_rating": mean(metrics["rating"]) if metrics["rating"] else 0.0,
            "event_count": float(len(metrics["latency"]))
        }
    return summary


def render_summary(summary: Dict[str, Dict[str, float]]) -> None:
    print("Role,Events,Avg Latency (ms),Avg Rating")
    for role, metrics in summary.items():
        print(
            f"{role},{metrics['event_count']:.0f},{metrics['avg_latency_ms']:.1f},{metrics['avg_rating']:.2f}"
        )


def export_summary(summary: Dict[str, Dict[str, float]], destination: Path) -> None:
    destination.parent.mkdir(parents=True, exist_ok=True)
    with destination.open("w", encoding="utf-8") as handle:
        json.dump(summary, handle, indent=2)
