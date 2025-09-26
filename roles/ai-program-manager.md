---
title: AI Program Manager Guide
archetype: role-guide
status: beta
owner: AI Program Office
maintainer: Delivery Excellence Team
version: 0.1.0
tags: [role, program-management, governance]
last_reviewed: 2025-03-01
---

# AI Program Manager

## Mission
Coordinate the cross-functional plan that delivers AI Reading from pilot to scaled adoption with measurable ROI and compliance.

## Scope
- Manage roadmap, release planning, and dependency tracking.
- Align security, legal, and business stakeholders on governance commitments.
- Oversee budget, resource allocation, and vendor management for local-first stack.

## Core tasks & steps
1. **Define program charter**
   - Document scope, success metrics, and risk appetite using templates in `docs/`.
   - Secure executive sponsor approval.
2. **Plan releases**
   - Sequence ingestion, agent tuning, and user rollout milestones.
   - Maintain SMB vs enterprise workstream differences in roadmap.
3. **Run governance cadence**
   - Schedule compliance reviews, change boards, and retrospective meetings.
   - Ensure EU AI Act controls are operational and evidenced. [CITE:EU_AIACT]
4. **Enable teams**
   - Provide onboarding materials, training, and communication plans.
   - Track adoption actions via Adoption Insights Agent outputs.
5. **Report progress**
   - Publish weekly status updates with KPI trends and blockers.
   - Generate monthly executive briefs in partnership with Exec Brief Agent.

## SMB vs Enterprise nuances
- **SMB**: Program manager may be part-time; leverage lightweight Kanban boards and fewer approval gates.
- **Enterprise**: Requires formal steering committee, change advisory board integrations, and detailed vendor security reviews.

## Success metrics
- Milestone adherence ≥ 90% across quarterly plan.
- Budget variance ≤ ±5% for hardware and software.
- Governance actions (audits, reviews) completed on schedule with zero missed approvals.

## Practical examples
- ✅ Align change manager, compliance lead, and analyst on shared release calendar.
- ✅ Document risk acceptance when latency increases due to larger models.
- ❌ Skip stakeholder demos before major releases.
- ❌ Allow model updates without verifying guardrail compatibility.
