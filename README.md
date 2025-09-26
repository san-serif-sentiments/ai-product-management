---
title: AI Reading — Intelligent Knowledge Companion
archetype: product
status: draft
owner: PoeticMayhem
maintainer: Shaily
version: 0.1.0
tags: [RAG, LLMOps, adoption, governance, SMB, enterprise]
last_reviewed: 2025-09-26
---

# AI Reading — Intelligent Knowledge Companion

## Overview
AI Reading helps teams **ingest, index, enrich, and retrieve** internal knowledge (docs, wikis, PDFs) with **role-aware** guidance: executive briefs, impact analysis, adoption hints, and compliance notes.

- **Why now:** 78% of orgs report using AI in at least one function (Mar 2025) and are rewiring workflows for value, risk, and governance. 0  
- **Value gap:** Knowledge workers still lose **~1.8 hours/day** searching for information; structured knowledge & retrieval can materially cut that. 1  
- **Risk climate:** GenAI threats (deepfakes, prompt-injection) are rising; SMBs are targeted too. Governance and guardrails are essential. 2

## What it does
- **Ingest** (connectors + cleaning) → **Chunk** → **Embed** → **Index** (Chroma/Qdrant)  
- **Retrieve** (semantic + filters) → **Generate** (role-aware prompts) → **Log & Evaluate**  
- **Govern** (PII redaction, audit trails, AI Act awareness) → **Adopt** (dashboards, playbooks)

## Who it’s for
- **SMBs:** faster onboarding, fewer repetitive queries, low-ops local stack.
- **Enterprises:** policy-aware retrieval, auditability, role-scoped outputs.

## Quick start
```bash
# 1) Clone & configure
cp ops/.env.example .env
# set OLLAMA/LM Studio model names, embeddings, vector store path

# 2) Local dev (no internet calls)
make dev

# 3) Index sample docs, run a test query
make ingest
make query Q="What changed in the leave policy?"# ai-product-management