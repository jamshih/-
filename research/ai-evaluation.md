# Team D — AI architecture, notification policy, Jev feasibility and evaluation

**Project:** 出門再說 / yoxi 隨行 · 2026 和泰 AI 黑客松
**Owner / tracker:** Team D, [Issue #5](https://github.com/jamshih/-/issues/5)
**Prepared:** 2026-10-10 Asia/Taipei
**Status:** **READY FOR REVIEW — proposal/evaluation evidence**, NOT a built or partner-authorized AI service.
**Immutable implementation/evidence:** this document and the accompanying `research/notification_gate_reference.js` are recorded at the PR's exact head commit once published; no moving-head claims are authoritative.
**Input contracts:** repository `docs/PRODUCT_BRIEF.md`, `docs/ARCHITECTURE.md`, `docs/COMPETITION_RULES.md`, `docs/SPRINT_PLAN.md`, `docs/HANDOFF_PROTOCOL.md`; Team C [PR #6](https://github.com/jamshih/-/pull/6) source addendum at `b7aca6c7d9ac843485b3580869ff836761054d9d`; Team B [PR #7](https://github.com/jamshih/-/pull/7) offline mock. Product direction remains frozen, and this research does not amend it.

## 1. One-slide diagram — paste into Chinese preliminary deck

**Slide heading:** 從提醒到行動：可信任的 AI 出行決策鏈

~~~text
[使用者逐項同意：通知／日曆／位置／偏好]  [可信來源：天氣／交通]
                       ↓
[情境標準化：活動時間、事件 ID、來源與資料時效]
                       ↓
[硬性規則閘門：無同意／取消／過期／靜音／重複／冷卻 → 不推播]
                       ↓
[「值得打擾嗎？」決策：可解釋規則基線]
[可選 Jev 判斷訊號（實驗中，尚未測試或導入）]
                       ↓
[一次有來源的提醒] ─ 點開 ─> [提醒是同一段聊天室的第一句]
                       ↓
[LLM：理解需求、選用工具、整理答案，不能捏造即時資訊]
                       ↓
[可信資料工具：路線／大眾運輸／天氣；yoxi ETA／車資／派車需授權]
                       ↓
[後端驗證 → 結構化比較卡：捷運／步行／yoxi／不叫車]
                       ↓
[使用者明確確認叫車與付款；Rive 可選、非核心]
~~~

**Speaker copy, approximately 25–30 sec (Chinese):**
> 「隨行不是讓 AI 自己決定叫車。使用者先同意資料用途，系統再用明確規則排除深夜、重複、過期和不重要的提醒。真正值得打擾時，通知就是對話的第一句。AI 負責理解需求與整合工具結果，路線與車資須來自經授權的資料服務，不由語言模型猜測。即使建議搭捷運、不叫車，也能創造日常價值；叫車始終由本人確認。」

**Slide-side badges/labels (truthful):** 已製作：四幕離線互動「模擬」原型（Team B）；已執行：22 個合成規則測例；提案中：真實情境來源、LLM 編排；尚未測試：Jev 在交通推播決策的準確度；需外部授權：即時資料、yoxi 叫車／車資／ETA。

**Integration warning:** Team B has implemented scripted HTML/SVG screen transitions only; there is no real permission flow, operating-system push, backend, LLM, Jev, transit integration, ETA or dispatch. Screen times/fares/routes and rain are **[模擬]**, not live. The presenter must not attribute architecture implementation to the prototype.

## 2. Notification decision contract: safe, explainable, consent-first

### Distinct phases

1. **Trigger only from allowed sources.** Separate granular opt-ins for push, calendar, location, travel preferences. A user may manually type or invoke 「直接叫車」 with no calendar/location permission. Notification consent never automatically implies calendar consent; source permissions are scoped and revocable.
2. **Normalize on a trusted backend.** Context object must contain tenant/user identity, consent scopes and version, event ID/type/status, trusted provider, source timestamp, receipt timestamp, expiry, suggested action, event time, and timezone. Never accept a client-asserted `source_verified=true` as authority in production.
3. **Apply non-bypassable, deterministic deny rules.** No push consent or opted out; unrelated source scope; marketing without dedicated consent; canceled/nonexistent event; unknown or stale weather/transit; unsupported freshness/expiry; quiet hours; earlier identical notification; active cooldown; exceeded per-day budget; event not in actionable lead window. Reject instead of guessing. User-requested manual chat remains possible.
4. **Evaluate relevance only for hard-gate survivors.** Rule baseline requires actionable **material change** and meaningful impact relative to a known user goal. The research candidate Jev may later provide a bounded `RELEVANT/NOT_RELEVANT/REVIEW` or score signal; it can **never override suppression**. Initially shadow-evaluate; then cautiously use as a *filter/ranker*, not to expand send authority without a separate safety review.
5. **Atomic delivery eligibility and idempotency.** Persist a dedup fingerprint (user + logical event + source generation + notification kind), quiet-hour decision and rate-limit counter under a database transaction/unique index. An asynchronous push enqueue is not a successful delivery; record proposed/queued/accepted/delivered/opened separately. Retried workers and multi-device tokens share one logical event decision. TTL, user cancellation and opt-out must be rechecked just before enqueue.
6. **Interruption is scarce.** Default *illustrative product policy*, not adopted limits: quiet 22:00–07:00 Asia/Taipei, 2 proactive travel pushes/day, one per unique event, and a configurable cooldown. These require user research, user preference controls, and an explicit policy for emergency exceptions; the R0 sample has **no emergency bypass**.
7. **Provide clear reason and control.** Sent message states observed change, source/age, consequence, route/action choices and 「略過／暫停提醒／調整設定」. No undisclosed ad; taxi is not always the winner.

**Pseudocode:**

~~~text
candidate = normalize(trusted_event, consented_context)
if missing_permission OR opted_out OR canceled OR stale_or_unverified:
    SUPPRESS(reason)
if quiet_hours OR duplicate OR cooldown OR cap_reached:
    SUPPRESS(reason)
if outside_time_window OR not_actionable_material_change:
    SUPPRESS(reason)
# ONLY after these checks:
relevance = deterministic_baseline(candidate)
# Optional future Jev signal: shadow first, does not override hard denies.
if relevance fails: SUPPRESS("insufficient relevance")
atomically claim (user_id, event_fingerprint, policy_version)
if claim fails: SUPPRESS("duplicate")
revalidate consent/event/source freshness
enqueue notification; retain trace IDs and limited audit metadata
on tap: resume same chat, validate tool results, offer options
on booking: fresh partner terms + explicit user confirmation
~~~

**Important correctness boundary:** The JavaScript reference harness implements a *single-process pure-function sample* and returns `SEND_CANDIDATE`; it **does not** implement atomic claims, server-side authenticated source records, OS permission checks, durable counters, actual sends, or a working consent DB. Treat production semantics above as design requirements, not tested implementation.

### Relevance principles

- Notify about a material, **timely, actionable** disruption to a user-authorized schedule or travel intent, not merely rain/traffic in the city.
- A study-place exploration that does not involve taxis is a valid **in-chat** recommendation; it must not be forced into unsolicited ride-promotion.
- Suppress if event was canceled, context missing, destination inconsistent, source stale, mode/POI inaccessible, or evidence cannot be attributed.
- Strict separation between **push decision** and **content personalization**. The LLM does not choose to bypass the push gate.
- Trace each decision by policy version, event fingerprint, permission version, source freshness and bounded reason code, with privacy-preserving retention.

## 3. Synthetic decision fixtures and reproducible test evidence

**Reference file:** [research/notification_gate_reference.js](notification_gate_reference.js) (Node.js without packages).
**Run locally:** `node research/notification_gate_reference.js`.
**2026-10-10 test evidence:** 22 of 22 cases passed when the **exact JavaScript pure function and fixture objects** were executed in the agent's JavaScript tool sandbox; 0 unexpected results. All input events, flags, user times and expected outcomes were author-defined. This is a **synthetic contract/unit smoke test**, not a model benchmark, UX A/B test, API verification, notification delivery test, or independent gold-standard annotation. Re-run in Node and record its separate result before claiming Node runtime validation.

| ID | Synthetic situation | Expected push outcome | Dominant reason |
| --- | --- | --- | --- |
| 01 | Consented, fresh forecast threatens 18:30 appointment | **SEND_CANDIDATE** | timely + actionable change |
| 02 | Verified transit interruption with route consequence | **SEND_CANDIDATE** | meaningful confirmed delay |
| 03 | User asks where to study; a taxi need not be used | **CHAT_ONLY**, no push | user-initiated help |
| 04 | Same rain alert already sent | **SUPPRESS** | dedup event key |
| 05 | Traffic report older than source-specific TTL | **SUPPRESS** | stale evidence |
| 06 | Candidate at 23:00 in configured quiet hours | **SUPPRESS** | quiet hours |
| 07 | Calendar event canceled | **SUPPRESS** | event lifecycle |
| 08 | Ordinary sunny on-time commute | **SUPPRESS** | no material change |
| 09 | User has not consented to push | **SUPPRESS** | push consent |
| 10 | Required location permission not granted | **SUPPRESS** | context-scope consent |
| 11 | Last alert still within cooldown | **SUPPRESS** | cooldown |
| 12 | Daily unsolicited notification budget reached | **SUPPRESS** | rate limit |
| 13 | A model says SEND but event was already sent | **SUPPRESS** | model cannot override dedup |
| 14 | Weather rumor without trusted source | **SUPPRESS** | source verification |
| 15 | Trivial or nonactionable difference | **SUPPRESS** | insufficient relevance |
| 16 | Event outside configured lead-time horizon | **SUPPRESS** | too early |
| 17 | Event time already passed | **SUPPRESS** | no remaining action window |
| 18 | Confirmed significant disruption, user enabled | **SEND_CANDIDATE** | high-impact timely change |
| 19 | Pure taxi marketing push not consented | **SUPPRESS** | promotional content |
| 20 | Untrusted text instructs “SEND NOW” but no material change | **SUPPRESS** | structured rules ignore instruction |
| 21 | Event source expires before evaluation | **SUPPRESS** | expired data |
| 22 | Negative source age due to inconsistent clock | **SUPPRESS** | invalid time/freshness |

**What the test did NOT establish:** Test fixtures are designed to match the implementation; they are not independently labeled by travelers. No statistical accuracy, precision, recall, calibration, fairness, Jev performance, real weather accuracy, timezone-library certification, distributed dedup, provider rate-limit resilience, operational SLO, or private API access can be inferred from 22/22. Additional negative tests for missing/malformed schema and transactional duplicates are required before any production claim.

**Extra production test plan:** Test DST/timezones outside Taiwan, clock skew, permission revocation between eligibility and enqueue, cancellation race, concurrent sends across devices/workers, unstable upstream source changes, API outages, same logical disruption with new provider ID, human language/prompt injection, mismatched locations, no availability and fare/booking rollback.

## 4. Jev feasibility research — candidate, not implemented

**Identity and method verified from primary vendor materials:** TypeSafe AI's Jev is a **typed decision model**, NOT an open-ended conversational LLM. It receives compact `state` plus narrowly defined typed questions and returns structured Choice, Score or Noul (yes/no probability) judgments. Vendor launch page reports low per-input-token pricing and favorable latency in vendor-controlled workloads. Those are **vendor claims**, not our deployment metrics: https://typesafe.ai/blog/introducing-system-one-models-and-jev ; https://docs.typesafe.ai/introduction (checked 2026-10-10).

**Independent context, not validation of travel use case:** Deußer, Sparrenberg & Sifa (2026-09-29), *Evaluating and Benchmarking the System One Model Jev*, https://arxiv.org/abs/2609.37647, evaluate version 1.13.0 on 37 public datasets. Their findings include task-dependent performance, weaknesses on fine-grained/noisy classification and threshold placement for binary probabilities. Their results are **NOT** a mobility-notification benchmark, and do not license any claimed accuracy, latency or lift for this product. The paper itself identifies calibration differences by task. Do not quote favorable general benchmarks as product KPIs.

**Crucial vendor-documented limitations** (https://docs.typesafe.ai/model-jaggedness/jev-1.13, last-reviewed 2026-10-02, checked 2026-10-10):
- Numeric arithmetic, counts, time-window ordering and date comparisons belong in **code**.
- Larger irrelevant state/context, indirect phrasing, conflicting instructions and option-order bias can degrade answers.
- Untrusted state can contain adversarial instructions; vendor explicitly warns it is **not hostile-input-safe by default**.
- Jev does **not generate user explanations, route results, maps, prices or dialogue**. Typed output is syntactically bounded; this does **not** guarantee semantic correctness.
- Probability numbers are not proof of correct real-world calibration. Any threshold must be selected from human-labeled, separate validation data and then checked on a held-out test set.

**Appropriate possible decision role:** After hard eligibility rules, give Jev a *minimal, redacted* state such as `{type: transit_disruption, impact_bucket: high, user_goal: reach_calendar_event, actionable_alternative: available, freshness_bucket: current}`; ask separate bounded questions, e.g. `choice: Is this candidate materially relevant to the authorized trip? relevant / irrelevant / unsure`; optionally `score: likely nuisance to interrupt now? low / medium / high`. Combine answers deterministically. No raw calendar description or GPS trace unless privacy/legal/vendor retention assessment expressly permits it.

**Experiment status:** **NOT TESTED** with Jev. No TypeSafe key, paid calls, response logs, model-version confirmation, task-level confusion matrix, latency distribution, calibration plot, or live service integration in this workstream. API ownership and exact deployed model build must be pinned and logged if tested. Do not confuse independent Jev resellers, similarly named websites, or generic benchmark repositories with verified authorized service access.

### Offline bake-off before choosing Jev

1. Define task taxonomy and human rubric **before** model prompts: `valuable_push`, `nuisance`, `critical_missed`, `manual_only`, `invalid_input`; separate safe eligibility from discretionary value.
2. Seed with the 22 public synthetic cases, then obtain **consented, minimized** examples and at least two independent human raters per sample; adjudicate disagreements. Include Chinese text, noisy weather/transit, ambiguity, non-taxi suggestions, false sources, cancellation, option permutations and injected instructions. Suggested starting scale **200–300 labeled cases** is a trial planning quantity, not collected evidence.
3. Pre-register fixed test/validation splits by **user and event**, not message, to prevent leakage. Freeze prompt, model version, cost accounting, source data and code. Tune thresholds *only on validation*, reserve holdout test for final comparison.
4. Compare **A pure rules baseline**, **B rules + Jev shadow**, **C rules + a cheaper constrained LLM-as-classifier**, if credentials/data policies permit. Hard gate is identical across variants. No model should gain extra send authority just for scoring high.
5. Report precision of human-judged useful alerts, recall for human-defined important alerts, nuisance false-positive rate, false-negative critical-event rate, abstention, per-language and user-group breakdown where lawful, p50/p95 end-to-end latency, invalid-output rate, model calls, actual bill, and sensitivity to threshold, option order and prompt injection.
6. **Go/no-go:** Require a pre-agreed risk budget and statistically defensible improvement over rules on the held-out set **without worse important-alert recall, consent breaches, or higher nuisance**. On unknown score, timeout, outage, drift, schema mismatch or unauthorized data processing, fall back to rule baseline/suppress; do not silently fail open.

### Comparison — not a foregone conclusion

| Approach | Strength | Weakness | Recommendation |
| --- | --- | --- | --- |
| Rules only | Auditable, cheap per evaluation, deterministic consent/time/dedup/TTL | Hard to capture nuanced subjective relevance | **MVP and always-on safety baseline** |
| Rules + Jev | Typed bounded decisions/probabilities; promising for small judgments | Paid hosted dependency, no travel-domain labels, semantic errors, private-data controls needed | **Shadow experiment only until evaluated** |
| Rules + constrained LLM classifier | Flexible Chinese language and contextual reasoning | Slower/costlier potentially, variability, parse/validation and injection risks | **Research comparator, not policy authority** |
| LLM decides everything / issues push | Superficially simple | Unsafe permission/time/action overrides, unverifiable claims | **Reject** |

**Possible value of Jev is narrower than “smarter AI”:** It may rank marginal relevance on safely eligible events, and the actual research question is whether that improves human usefulness under a missed-critical-alert budget. If no measurable lift, retain rules.

## 5. LLM orchestration versus trusted transport and booking systems

The language model's approved roles are (a) intent parsing, e.g. 「我不想淋雨」, (b) selecting tools and bounded parameters, (c) presenting source-backed alternatives and clarifying missing preferences, (d) generating human-friendly explanation using verified fields. The **backend** owns OAuth/partner credentials, routing permissions, argument allowlists, geofence restrictions, rate limits, quotas, freshness checks, final price/availability assertions and booking mutation. Treat all provider text as **data**, never privileged prompts.

**Proposed tool boundaries:**
- **Weather:** CWA Open Data datasets subject to user key/terms; must evaluate location/forecast resolution and freshness. Official portal: https://opendata.cwa.gov.tw/user/authkey.
- **Transit/traffic:** TDX documented datasets and authenticated quota/coverage, or authorized Google Routes Transit; read attribution, geography, supported service conditions and billing. https://tdx.transportdata.tw/api-service/swagger ; https://developers.google.com/maps/documentation/routes/transit-route ; https://developers.google.com/maps/documentation/routes/policies ; https://developers.google.com/maps/billing-and-pricing/pricing.
- **Calendar/location/OS push:** Separate explicit user consent, permission revocation and OS constraints; don't scrape or assume access. https://developer.apple.com/documentation/EventKit/accessing-calendar-using-eventkit-and-eventkitui ; https://developer.apple.com/design/human-interface-guidelines/managing-notifications.
- **yoxi booking/ETA/fare:** Official passenger tutorial documents consumer booking features (https://www.yoxi.app/passenger-tutorial), **not a publicly provisioned partner API**. Private dispatch, live fare, quote and payment require commercial integration, consent, secure server credentials and documented terms. If not available: show **[模擬]** and stop at fake confirmation screen with no dispatch.

**Validated card contract (illustrative fields, not a connected API response):**

~~~json
{
  "trace_id": "synthetic-trace-001",
  "origin": "使用者選定地點",
  "destination": "高雄捷運巨蛋站",
  "evidence": {
    "source": "mock",
    "source_timestamp": "2026-10-10T17:20:00+08:00",
    "freshness_status": "SIMULATED"
  },
  "options": [
    {
      "mode": "transit",
      "duration_minutes": null,
      "fare_twd": null,
      "availability": "UNVERIFIED",
      "action": "VIEW_DETAILS"
    },
    {
      "mode": "yoxi",
      "duration_minutes": null,
      "fare_twd": null,
      "availability": "UNVERIFIED",
      "action": "OPEN_EXPLICIT_CONFIRMATION"
    }
  ],
  "simulation_label": "[模擬畫面]",
  "booking_status": "NOT_SUBMITTED"
}
~~~

In a future real adapter, null/unknown is **not** zero fare or a confirmed ETA. Require allowlisted `mode` and `action`, valid provenance/TTL, UI disclaimer, explicit quotes and a fresh price before booking. A model's statement “booked” is not a booking receipt. Rive state (idle/rain/replanning) is decorative and must honor reduced-motion settings.

## 6. Three credible KPIs and realistic experiment plan

**All baselines, targets, uplifts and real conversion effects: NOT MEASURED.** First determine denominators and instrumentation privacy acceptance. Never optimize clickbait pushes or taxi-only conversion.

1. **Useful-notification precision (quality KPI):** Human-judged valuable delivered pushes / all independently judged sampled delivered pushes, with confidence intervals and user-segment coverage. Collect one-tap 「有幫助／打擾」 plus blinded annotation; account for nonresponse bias. Pair with **important-event recall** among independently reviewed eligible critical cases as a safety guardrail.
2. **Seven-day useful engagement days (high-frequency KPI):** Average number of distinct days in a seven-day window on which a consenting active participant intentionally completes at least one legitimate mobility aid action (views route comparison, accepts a non-taxi suggestion, or completes a confirmed ride). Exclude automatic push receipts, background pings and idle app opens. Disaggregate **no-booking useful days** vs booked days. Include per-user cohort denominators and retention.
3. **Notification trust harm rate (guardrail KPI):** (mute, push opt-out, and negative-relevance feedback events attributable to proactive messaging) per **1,000 delivered travel notifications**, with event-specific attribution windows and individual component rates reported to avoid obscuring severe opt-outs. Also track duplicate sends, permission violations, false claims, and cost per useful action as stop metrics.

**Experiment sequence:** (0) 22 synthetic smoke fixtures — **done**; (1) 200–300 illustrative planned consent-safe, double-human-labeled cases, with baseline rules and shadow model — **not done**; (2) 1–2-week authorized backend shadow trial without real pushes, measuring freshness, candidate recall, cost, and safety — **not done**; (3) optional limited randomized opt-in user pilot, **rules vs rules-plus-validated-filter**, with stable assignment, predeclared sample size/power, 2–4 weeks observation, no new automatic booking authority, staffed monitoring and instant fallback — **not done**. Treat stage lengths as planning estimates, not sponsor commitments; use a power calculation after baseline variability. No arbitrary “30% retention increase” story.

**Stop/rollback conditions:** unauthorized source use, consent mismatch, repeated duplicate push, severe quiet-hour breach, unexplained surge of nuisance/mute, missed critical events above predeclared budget, misrepresented fare/ETA or incorrect dispatch state. Results require CI and cohort details before external promotion.

## 7. Cost, privacy, security, operations and dependencies

**Cost structure (budget worksheet, not an actual quotation):** Weather/transit/maps provider tariffs + attribution + provider quotas + server/DB/queues + push infrastructure + LLM tokens on conversations + optional Jev tokens + logging and human evaluation/QA. Rules still require hosting and reliable data subscriptions; zero model-token cost is not zero end-to-end cost. Vendor-listed Jev reference **US$0.042 per million input tokens** (TypeSafe announcement, accessed 2026-10-10): if 100,000 candidate evaluations contained 800 billed input tokens each, the illustrative *model-only* nominal amount is **US$3.36** (100,000×800÷1,000,000×0.042). This is arithmetic based on vendor list price, **not an invoice**, ignores minimums/tiers, retries, transport, regional taxes and non-Jev system costs. Revalidate all price terms before procurement. Maps/route usage could dominate and is unpriced without volumes and contract.

**Privacy/security:** No unauthorized calendar ingestion or background location tracking. Minimize to coarse trip-impact features and ephemeral relevance buckets, avoid sending addresses/event titles into third-party models; encryption in transit/at rest; role-based access; secret rotation; model/provider DPA and storage/training location review; configurable retention/deletion; transparent consent, easy revocation and manual-mode utility. Prevent prompt injection from scraped events/venues, forged provider freshness, cross-user dedup leakage, push payload PII on lock screens, unauthorized partner dispatch, accidental logging of precise location. Operational revocation must immediately block *queued* sends too. Seek legal/privacy review before production use.

**Dependencies from C:** credential/key/terms/access for CWA, TDX, mapping, any venue quality data; actual API coverage and service economics unknown; partner agreement and stable private yoxi APIs unknown; brand/mascot rights unknown. Live logged-in competition portal still requires human owner validation. The initial proposal includes the mandatory ~3-minute Unlisted YouTube video and slide deck, not an obligatory final-round-grade backend prototype.

**Optional ideas — require Team M approval, NOT MVP prerequisites:**
1. **Explain-why + snooze feedback chip:** high user trust / low-to-medium implementation effort; directly exposes reason and reduces nuisance.
2. **No-booking useful-day mode:** high goal alignment / medium effort; explicit study-spot/walk/transit suggestions with no taxi upsell.
3. **Pretrip reliability card:** medium value / medium-high integration effort; publish confidence + age of evidence, never a fabricated promise.

## 8. Evidence/status matrix — avoid presentation overclaim

| Element | Classification | Evidence / gate |
| --- | --- | --- |
| Product framing, consent-first architecture, rule contract | **PROPOSED / DOCUMENTED** | Frozen docs + this report |
| Four-state clickable concept + vector screens | **IMPLEMENTED AS OFFLINE [模擬]** | Team B PR #7, NOT production AI |
| Pure-function notification gate + 22 synthetic fixtures | **IMPLEMENTED + TESTED IN JS TOOL SANDBOX** | `research/notification_gate_reference.js`; 22/22 expected fixture outcomes; Node re-run pending |
| Real push delivery, user permission state, backend transaction, live APIs | **NOT IMPLEMENTED / NOT TESTED** | Needs backend, credentials, contracts |
| Jev real call, accuracy/latency/cost, travel-domain calibration | **NOT TESTED** | Candidate only, needs API key + human eval |
| Conversational LLM and tool orchestration | **PROPOSED, NOT IMPLEMENTED** | No live LLM in Team B prototype |
| Google/TDX/CWA live access and licensing | **DOCUMENTATION AVAILABLE, ACCESS NOT VERIFIED** | Team C PR #6 |
| Private yoxi quote/dispatch/payment | **REQUIRES EXTERNAL AUTHORIZATION** | Official consumer features do not imply partner API |
| KPI changes / user value / user research | **NOT MEASURED** | Requires approved opt-in study |
| Registration, upload constraints, final submission receipt | **OWNER-ONLY; NOT VERIFIED** | Team C published contest source + portal check |

## 9. Reproducibility, sources and final handoff

**Reproduce the only claimed test** (source file from this PR after checking exact commit):

~~~sh
node research/notification_gate_reference.js
# Expected summary: Synthetic deterministic policy: 22/22 passed;
# Jev/LLM/external data NOT tested.
~~~

**Source dates:** All linked public material reviewed 2026-10-10 where accessible. Team C research was independently assembled 2026-10-09 and is cross-referenced, not falsely claimed as my own API invocation. The TypeSafe primary docs and vendor material are not a substitute for an independently validated service agreement.

**Primary + independent sources:**
- TypeSafe AI, official Jev model introduction: https://docs.typesafe.ai/introduction
- TypeSafe AI, Jev 1.13 failure modes (reviewed 2026-10-02): https://docs.typesafe.ai/model-jaggedness/jev-1.13
- TypeSafe AI, founder announcement and vendor claims/qualification: https://typesafe.ai/blog/introducing-system-one-models-and-jev
- Deußer, Sparrenberg, Sifa (2026), independent Jev benchmarking study: https://arxiv.org/abs/2609.37647
- Team C PR #6, source/permission/competition gates: https://github.com/jamshih/-/pull/6 ; evidence pinned to `b7aca6c7d9ac843485b3580869ff836761054d9d`
- Team B PR #7, synthetic-only demo caveat: https://github.com/jamshih/-/pull/7
- Official integration/cost/policy endpoints listed in §5; no keys or live result logs.

**Consumers:** Team A Issue #2, Team M Issue #1, Team E Issue #8; copy slide/voiceover from §1, use safeguards/fixture table in appendix, never present claimed model lift or fake bookings. **Remaining dependencies:** A to select final slide layout; E to match exact voiceover; M/human to verify portal/consent/brand and final submission; partner authorizations and genuine user study for any post-hackathon production gate.

**Release advice:** Use deterministic rule gate + simulated context cards as credible prelim proof, refer to Jev as a *possible measurable extension*, and prioritize readable evidence/provenance over a vendor benchmark slide. Do not place Jev vendor speedup or a claimed “smart notification accuracy” in the pitch.
