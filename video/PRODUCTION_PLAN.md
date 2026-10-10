# Video production plan — 3-minute preliminary submission (V0)

**Parent issue:** [Team E #8](https://github.com/jamshih/-/issues/8) · **Read-aloud script:** [VIDEO_SCRIPT_V0.md](VIDEO_SCRIPT_V0.md)  
**Status:** Script/shot plan ready for human recording; no actual video, captions, audio or submission have been produced yet.

## 7-scene edit decision list

| Target | Visual / what viewer sees | Voiceover source | Assets and on-screen text |
| --- | --- | --- | --- |
| **0:00–0:22** | Logo-neutral title against simple transit-map lines; 3 questions appear one at a time | Script §開場 | 「為什麼只有要搭車才開 yoxi？」／「等等去哪？／幾點出門？／怎麼去？」 |
| **0:22–0:44** | Concept product title + four-screen interactive home zoom/crop | Script §一句話解法 | [B screen 01 home](https://github.com/jamshih/-/blob/9a882e9c2ee82f11135c5587e90a1b21fa27233f/prototype/screens/01-home.svg), `出門再說｜yoxi 隨行`; subtitle `以對話為入口，而不是重做一個叫車 App` |
| **0:44–1:16** | Calendar time and weather *hypothetical*, a push card enters screen, push taps into same conversation | Script §通知就是第一句 | [B screen 02 alert](https://github.com/jamshih/-/blob/9a882e9c2ee82f11135c5587e90a1b21fa27233f/prototype/screens/02-alert.svg) → [B screen 03 chat](https://github.com/jamshih/-/blob/9a882e9c2ee82f11135c5587e90a1b21fa27233f/prototype/screens/03-chat.svg). Overlay `通知，就是對話的第一句` and `[模擬情境]` |
| **1:16–1:47** | On screen type '我不想淋雨'; alternate transport cards, highlight explicit taxi confirmation and 巨蛋站 | Script §不同運具 | [B screen 04 replan](https://github.com/jamshih/-/blob/9a882e9c2ee82f11135c5587e90a1b21fa27233f/prototype/screens/04-replan.svg). Fixed lower third `畫面/路線/價格均為模擬；未連接真實叫車` |
| **1:47–2:11** | Split pictograms: transit disruption, study location. Icons/text only; don't make more app screens | Script §高頻價值 | `路線異常 → 可重新規劃`; `今天不搭車 → 也能問去哪`. If using place images, only original/rights-cleared assets |
| **2:11–2:42** | Simple clean architecture diagram, gates light up sequentially; optional tiny Rive mascot as conceptual thumbnail *only if legally safe and already ready* | Script §可信資料 | `使用者授權→硬性通知規則→待評估 Jev→LLM 理解→可信交通資料→可操作卡片`; label `[提案架構，非正式串接]` |
| **2:42–3:00** | 4 KPIs on one screen and closing call; short CTA | Script §結語 | `非叫車開啟` / `每週使用天數` / `通知關閉率` / `AI→搭乘轉換`; then `在你決定怎麼出門前，yoxi 就幫得上忙。` |

## Asset availability / handoffs (what is real)
- **B assets ARE committed:** [Prototype draft PR #7](https://github.com/jamshih/-/pull/7) pinned head `9a882e9c2ee82f11135c5587e90a1b21fa27233f`; four **vector SVG storyboard images**, not claimed actual browser captures. B's HTML is interactive but browser QA/PNG exporter not yet run. Use these now.
- **C research source:** [Research PR #6](https://github.com/jamshih/-/pull/6) last verified head `b7aca6c7d9ac843485b3580869ff836761054d9d`; primary campus briefing on video spec linked in #4. No verified official mascot rights.
- **D architecture:** Agent not yet evidenced as claimed in #5 at time of V0; script intentionally presents Jev as experimental candidate and no performance claims.
- **A deck:** no A-created draft found at time of V0; video can be produced from these seven scenes without a deck.

## How a human can make the video TODAY
1. Open four SVG frames from B's immutable links and build a **16:9 canvas** (suggested 1920×1080 or 1280×720; verify competition video format if specified). Prefer Canva, CapCut, Keynote, or PowerPoint depending on familiarity. Never depend on inaccessible editing software.
2. Create seven simple scenes from table. Reuse SVG crop-with-padding for 0:22–1:47; no extra animations needed. Use original line icons/shapes for other scenes. Keep [模擬] caption visible over demo screens.
3. Record a **single Chinese voiceover take** from script, preferably with phone microphone or laptop headset in a quiet room; edit pauses. Measure total runtime. Current 3:00 timings are editing targets, NOT measured read speed.
4. Align scenes to narration, generate/edit Chinese captions for accuracy (proper nouns **yoxi、巨蛋站、Jev、Rive**); use music only if licensed, preferably none.
5. Play full video: comprehensible without screenshots, audible voice, no unsupported claims, sources on last frame or pinned deck appendix. Check duration and text legibility at phone size.
6. Upload to YouTube as **「不公開」 (Unlisted)**, **not 「私人」 (Private)**. Required title pattern from campus briefing: `出題企業_作品名稱_2026 和泰 AI 黑客松`; suggested title `yoxi_yoxi隨行_2026 和泰 AI 黑客松` is **provisional** until checked against official form's enterprise display name.
7. Open the YouTube link in a private/incognito window to verify it plays without login, then paste URL into the registered team-leader's **official submission record** with deck, before organizer deadline. Preserve screenshot of final confirmation. Only human owner can attest upload/submission.

## Visual/copy guardrails
- **Do not** imply mock weather/route/fare are real data; speak conditionally and mark simulated screens.
- **Do not** claim installed Google Routes/TDX/CWA/yoxi fare API, live dispatch, a calibrated Jev model, Rive official character, or evidence of higher conversion.
- Do not depict official logos/mascots via unlicensed tracing/derivatives. Plain typed names may still be subject to event brand rules; Team C/owner checks.
- Include quiet hours/permissions as visible concepts; avoid promising unsupported background access.
- If A's finished slide deck arrives, **replace still scenes with deck visuals** but keep the spoken argument. Video creation must not wait.
- Stop visual polishing if video runtime, audio quality, factual accuracy or portal submission is at risk.

## Acceptance / QA log to complete
- [ ] Script read-aloud timed (actual __ min __ sec; speaker __; date __)
- [ ] Recorded/editable video produced (path/URL __)
- [ ] All four B concept frames proofed or replaced; simulated data marked
- [ ] Audio audibility + Chinese captions proofread
- [ ] Branding/use rights & source claims reviewed by C/M
- [ ] YouTube '不公開' URL verified playable via fresh session
- [ ] Final deck + video URL entered, portal receipt screenshot recorded by human owner
