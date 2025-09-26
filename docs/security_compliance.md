---
title: Security and Compliance Controls
archetype: documentation
status: beta
owner: Security Guild
maintainer: Risk & Compliance Team
version: 0.1.0
tags: [security, compliance, eu-ai-act, governance]
last_reviewed: 2025-03-01
---

# Security and Compliance

AI Reading aligns to EU AI Act risk-based requirements by classifying use cases as **limited risk** (knowledge assistance) with safeguards that prevent escalation into high-risk processing.

## Governance approach
- **Risk assessment**: Run quarterly AI impact assessments to validate scope, datasets, and residual risk. [CITE:EU_AIACT]
- **Role separation**: Ingestion, compliance, and runtime responsibilities are split across agents and human owners to ensure no single failure bypasses controls.
- **Evidence management**: All agent decisions log timestamp, user role, prompt, retrieved sources, and guardrail verdicts for audit readiness.

## Controls by phase

### Ingest
| Control | Description | SMB Considerations | Enterprise Considerations |
| --- | --- | --- | --- |
| Data classification gate | Require metadata tags (confidentiality, department, retention) before ingest. | Lightweight CSV template and CLI prompts. | Integrate with data catalog APIs (Collibra, Purview). |
| PII masking | Regex and ML-based detection mask sensitive identifiers prior to storage. | Enable default regex pack; manual review for edge cases. | Extend with DLP tooling and regional policy packs. |
| Source approval workflow | Document owners approve ingestion runs. | Email confirmation logged in ingestion report. | Integrate with ticketing systems for traceability. |
| Hash-based deduplication | Prevent redundant storage and reduce leakage surface. | Optional flag in Makefile; manual review acceptable. | Mandatory with automated reports to compliance. |

### Runtime
| Control | Description | SMB Considerations | Enterprise Considerations |
| --- | --- | --- | --- |
| Role-based retrieval filters | Apply metadata filters based on IAM groups. | Local user mapping file maintained by Manager of AI. | Sync with enterprise RBAC and ABAC policies. |
| Prompt screening | Compliance agent scores prompts for risk terms and blocks as needed. | Maintain simple deny-list and manual override. | Use guardrail config tied to policy references and alert SOC on blocks. |
| Context integrity check | Validate retrieved chunks for classification mismatches. | Warning log with manual follow-up. | Automatic block with ticket creation and retagging workflow. |
| Secure inference channel | Enforce TLS between orchestrator and model servers. | Use self-signed certs with documented rotation. | Integrate with corporate PKI and HSM-backed certificates. |

### Post-run
| Control | Description | SMB Considerations | Enterprise Considerations |
| --- | --- | --- | --- |
| Audit log retention | Store immutable logs for minimum 12 months. | Local append-only JSON with off-site backups monthly. | Centralize in SIEM with WORM storage and retention policies. |
| Adoption analytics review | Monthly review of usage anomalies to detect misuse. | Manager of AI leads review with manual spreadsheet. | Automated dashboards with anomaly alerts to risk committees. |
| Incident response | Documented runbook for blocked or high-risk events. | Shared wiki page with clear escalation contacts. | Integrated ServiceNow workflow with RACI mapping. |
| Model update approval | Re-validate models prior to deployment. | Lightweight checklist signed by Program Manager. | Formal change advisory board with regression tests. |

## Data residency and privacy
- All inference stays within customer-controlled infrastructure; no default outbound API calls.
- Configure regional storage paths for vector databases to align with data residency commitments.
- Adopt privacy-by-design practices, including data minimization and purpose limitation logs. [CITE:EU_AIACT]

## Continuous compliance activities
1. **Monthly**: Review guardrail effectiveness metrics, blocked prompts, and adoption anomalies.
2. **Quarterly**: Reassess risk classification, validate documentation, and refresh training for operators.
3. **Annually**: Conduct independent audit of logs, controls, and policy alignment; update governance playbook for EU AI Act refinements.
