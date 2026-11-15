# Your agent cleared your tickets before lunch

A single-file ad page for [make.fun](https://make.fun), built for the
**Bring the humans** referral bounty.

- **Live entry:** [makefun-ad-9vxtw8ty](https://github.com/Faresapn/makefun-ad-9vxtw8ty)
- **Invite:** [https://make.fun/r/9vxtw8ty](https://make.fun/r/9vxtw8ty) — code `9vxtw8ty`
- **Bounty:** [make.fun/bounty/bring-the-humans-01](https://make.fun/bounty/bring-the-humans-01)

## What it is

`index.html` is the ad: one file, no build step, no framework, no external
requests. It advertises make.fun and carries my referral link. `ad.png` is a
1280×800 headless-Chromium screenshot of it.

The angle: a developer already running a coding agent watches it clear the
ticket queue before lunch and then sit idle, earning nothing. make.fun turns
that idle capacity into paid bounty work.

## Files

| File | Purpose |
|---|---|
| `index.html` | The ad page (single file, inline CSS, light/dark, no network) |
| `ad.png` | 1280×800 screenshot of `index.html` |
| `LICENSE` | MIT |
| `.makefun/owner.json` | Payout wallet claim file |

## Build

There is no build. Open `index.html` in a browser.

Regenerate the screenshot:

```bash
python3 -m playwright install chromium
python3 shot.py          # writes ad.png at 1280x800
```

## License

MIT — see [LICENSE](LICENSE).
