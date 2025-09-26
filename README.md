---
title: AI Reading — Intelligent Knowledge Companion
archetype: readme
status: beta
owner: AI Product Team
maintainer: LLMOps Guild
version: 0.1.0
tags: [ai-reading, rag, governance, adoption]
last_reviewed: 2025-03-01
---

# AI Reading — Intelligent Knowledge Companion

AI Reading is a local-first Retrieval-Augmented Generation (RAG) toolkit that lets knowledge teams curate, govern, and deliver role-aware answers from internal content. It ships with an opinionated architecture, agent prompts, and operational scripts so small teams and enterprises can move from pilot to scaled adoption without sacrificing control.

## Why this repo exists
- Search friction slows knowledge work and drives shadow AI usage. [CITE:MCKINSEY_2025]
- Regulated industries need AI systems that prove compliance without external data leakage. [CITE:EU_AIACT]
- Adoption stalls without programmatic role clarity and measurable success criteria. [CITE:IBM_2024]

## Core capabilities
1. **Local-first pipeline**: Ollama or LM Studio for inference, Chroma default vector store, optional Qdrant for scale.
2. **Role-aware experiences**: Prebuilt prompts for business analysts, program managers, adoption leads, and AI leaders.
3. **Governance-ready**: EU AI Act-aligned controls across ingest, runtime, and post-run with audit trails.
4. **Adoption playbooks**: Metrics, change tactics, and executive briefs to keep stakeholders aligned.

## Repository layout
- `docs/` — Strategy, architecture, security, metrics, and references.
- `roles/` — Pragmatic guides for the four key personas.
- `agents/` — System prompts, guardrails, and configuration templates.
- `data/` — Sample documents and vector index placeholder.
- `ops/` — Local orchestration via Makefile, Docker Compose, and env template.

## Getting started
1. Copy `.env.example` to `.env` and adjust secrets.
2. Install prerequisites: Docker, Make, Ollama (or LM Studio CLI).
3. Run `make bootstrap` to pull models and create local volumes.
4. Run `make up` to start the stack; use `make ingest` to load sample docs.
5. Access usage dashboards via `make adoption-report` once traffic exists.

## Target users
- SMB teams looking for low-lift knowledge copilots with strict boundary controls.
- Enterprise programs that need evidence of compliance, auditability, and adoption maturity.

## Support and contributions
- File issues for defects or doc gaps.
- Fork and open PRs for improvements; include governance and adoption impacts in descriptions.
- Join discussions on local-first AI patterns in the Issues tab.

## License
Released under the MIT License (see `LICENSE`).
