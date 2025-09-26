---
title: AI Reading Agents Catalog
archetype: documentation
status: beta
owner: LLMOps Guild
maintainer: Agents Working Group
version: 0.1.0
tags: [agents, prompts, governance]
last_reviewed: 2025-03-01
---

# Agents Catalog

Use this catalog to configure and operate AI Reading agents safely. Each agent has a dedicated prompt, expected inputs/outputs, and guardrail requirements.

## Shared principles
- **Single responsibility**: Each agent performs one job to simplify testing and auditing.
- **Local-first**: All prompts assume Ollama or LM Studio endpoints; update configs before enabling remote APIs.
- **Guardrail-first**: Every agent must log decisions and adhere to deny-lists, regex checks, and policy tags.

## Agents summary

| Agent | Purpose | Inputs | Outputs | Guardrail focus |
| --- | --- | --- | --- | --- |
| Ingestion Agent | Normalize and embed documents. | File path, metadata tags, sensitivity level. | Chunked text, embeddings, ingestion log. | PII masking, source approval confirmation. |
| Compliance Agent | Score prompts and answers for risk. | User role, prompt, retrieved context, draft answer. | Verdict (allow/warn/block), rationale, policy references. | Policy mapping, sensitive term detection, escalation triggers. |
| Adoption Insights Agent | Convert usage logs into adoption signals. | Query logs, feedback scores, role roster. | Adoption summary, at-risk cohorts, recommended actions. | Threshold alerts, anonymization, storage retention. |
| Exec Brief Agent | Produce executive-ready summaries. | Topic, audience role, context snippets, KPI highlights. | 1-page brief with recommendations, risk notes. | Citation enforcement, scope confirmation, confidentiality guardrails. |

## Implementation steps
1. Copy `agents/configs/settings.example.yml` to your environment and adjust model endpoints.
2. Update guardrail patterns in `agents/configs/guardrails.example.yml` with organization-specific policies.
3. Test each agent via `make agent-test AGENT=name`; confirm logs in `./logs/agents`.
4. Review adoption metrics after any prompt update to validate intended behavior.

## SMB vs Enterprise guidance
- **SMB**: Run agents sequentially on a single orchestrator; rely on Makefile targets for orchestration.
- **Enterprise**: Deploy agents as containerized microservices with centralized logging and SSO authentication.

## Change management
- Version prompts and configs via Git; require peer review for high-risk updates.
- Document rationale for guardrail overrides and store with audit artifacts.
