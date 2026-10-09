# Four-day sprint — parallel work / dependency-safe execution (2026-10-09)

**Internal freeze:** October 13, 2026. Public cutoff: public announcements indicate October 14 13:00 Taipei; Team C must verify precise portal requirements. **First goal: Chinese preliminary deck + mandatory summary.** Prototype is a supporting exhibit; complete demo is described for finals in provided template.

## Workstreams and file ownership

| Agent (separate chat) | Independent R0 starts NOW | Downstream gate (only dependent subsection waits) | Owned outputs |
| --- | --- | --- | --- |
| **A / Slides #2 / P0** | Chinese slide story, summary, 13-slide candidate narrative, placeholder visuals | C verified rules/claims + D architecture/KPIs for final copy; B screenshots only for replacement | `slides/` |
| **B / Prototype #3 / P1** | Four-screen fictional-data storyboard/clickable mock; screenshot pack | C mascot/asset rights only if adding official mascot; A finalized copy only for final polish | `prototype/` |
| **C / Research #4 / P0** | Confirm portal/rules, existing yoxi functions, competitors, mascots, API feasibility | No inbound dependency; inaccessible portal becomes **owner action** not full team blocker | `research/verified-findings.md` |
| **D / AI evaluation #5 / P1** | Deterministic push policy, Jev evaluation plan, 8 fixtures, privacy, 3 KPIs | C vendor/API facts only for final integration statements; no need to test Jev to deliver honest proposal | `research/ai-evaluation.md` |
| **M / Coordinator #1 / P0** | Coordinate, monitor GitHub handoffs, document decisions, assemble final deck | Requires A content, C official checks, D verified wording and optionally B visuals; explicitly scope out missing noncritical additions | `docs/`, integration |

## Producer → consumer contracts

- **C0 on Oct 09 → A + M**: source-verified 15-page/summary/format/date facts, unresolved portal needs; **C mascot → B**; C competitor → A; C API → D.
- **D0 on Oct 10 → A + M**: 1-slide architecture + safe Jev wording + concrete KPI definitions and mock vs real labels.
- **B0 on Oct 10 → A**: four scenario screens and accurate descriptions. **B1 by Oct 11**: screenshots or durable link; if B slips, A uses wireframes and proceeds.
- **A0 on Oct 10 → M**: fully written proposal text; no waiting for C/D/B. **A1 Oct 11**: source-corrected, visually integrated reviewable deck.
- **M by Oct 12**: adversarial review and gap resolution. **Oct 13**: export/freeze/check page count and portal submission buffer.

## Ready-to-start policy
1. Each agent claims issue immediately then produces R0 baseline **from current frozen docs**. Missing upstream work means `[待查證]`, `[模擬]`, or separate `BLOCKED-ON-OWNER` section; it **does not stop unrelated progress**.
2. No downstream sign-off using unverified assumptions. Every dependent revision cites upstream GitHub issue, exact immutable SHA and confidence/limitations.
3. Source-of-truth versioning: A owns slides, B prototype, C verified findings, D AI eval, M docs/integration. No parallel overwrite of same files.
4. Working state on GitHub: `CLAIMED → IN_PROGRESS → READY_FOR_REVIEW → COMPLETE` or `BLOCKED` with slice and next action; cross-link producer/consumer.
5. Post important decisions, sources, caveats, test evidence, exact commit SHAs and handoffs **on GitHub**; this includes M.
6. Nothing about a repo issue automatically executes an agent; owner launches chats using [team launch prompts](TEAM_LAUNCH_PROMPTS.md).
7. Real competition team requires **2–5 humans**. AI agents don't qualify.
