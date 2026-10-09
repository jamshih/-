# Technical feasibility & reference architecture (preliminary proposal)

> Architecture concept, not a claim of implemented or licensed API access.

```text
Consent & user settings
        ↓
Calendar / location / weather / traffic / travel preferences
        ↓
Context normalization + freshness / uncertainty checks
        ↓
Deterministic push gate: permission, opt-out, quiet hours, dedup, cooldown
        ↓
Candidate 'interrupt now?' scoring:
  A. deterministic baseline (mandatory fallback)
  B. Jev bounded classification (experiment; must be validated)
        ↓
Notification with evidence + trace ID → same conversation on open
        ↓
LLM: parse intent / request tools / compose language
        ↓
Trusted tools: route, transit, maps, POI, weather, official yoxi ETA/fare/booking
        ↓
Validated action schema → dynamic cards / map / quick replies
        ↓
Explicit confirmation for ride request and payment
        ↓
Rive state machine (optional, nonblocking)
```

## Hard boundaries
- LLM **never fabricates ETA, rainfall, fares, route disruptions, or confirmed bookings**.
- Demo uses **clearly labeled mocked** route/forecast/price/booking status unless access to real APIs is verified.
- Jev is **not** authoritative merely because it emits probabilities; may be unavailable, too costly, poorly calibrated, or mismatched. Compare against human-reviewed fixtures for precision (valuable alerts), nuisance rate, false negatives (missed urgent changes), latency, and cost. Do not claim calibration without measurement.
- Use hard deny rules for unsubscribed user, sensitive data, duplicate event, privacy limits, rate limit, stale data.
- Any action (book, pay, message) requires permission and a user confirm action.
- Data retention minima, user controls, quiet hours, and push policy must be in the deck.
- Secure tool calls and protect secrets in backend; prototype not authorized to access production yoxi APIs.
- Rive persona is a supplementary visual state layer; include reduced-motion and do not block task completion.

## Thin proof-of-concept contract
4 screen states: (1) chat home + contextual chips, (2) contextual push with route impact, (3) resumed conversation + verifiable travel options, (4) user changes constraint '我不想淋雨' → updated cards → mock confirmation screen.
Optional screens only if slides are already on track.

## Evaluation fixtures
At least 8 synthetic scenarios: on-time sunny trip, rain before class, route delay, stale weather, quiet hours, event canceled, notification duplicate, no-ride study place. Each has deterministic truth / appropriate action expected and reason. Share schemas and result screenshots with slide owner.

## Potential implementation
Clickable Figma/HTML/SwiftUI demo based on team bandwidth; NO need for real API integrations in prelim. Dynamic cards can be represented by safe structured JSON with design renderer. Rive mascot as optional video or interactive embed; never spend critical-path days inventing mascot brand identity.

## Claims register
Whenever a tool, model, competitor capability, license, brand asset or data feed is named, attach source URL + checked date + limits. Keep **verified / proposed / simulated** labels distinct.
