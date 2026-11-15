#!/usr/bin/env python3
"""Screenshot entry/index.html -> ad.png at 1280x800, light, 1x."""
import asyncio
from pathlib import Path
from playwright.async_api import async_playwright

REPO = Path.home() / "makefun-bounty" / "entry"
SRC = REPO / "index.html"
OUT = REPO / "ad.png"


async def main():
    async with async_playwright() as p:
        browser = await p.chromium.launch()
        page = await browser.new_page(
            viewport={"width": 1280, "height": 800},
            device_scale_factor=1,
            color_scheme="light",
        )
        await page.goto(SRC.as_uri(), wait_until="networkidle")
        await page.wait_for_timeout(900)

        # verify hero + code + CTA all above 800px
        chk = await page.evaluate("""() => {
            const out = {};
            const h1 = document.querySelector('h1');
            out.h1 = h1 ? h1.getBoundingClientRect().bottom : null;
            const btn = document.querySelector('.cta, .btn, a[href*="9vxtw8ty"]');
            const btns = [...document.querySelectorAll('a[href*="9vxtw8ty"]')];
            out.cta_top = btns.length ? btns[0].getBoundingClientRect().bottom : null;
            const code = [...document.querySelectorAll('*')]
                .find(e => e.children.length === 0 && (e.textContent || '').trim() === '9vxtw8ty');
            out.code = code ? code.getBoundingClientRect().bottom : null;
            out.scrollH = document.documentElement.scrollHeight;
            return out;
        }""")
        print("layout check:", chk)

        await page.screenshot(path=str(OUT), type="png", animations="disabled")
        await browser.close()

    size = OUT.stat().st_size
    print(f"ad.png: {size:,} bytes ({size/1024:.1f} KB)")
    assert size < 2_000_000, "terlalu besar"


asyncio.run(main())
