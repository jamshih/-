# Team B · 「隨行」四幕概念原型（初賽）
**Status:** R0 clickable concept / [模擬]. **Owner:** Team B · [Issue #3](https://github.com/jamshih/-/issues/3). **Not an official yoxi app.**

The four scenes demonstrate the frozen idea: **「通知本身，就是對話的第一句。」** Unlike a ride-only experience, the assistant presents transit as a viable recommendation and only navigates toward **explicit user-confirmed** booking; it never autonomously dispatches a vehicle.

## View it
Open `prototype/index.html` in a modern browser (works locally without a backend or network). Alternative:
```sh
cd prototype
python3 -m http.server 8000
# open http://127.0.0.1:8000/
```
Click the left numbered state controls or use the sample hash deep links `#state-1` through `#state-4`. Arrow keys change scenes outside the dialog. Buttons within the phone act as demonstration transitions: home → reminder; reminder → *same conversation*; comparison → rain replanning; replan → confirmation dialog. The `直接叫車` shortcut opens a **mock explanation**, deliberately NOT a real booking form. For the last scene, click `查看叫車確認`, then `我確認（模擬，無派車）` to see the **no-dispatch** result.

## Slides-ready assets
The four original, editable **430 × 900 SVG vector storyboard frames** are in `prototype/screens/`:
- `01-home.svg`: home, one-tap ride fallback and reminder.
- `02-alert.svg`: user-opted-in, synthetic 18:30 高雄巨蛋（捷運巨蛋站） reminder.
- `03-chat.svg`: notification becomes first chat message; MRT and yoxi comparison.
- `04-replan.svg`: 「我不想淋雨」 update, optional MRT, explicit confirmation entry.

**Important distinction:** these SVGs are *slide illustrations of the product concept*, NOT pixel-accurate screenshots taken from the browser. They can be dropped straight into the slide deck as vector images with a visible **「模擬畫面」** caption. PNG exports of the actual HTML render are supported via `capture_screens.py` (below) and should be visually checked by a reviewer before slide integration. No such browser-capture QA is asserted here without actual execution.

### Capture real PNGs from the HTML and smoke-test it (optional)
Requires local Python 3 and Playwright with an installed Chromium browser:
```sh
python3 -m pip install playwright
python3 -m playwright install chromium
python3 prototype/capture_screens.py
```
The script visits all four hash states, checks one visible scene per state and the last confirmation dialog, and writes `prototype/screenshots/01-home.png`, etc. It does **not** call any service or claim API integration. If the optional browser dependency is absent, use the SVG frames or the browser's screenshot inspector. Do not state smoke tests passed unless they were run.

## Narration
[30–60-second walkthrough and two extra scenario storyboards](STORYBOARD.md) are ready for A's pitch use.

## Interaction / accessibility
- Proper HTML buttons, discernible labels, keyboard-operated step navigation, focus outlines and live state announcements.
- `prefers-reduced-motion: reduce` disables transitions/animations. Decorative orb is static. No Rive needed for submission.
- High-stakes booking uses a visible `[模擬]` confirmation dialog. Keyboard `Escape` closes it.
- **Accessibility QA limitations:** no external assistive-technology audit or user tests performed. Dialog focus-trapping, different screen readers, 200% zoom, contrast and cross-browser layout **NOT VERIFIED**; treat the concept as prototype, not a production-accessibility claim.

## Safety / truthfulness / source-of-truth
- All displayed times (including 18:02), prices (MRT NT$35; yoxi NT$240), 28/17-minute travel durations, rain, permissions, places of origin, notification receipt and booking outcomes are explicitly **[模擬] fictional**. The only fixed geographic correction is **巨蛋站**, NOT 凹子底. No real-time location, weather, transport, dispatch, calendar, price estimate, or payments.
- No data leaves the browser. No APIs, credentials, trackers, app permissions, push delivery or database.
- No AI model, route inference, Jev classifier, user data, live consent system, or experiment is implemented. All content and choices are scripted. Performance, conversion and real-world usefulness **NOT MEASURED**.
- No official mascot, logo vector, copyrighted visual asset, or Rive file is included. `隨行` wordmark text and neutral decorative shape are original proposal mock elements, not authorized yoxi brand assets. Team C [Issue #4](https://github.com/jamshih/-/issues/4) found logo motif only; official mascot/asset-rights remain **UNVERIFIED**.
- Original inputs: [product brief](../docs/PRODUCT_BRIEF.md), [architecture](../docs/ARCHITECTURE.md), [competition assumptions](../docs/COMPETITION_RULES.md), [Team B brief](https://github.com/jamshih/-/issues/3).

## Handoff and remaining integration
- **Team A #2:** use four SVG storyboard screens as optional pitch visuals now; captions must say [模擬畫面]. PNGs may replace them after browser QA.
- **Team C #4:** confirm rights before anyone introduces official visuals; no action needed for neutral R0.
- **Team D #5:** keep Jev / learned notification efficacy experimental and unverified.
- **Team M #1:** confirm whether deck needs any interface captions adjusted; prior user decisions remain frozen.
- Prototype does **not** satisfy any final-round full-demo/backend criteria by itself. No automatic merge, publication, registration or submission is implied.
