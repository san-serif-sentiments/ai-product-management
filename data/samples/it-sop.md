---
title: IT SOP - Patch Management
archetype: sample-doc
status: approved
owner: IT Operations
maintainer: Infrastructure Team
version: 2.1.0
tags: [it, sop, security]
last_reviewed: 2025-01-30
---

# Patch Management SOP

## Objective
Maintain secure, up-to-date endpoints supporting AI Reading infrastructure.

## Scope
- Applies to all servers, desktops, and containers hosting AI Reading components.

## Procedure
1. **Inventory**
   - SMB: Maintain device list in shared spreadsheet updated weekly.
   - Enterprise: Sync CMDB (ServiceNow) nightly.
2. **Assess**
   - Evaluate criticality using vendor advisories and internal risk scoring.
   - Prioritize patches affecting Ollama/LM Studio runtimes and vector stores.
3. **Deploy**
   - Stage patches in test environment; verify ingestion and retrieval smoke tests.
   - Use `make patch-apply` for Compose stack.
4. **Validate**
   - Confirm services running; review logs for errors.
   - Enterprise: Capture evidence screenshots for compliance audit.
5. **Report**
   - Publish monthly patch compliance score.
   - Escalate overdue critical patches to Manager of AI.
