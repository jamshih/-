# Team B · 45-second demo narration / storyboard
**Cinematic order:** state 1 → 2 → 3 → 4; Chinese speaker copy below. All transport numbers, rain, time, booking outcomes and notification conditions are fictional **[模擬]**. Duration is a **suggested narration target**, not a recorded video.

| Suggested timing | Screen | Narration (Chinese) | Tap / interaction |
|---|---|---|---|
| 00–09 s | **01 對話式首頁** | 「不是只有要叫車才打開 yoxi。使用者可以直接叫車，也可以先問今天怎麼走；不授權行事曆也能手動使用。」 | Point out `直接叫車`, then select `今晚行程`. |
| 09–20 s | **02 已同意的情境提醒** | 「使用者選擇同意通知後，系統在模擬的出發情境下，提醒 18:30 要到高雄巨蛋，也就是捷運巨蛋站。」 | Tap `點開通知`. |
| 20–32 s | **03 同一段對話 + 路線卡** | 「重點是通知不是一則消失的推播，而是同一段對話的第一句。捷運與叫車公平比較；比較數字全是模擬。」 | Highlight notification bubble and non-ride MRT card. |
| 32–45 s | **04 我不想淋雨 → 明確確認** | 「使用者說『我不想淋雨』後，卡片依偏好重新排序；即使推薦 yoxi，也要使用者自己進入確認，絕不自動派車。」 | Tap `查看叫車確認`, then `我確認（模擬，無派車）` to demonstrate that no real booking occurs. |

## Presentation slide caption (copy/paste)
> **流程示意／模擬畫面：** 使用者自主同意情境提醒 → 高雄巨蛋 18:30 出發提醒 → 通知直接成為原對話訊息 → 捷運與 yoxi 中立比較 → 「我不想淋雨」改變偏好 → 需用戶明確確認才進入正式叫車流程。所示雨況、時間與價格皆為模擬，尚無實際 API 或派車功能。

## Additional *storyboard-only* variants (not extra implemented screens)
**Scenario 2 — disruption:** A previously consented user is about to transfer. A reliable, hypothetical source flags a significant delay; dedup/cooldown/silent-hour rules filter nuisance alerts. A single **[模擬]** interruption enters that user's existing chat as the first update. Cards show a transit reroute, a taxi alternative and snooze/dismiss. Do not imply access to official transit reliability feeds. **No separate implemented demo is claimed.**

**Scenario 3 — no-ride study:** User types「我還有兩個小時，想找安靜的地方讀書」. Proposed response gives quiet study-space suggestions and access routes, explicitly prioritizing a viable non-taxi option. Exact study places, occupancy, opening hours and travel times require trustworthy external sources in a future implementation. **This is storyboard-only, not a tested feature.**

## QA checklist (to be completed by the reviewer, not pre-checked)
- [ ] Open every `#state-1`…`#state-4` route in Chromium.
- [ ] Compare each HTML state against its corresponding SVG; note that vectors are illustrative, not screenshots.
- [ ] Verify `直接叫車` triggers explanatory mock dialog, not a service call.
- [ ] Verify 18:30 destination names are **高雄巨蛋／捷運巨蛋站**, not 凹子底.
- [ ] Click notification and inspect the first assistant bubble in the **same** chat.
- [ ] Trigger 「我不想淋雨」 and inspect card order and user-confirmation dialog.
- [ ] Verify all fare/ETA/data values say `[模擬]` and no actual booking claim.
- [ ] Test keyboard focus, Escape and reduced motion; record any defects.
- [ ] Export four browser PNGs if slides prefer them; retain `[模擬畫面]` labels.

**Source ownership:** Team B `prototype/`. Decisions about real platform APIs, brand licensing, official contest portal, prototype publication and deck wording are deferred to C/M/A respectively.
