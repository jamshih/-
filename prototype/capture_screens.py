#!/usr/bin/env python3
"""Local optional screenshot export + minimal browser smoke test. No network/backends."""
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parent
CASES = [
    (1, "01-home.png"),
    (2, "02-alert.png"),
    (3, "03-chat.png"),
    (4, "04-replan.png"),
]


def main() -> int:
    try:
        from playwright.sync_api import sync_playwright
    except ImportError:
        print("Missing Playwright. Install with: python3 -m pip install playwright", file=sys.stderr)
        return 2
    out = ROOT / "screenshots"
    out.mkdir(exist_ok=True)
    uri = (ROOT / "index.html").as_uri()
    with sync_playwright() as p:
        try:
            browser = p.chromium.launch(headless=True)
        except Exception as e:
            print("Chromium unavailable. Try python3 -m playwright install chromium", file=sys.stderr)
            print(repr(e), file=sys.stderr)
            return 2
        page = browser.new_page(viewport={"width": 1366, "height": 1100}, device_scale_factor=2,
                                reduced_motion="reduce", locale="zh-TW")
        for n, filename in CASES:
            page.goto(f"{uri}#state-{n}", wait_until="load")
            visible = page.locator(".screen.active")
            assert visible.count() == 1, f"Expected exactly one active scene for {n}"
            assert visible.get_attribute("data-state") == str(n)
            assert page.locator(".step[aria-current='step']").get_attribute("data-go") == str(n)
            page.locator(".mock-device").screenshot(path=str(out / filename))
            print("CAPTURED", out / filename)
        # Verifies the fourth state explicitly asks for confirmation and never claims live booking.
        page.get_by_role("button", name="查看叫車確認").click()
        assert page.locator("#dialog-layer").get_attribute("class").find("open") >= 0
        assert "派遣車輛" in page.locator("#dialog-note").inner_text()
        page.get_by_role("button", name="我確認（模擬，無派車）").click()
        assert "沒有送出任何叫車請求" in page.locator("#dialog-text").inner_text()
        page.keyboard.press("Escape")
        assert "open" not in page.locator("#dialog-layer").get_attribute("class")
        # The same code path also checks direct ride fallback from the home state.
        page.goto(f"{uri}#state-1", wait_until="load")
        page.get_by_role("button", name="直接叫車").first.click()
        assert "沒有派車能力" in page.locator("#dialog-text").inner_text()
        browser.close()
    print("PASS: 4 states, simulated explicit booking path, direct-booking fallback.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
