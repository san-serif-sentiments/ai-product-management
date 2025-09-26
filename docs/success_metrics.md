---
title: Success Metrics
archetype: documentation
status: beta
owner: AI Program Office
maintainer: Analytics Team
version: 0.1.0
tags: [metrics, adoption, governance]
last_reviewed: 2025-03-01
---

# Success Metrics

Track these metrics to confirm AI Reading delivers measurable value while staying compliant. Align targets with SMB or enterprise baselines as noted.

## Time to answer (TTA)
- **Definition**: Median seconds from user query submission to response delivery.
- **Target**: 
  - SMB: ≤ 5 seconds for 90% of queries using local inference on single-node hardware.
  - Enterprise: ≤ 8 seconds for 90% of queries with guardrails and deeper retrieval.
- **Measurement cadence**: Daily automated log aggregation; weekly review.

## Deflection rate
- **Definition**: Percentage of resolved queries that avoid human escalation.
- **Target**: 
  - SMB: ≥ 55% deflection within first 60 days. [CITE:MCKINSEY_2025]
  - Enterprise: ≥ 65% deflection after integrating with knowledge base workflows. [CITE:IBM_2024]
- **Measurement cadence**: Weekly; correlate with service desk ticket volume.

## Adoption velocity
- **Definition**: Share of target users submitting ≥3 queries per week.
- **Target**: 
  - SMB: 60% of invited users by week 6.
  - Enterprise: 45% of licensed users by week 8 due to larger cohorts and change controls.
- **Supporting actions**: Use Adoption Insights Agent outputs to plan enablement.

## Answer quality
- **Definition**: Percentage of responses rated ≥4/5 by users or reviewers.
- **Target**: Maintain ≥ 85% positive ratings across roles; escalate if any persona drops below 75%.

## Audit completeness
- **Definition**: Percentage of interactions with associated compliant logs (prompt, retrieval context, guardrail verdict, answer).
- **Target**: 
  - SMB: 95% completeness with monthly manual sampling.
  - Enterprise: 99% completeness with automated validation scripts and quarterly audits. [CITE:EU_AIACT]

## Change management effectiveness
- **Definition**: Percentage of adoption actions completed on schedule (training sessions, communications, policy updates).
- **Target**: 90% on-time delivery; escalations reviewed during biweekly steering meeting.

## Escalation handling
- **Definition**: Mean time to resolve blocked or flagged interactions.
- **Target**: 
  - SMB: < 2 business days.
  - Enterprise: < 1 business day with on-call compliance rotation.

## Reporting workflow
1. Export metrics via `make adoption-report` (SMB) or scheduled pipeline (enterprise).
2. Manager of AI reviews KPI dashboard; share exec summary via Exec Brief Agent monthly.
3. Capture corrective actions and re-forecast targets quarterly.
