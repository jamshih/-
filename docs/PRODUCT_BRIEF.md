# Frozen product brief — yoxi 隨行 / Product thesis

**Team:** 出門再說  
**Topic:** 「不搭車，也打開 yoxi —— 打造高頻互動的 AI 出行夥伴」  
**Product / service (working name):** yoxi 隨行  
**Tagline:** 主動懂你下一步的 AI 出行夥伴

## Problem and opportunity
Today ride-hailing is opened mostly *after* the rider decides to book. We want yoxi to help **before** the mode decision: where to go, when to leave, and how to travel. High-frequency utility must include days when the recommendation is *not to book*.

## Frozen unique UX
**「通知本身，就是對話的第一句。」** Context-aware notifications open the **same conversation** with the original notification message and structured evidence. The default homepage is a conversational interface with context prompts and tappable generated **cards**. High-stakes ride selection, map, pickup/dropoff, fare and booking **retain explicit user confirmation and familiar native controls**. No autonomous booking.

### Core pipeline
Opt-in context (calendar, location, weather, traffic, saved habits) → deterministic rules + safety/cooldown → experimental Jev notification gate (if validated) / transparent fallback → LLM intent and response orchestration → authoritative data tools → dynamic route/ride cards → optional Rive character reflecting app state.

### Three locked demo scenarios
1. **Leave on time (weather + calendar):** At 18:30 the user needs to reach **高雄巨蛋／高雄捷運巨蛋站** (not 凹子底). A rain/travel-delay alert is shown as a chat entry. User says **「我不想淋雨」**; compare a transit option with a yoxi option and explicit booking confirmation. All sample ETAs/prices must be labeled simulated unless sourced.
2. **Disruption / replanning:** Delayed transit or significant traffic change triggers a single valuable alert, with route alternative, yoxi option and dismiss/snooze.
3. **No ride intent:** User has two hours to study outside. Suggest suitable quiet places and transport, **including recommendations that do not book yoxi**.

## Target user & experience constraints
Initial persona: urban student / commuter with calendar commitments and mixed transit + taxi trips. We should not claim validated TAM or behavior without citations. Home should allow `直接叫車`, `回家` and suggestions without typing. Chat supplements fast actions; it must not slow familiar ride booking.

## Business hypothesis (NOT measured results)
- Leading: weekly engaged days, non-booking opens, value-bearing notification open rate, suggestions acted upon, opt-out rate.
- Lagging: monthly trips per active user, AI-assisted booking conversion, repeat use and satisfaction.
- Avoid optimizing just push-open rate or forced taxi upsell; protect trust via sparse notifications and neutral mode recommendations.
- Quantified improvement claims must be **hypotheses or goals** with baseline and experiment plan, never presented as measured.

## Brand / mascot
Use existing official yoxi mascot if one is confirmed and licensing allows. Otherwise propose a subtle **Rive-driven Dynamic AI Persona**: idle, thinking, rain, rerouting, success, car-arriving. Quiet during price/booking/payment. No new mascot necessary for initial submission; research brand usage first.

## Explicit non-goals
No separate new taxi app; no replacing existing yoxi backend or dispatch; no unsanctioned real booking; no hallucinated real-time facts; no permission scraping; no 'global-first' novelty claim; no untested autonomous notification model.

## Product constraints
- Location/calendar/notifications: progressive granular permission, can operate manually without them, quiet hours and cooldown.
- Weather/traffic/ETA/fare: server-sourced with freshness/attribution; no LLM calculations or guesses.
- Jev: candidate for bounded evaluation **only after independent benchmark** against deterministic baseline and human-labeled fixtures.
- Rive: expressive state binding, decorative only, accessible reduced-motion option.
