# TEAM A — A0 Deck Artifact QA / GitHub-first handoff
**Date:** 2026-10-10 (Asia/Taipei)  
**Issue:** #2 · **Owner:** Team A  
**State:** READY_FOR_REVIEW (R0) — Team D R1 claim review and Team M final approval outstanding.

## What exists now
- `slides/slide-copy.md`: complete Chinese summary + every main/appendix page, visual treatment, speaker cues, source provenance and explicit [模擬]/[待驗證] status.
- Created external ChatGPT-conversation attachments for **fully editable PowerPoint** `yoxi-suixing-preliminary-2026.pptx`, **PDF export** `yoxi-suixing-preliminary-2026.pdf`, **reproducible generator** `build_deck.js`, **literal slide text/notes** `slide-copy.md`, and **two original Team B SVG sources**. Coordinator must obtain attachment copies from Team A's delivery response and check them into this branch or a GitHub Release before considering binary-file archival complete.
- Tool environment could not authenticate or push binary files from the local slide-generation runtime to GitHub. **The PPTX/PDF are real files and have been exported and visually reviewed, but are not claimed to be committed to this PR.** Do not confuse committed page copy with source binary archival.

## Exact slide counts
| Category | Count |
|---|---:|
| Compulsory seven-field summary | 1 (excluded) |
| Main body, including cover and closing | **15 / 15** |
| Appendix (sources and evidence-status register) | 2 |
| Total PDF/PPTX | **18** |

## Local build and verification performed (not CI)
- Source: `build_deck.js`, generated via Node 22 + PptxGenJS. All ordinary slide headlines, body copy, cards and diagrams are native editable PowerPoint elements; the two embedded Team B mock illustrations are image assets, separately accompanied by editable original SVGs.
- PDF: LibreOffice `soffice --headless --convert-to pdf`, successful.
- Structural: python-pptx and PyMuPDF opened both deliverables and independently counted 18.
- Render: all 18 PDF pages rasterized into a contact sheet; visually inspected, then repaired a clipped summary row, re-exported and examined the summary at larger scale.
- Required summary fields in prescribed order; literal `運用到的AI技術、服務或模型等資源` appears in the PowerPoint source (PDF extraction may add spaces between Chinese/Latin token runs).
- Native Team B original SVG sha1 git blob equality manually verified with source blobs (final newline removed): 03-chat `18f9e54c525dd09b20aea836606dad67f5aeb9e8`, 04-replan `191d1b6e2c7234f7ec87702b2146f119301b060d`.
- Final local SHA256: PPTX `7722fc299d0935925a8bbde25246efc1c7c4192273a00b19620d9012665ea15f`; PDF `079cd1947c8603a3835a1b5d6c2608e3fa69d86285d6374aa592cfb9486612c3`; generator `c473164a1f6057aa3f9da362d2c158b13e380657f2d93351b9106e4d641aa1ec`.
- No live integration, user experiment, model benchmark, stopwatch-video timing, or successful submission test was performed or implied.

## Supporting upstream evidence
- [Competition rules / organizer campus briefing](../docs/COMPETITION_RULES.md): separate required ~3-minute **Unlisted** video + <=15 main slide deck; summary not counted.
- [Frozen concept](../docs/PRODUCT_BRIEF.md) and [architecture](../docs/ARCHITECTURE.md).
- [Team C PR #6](https://github.com/jamshih/-/pull/6), immutable `737668222087cf8d14150444210ca5152c0fd445`.
- [Team B PR #7](https://github.com/jamshih/-/pull/7), immutable `9a882e9c2ee82f11135c5587e90a1b21fa27233f`.
- [Team E #8 / PR #9](https://github.com/jamshih/-/pull/9), on-camera human presentation planned after Team M approval.

## R1 / QA acceptance gates
1. **Team D #5:** independently review exact Jev NOT TESTED status, guardrail ordering, AI roles and valid KPI definitions. Provide pinned SHA to Team A and M before final approval.
2. **Team C / M:** check all market/publisher claims against accessible sources; do not assert global novelty.
3. **Team M / owner:** confirm 2–5 real entrants; login-verified upload file format/max size, brand/logo/IP conditions and confirmation receipt; coordinator re-downloads both PPTX/PDF attachments; rechecks 1 + 15 + 2 and Chinese fonts; stages binary files in persistent repo/Drive.
4. **Team E / presenter:** use headline anchors but record only once claims gate passes. Video made by human entrant personally, 3-minute Unlisted link and portal upload still required.
5. If source constraints change, rev bump A0 → A1 with updated binary exports, checksums, complete source and matching copy.
