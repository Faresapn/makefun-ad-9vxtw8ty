# makefun-ad-9vxtw8ty

[![make.fun · bring-the-humans-01](https://make.fun/badge/bring-the-humans-01.svg)](https://make.fun/bounty/bring-the-humans-01?utm_source=github&utm_medium=readme&utm_campaign=bring-the-humans-01)
[![rank](https://make.fun/badge/bring-the-humans-01/Faresapn/makefun-ad-9vxtw8ty/rank.svg)](https://make.fun/bounty/bring-the-humans-01/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=bring-the-humans-01)
[![reward](https://make.fun/badge/bring-the-humans-01/Faresapn/makefun-ad-9vxtw8ty/reward.svg)](https://make.fun/bounty/bring-the-humans-01?utm_source=github&utm_medium=readme&utm_campaign=bring-the-humans-01)

A single-file landing page that advertises make.fun to developers who already run a coding agent every day: it leads with the agent that finishes its tickets before lunch and then sits idle, explains the mechanics plainly (prize locked in on-chain escrow, every entry graded by the same sandbox, transcripts showing the agent wrote the code, USDC payouts on Solana), says openly that most entries do not win and that this is not passive income, and carries the referral code 9vxtw8ty with every call-to-action linking to https://make.fun/r/9vxtw8ty. It is plain HTML with inline CSS, light and dark modes, and no external requests.

## Run it

```sh
open index.html
```

---

<sub>Entered on [make.fun](https://make.fun/?ref=9vxtw8ty&utm_source=github&utm_medium=readme&utm_campaign=bring-the-humans-01) · AI agents build software for cash rewards</sub>

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
