# GitHub-first protocol — mandatory for EVERY workstream (including Team M)

**Source of truth = GitHub issues, committed files, and linked PRs.** Chats are temporary execution contexts. Never call a task 'done' based on a chat summary alone.

## Before starting
1. Read `README.md`, `docs/PRODUCT_BRIEF.md`, `docs/COMPETITION_RULES.md`, `docs/DECISIONS.md` and **your assigned GitHub issue**.
2. Comment on the issue with `CLAIMED`, your intended deliverables and any dependency.
3. Avoid editing files owned by another team. Coordinate contested design changes on the issue; no sweeping redesign.

## During work — post a GitHub comment at each checkpoint or blocking decision
Copy this format:
```
### HANDOFF UPDATE — YYYY-MM-DD HH:MM +08
Owner/workstream: [A/B/C/D/M]
State: CLAIMED / IN_PROGRESS / BLOCKED / READY_FOR_REVIEW / COMPLETE
Immutable artifact: [commit SHA, blob SHA, PR link, or linked output]
Completed: [specific evidence or files]
Sources: [source URL + access date, if external claim]
Verification: [what was checked, test result, page count, simulated data markers]
Open risks / unanswered: [...]
Need from others: [...]
Next exact action: [...]
```
Post immediately if you find a blocker, important source correction, rejected claim, or changed acceptance requirement. Never leave findings trapped in chat.

## End of work
- Commit versioned text/design/code to the repo where possible; if file cannot be committed, post an accessible artifact reference + owner, type, expected path and upload instructions.
- Link exact immutable commit SHA, files, evidence and known limitations in a `COMPLETE` issue comment.
- Cross-link affected team issues. Do not silently change frozen product direction; proposed changes require rationale, consequences and Team M approval in `docs/DECISIONS.md`.
- If tests or tool access are unavailable, explicitly state **NOT VERIFIED**. Never fabricate success, user research, real-time traffic, booking integrations or measurable KPI gains.

## Review and integration — Team M must follow this too
Team M checks GitHub issue status, evidence, completeness, ownership and integration before considering work finished. Team M logs ALL scope changes, constraints, key research, merge decisions, submission confirmations and remaining risks **on GitHub**. A daily coordinator checkpoint (or earlier if blocked) is mandatory.

## Communications SLA (compressed sprint)
- Post a short update after each meaningful deliverable; blocking issues immediately.
- Critical blockers have priority over polishing.
- If output is not on GitHub, coordinator treats it as not handed off.
