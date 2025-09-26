---
title: AI Reading Overview
archetype: documentation
status: beta
owner: AI Product Team
maintainer: Knowledge Ops Guild
version: 0.1.0
tags: [overview, strategy, rag]
last_reviewed: 2025-03-01
---

# Overview

AI Reading — Intelligent Knowledge Companion is a blueprint for deploying a Retrieval-Augmented Generation (RAG) assistant that respects data residency, role-based experience design, and EU AI Act-oriented governance.

## Problem this solves
- **Fragmented knowledge**: Employees waste hours searching internal wikis, email threads, and policy docs. [CITE:MCKINSEY_2025]
- **Compliance anxiety**: Security and legal teams block AI deployments lacking transparent controls. [CITE:EU_AIACT]
- **Adoption gap**: Pilots stall when roles and metrics are undefined, reducing ROI. [CITE:IBM_2024]

## Solution pillars
1. **Local-first stack** — Ollama or LM Studio hosts models on customer-controlled hardware. Embeddings default to Chroma for quick setup, with Qdrant optional when scale or filtering is required.
2. **Role-aware delivery** — Four guides align tasks for analysts, program managers, adoption leads, and AI managers so decision-making is consistent across SMB and enterprise environments.
3. **Governance by design** — Controls, audit logs, and risk scoring map to EU AI Act risk tiers and common internal policies.
4. **Adoption intelligence** — Built-in prompts and metrics highlight time-to-answer, resolution quality, and training needs.

## Deployment modes
| Mode | SMB focus | Enterprise focus |
| --- | --- | --- |
| **Laptop / Mini PC** | Single-node Ollama with Chroma; ideal for <50 users and limited IT overhead. | Not recommended beyond prototyping. |
| **On-prem cluster** | Optional for SMBs with compliance-heavy data; run Compose stack on hardened servers. | Standard: multi-node Docker, automated backups, optional Qdrant cluster. |
| **Private cloud** | Burstable compute with VPN access; ensure network egress controls. | Integrate with IAM (Azure AD/Okta) and policy engines; extend guardrails. |

## Lifecycle
1. **Ingest** sample docs, sanitize, and embed.
2. **Retrieve** via orchestration agent, tuned per role.
3. **Generate** role-specific responses with guardrails.
4. **Observe** adoption metrics, iterate prompts, and adjust governance settings.
5. **Audit** logs for compliance, refine controls, and renew approvals quarterly.

## Success factors
- Establish cross-functional working group with security, knowledge management, and business sponsors.
- Pair SMB teams with managed change templates; provide enterprise teams with integration runbooks.
- Track success metrics weekly; escalate gaps to the Manager of AI for unblock.
