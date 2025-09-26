
---
title: Agents Guide
archetype: guide
status: draft
owner: LLMOps
maintainer: Shaily
version: 0.2.0
tags: [agents, orchestration, RAG, governance, adoption]
last_reviewed: 2025-09-26
---

# AI Reading — Agents Guide

## Purpose
Agents are small, **single-purpose AI workers** that make the AI Reading system modular and safe. Each agent focuses on one slice of the workflow so you can scale or swap them independently.

## Core Agents

### 1. **Ingestion Agent**
- **Goal:** Turn raw docs into clean, searchable chunks.
- **Key Tasks:**
  - Parse PDFs, wikis, PPTs → normalized text/metadata
  - Detect and mask PII (emails, phone numbers, IDs)
  - Generate embeddings and push to vector DB (Chroma default, Qdrant optional)
- **Outputs:** Indexed chunks with doc IDs + metadata JSON

### 2. **Risk & Compliance Agent**
- **Goal:** Guard every retrieval/generation step against policy breaches.
- **Key Tasks:**
  - Scan prompts and retrieved text for sensitive data or high-risk categories
  - Check alignment with EU AI Act, GDPR, internal compliance lists
  - Produce explainable logs and “block / warn / allow” verdict
- **Outputs:** Risk score + reason, audit log entry

### 3. **Retrieval Orchestration Agent**
- **Goal:** Decide the best retrieval path for each query.
- **Key Tasks:**
  - Pick retrieval mode (semantic vs hybrid vs keyword fallback)
  - Adjust context window and chunk limits
  - Add metadata filters (team, region, classification)
- **Outputs:** Ranked, cleaned context for the LLM

### 4. **Adoption Insights Agent**
- **Goal:** Turn usage data into actionable adoption signals.
- **Key Tasks:**
  - Track queries, user roles, answer ratings, retention
  - Spot blockers (slow answers, bad quality, low reuse)
  - Suggest comms/training interventions
- **Outputs:** Adoption dashboard feed, tips for Change Manager

### 5. **Executive Brief Agent**
- **Goal:** Generate CXO-level summaries safely.
- **Key Tasks:**
  - Condense knowledge into 1-page briefs with confidence signals
  - Highlight risk notes and adoption metrics
  - Tag by function (HR, Sales, IT)
- **Outputs:** Briefs, decks, meeting prep packs

---

## How to Extend

1. **Copy an existing prompt** from `agents/prompts/` as a starting point.
2. **Configure** it in `agents/configs/settings.example.yml`:
   - Add model & temperature
   - Input/output schema
3. **Guardrails**:
   - Update `agents/configs/guardrails.example.yml` to add deny-lists, regex checks, safety filters.
4. **Test locally** using the `make dev` stack; check logs in `./data/vectors` and `./logs/agents`.

---

## Design Principles

- **Single-responsibility:** one agent, one job. Easier debugging and scaling.
- **Composable:** swap vector DB or model without rewriting other agents.
- **Observable:** every agent logs what it did and why.
- **Policy-aware by default:** GDPR/AI Act aligned scanning and blocking.

---

## Practical Examples

✅ Extend Retrieval Orchestration Agent to add **department-level filters**  
✅ Add a **Retention Coach Agent** that nudges users to return weekly  
❌ Ship an ingestion agent that pushes raw PII to external APIs  
❌ Combine compliance and retrieval into one giant prompt

---

## Escalation & Failover

- If any agent fails, default to safe fallback: plain search + user warning.
- Compliance agent failure → block generation and log incident.
- Adoption agent failure → degrade to raw usage logs, no KPI updates.

---

## Next Steps

- **Pilot with Ingestion + Retrieval + Risk first.**  
- Add Adoption Insights once there’s steady usage.  
- Only add Exec Brief when risk/compliance is proven.



