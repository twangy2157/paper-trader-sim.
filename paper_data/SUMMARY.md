# Paper trader summary

SIMULATION ONLY. No real trades.

Updated 2026-11-03T18:02:09Z. Bankroll cash (research-selected trades): 860.0946161788225. Open positions: 17. Pools on watchlist: 54.

| group | n | win | avg | CI | P&L $ |
|---|---|---|---|---|---|
| research-picked | 2 | 0% | -69.5% | - | -140 |
| momentum, not picked | 345 | 14% | -53.8% | -61 to -47 | -18583 |
| all momentum | 347 | 14% | -53.9% | -61 to -47 | -18722 |
| control | 384 | 8% | -16.1% | -20 to -13 | -6233 |
| dip buy | 3 | 33% | 12.5% | - | 37 |
| proven pools | 15 | 33% | -36.8% | -64 to -10 | -553 |

What-if exit rules on the SAME trades. Cells: avg return (trades, win rate).

| exit rule | momentum | control | dip | proven |
|---|---|---|---|---|
| base_sl30_tp100 | -55% (326, 15%) | -16% (384, 8%) | 12% (3, 33%) | -37% (15, 33%) |
| wide_sl50_tp100 | -55% (326, 17%) | -16% (384, 9%) | 12% (3, 33%) | -37% (15, 33%) |
| sl30_tp50 | -56% (326, 19%) | -17% (384, 9%) | 1% (3, 33%) | -37% (15, 33%) |
| sl50_tp50 | -55% (326, 22%) | -17% (384, 9%) | 1% (3, 33%) | -37% (15, 33%) |
| no_stop_tp100 | -55% (326, 17%) | -17% (384, 9%) | 12% (3, 33%) | -37% (15, 33%) |

Verdict: NOT ENOUGH DATA (need 30+ closed filter=1 trades and a CI above zero before believing anything).

Pools seen: 12577. Outcomes:

- missed_window: 8332
- low_liquidity: 2525
- proven_liquidity_gone: 650
- no_momentum: 435
- research_failed: 354
- simulated failed buy: 129
- proven_low_volume: 105
- proven_price_collapsed_or_parabolic: 17
- proven: 16
- proven_no_uptrend: 9
- dip: 3
- research_passed: 2

Warning: 84 judged pools had an unreadable mint/freeze value. Check mint_raw / freeze_raw in candidates.csv; the parsing may need fixing.
