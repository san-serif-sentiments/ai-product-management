---
title: AI Business Analyst Guide
archetype: role-guide
status: beta
owner: Analytics Chapter
maintainer: AI Program Office
version: 0.1.0
tags: [role, business-analyst, rag]
last_reviewed: 2025-03-01
---

# AI Business Analyst

## Mission
Translate business questions into structured prompts, validate AI Reading outputs, and surface insights that drive measurable outcomes.

## Scope
- Manage demand intake and prioritization for AI Reading requests.
- Own prompt templates and retrieval configurations for business-facing workflows.
- Coordinate with Compliance and Adoption teams to ensure outputs are trustworthy and usable.

## Core tasks & steps
1. **Clarify business question**
   - Capture context, stakeholders, and desired format.
   - Tag requests with role, department, and sensitivity level.
2. **Design retrieval strategy**
   - Select default retrieval depth (Top-3 vs Top-6) based on complexity.
   - Choose vector store (Chroma vs Qdrant) and filters.
3. **Craft prompt**
   - Apply role-aware system prompt; include citations and answer style instructions.
   - Run test query and review guardrail output.
4. **Validate output**
   - Confirm source snippets match answer claims.
   - Flag hallucinations or policy conflicts to Compliance Agent.
5. **Publish insight**
   - Deliver formatted response to stakeholders with recommended actions.
   - Capture feedback and rate answer quality in adoption dashboard.

## SMB vs Enterprise nuances
- **SMB**: Analyst may double as data steward; use lightweight spreadsheets for intake and approval.
- **Enterprise**: Work through existing analytics backlog tools (Jira, Aha!) and adhere to formal data classification workflows.

## Success metrics
- ≥ 90% of analyst-authored prompts reused across teams within 60 days.
- Answer validation cycle time ≤ 1 business day for high-priority requests.
- Zero unapproved high-risk data exposures from analyst workflows per quarter.

## Practical examples
- ✅ Configure prompt that returns HR policy summaries with inline citations for onboarding deck.
- ✅ Collaborate with Compliance Agent to adjust deny-list after detecting regional privacy clause.
- ❌ Deploy prompt changes directly to production without regression testing.
- ❌ Ignore feedback from adoption metrics that show low confidence ratings.
