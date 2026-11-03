# Paper trader summary

SIMULATION ONLY. No real trades.

Updated 2026-11-03T18:24:00Z. Bankroll cash (research-selected trades): 860.0946161788225. Open positions: 18. Pools on watchlist: 72.

| group | n | win | avg | CI | P&L $ |
|---|---|---|---|---|---|
| research-picked | 2 | 0% | -69.5% | - | -140 |
| momentum, not picked | 349 | 15% | -53.8% | -61 to -47 | -18819 |
| all momentum | 351 | 15% | -53.9% | -61 to -47 | -18959 |
| control | 387 | 8% | -16.3% | -20 to -13 | -6355 |
| dip buy | 3 | 33% | 12.5% | - | 37 |
| proven pools | 15 | 33% | -36.8% | -64 to -10 | -553 |

What-if exit rules on the SAME trades. Cells: avg return (trades, win rate).

| exit rule | momentum | control | dip | proven |
|---|---|---|---|---|
| base_sl30_tp100 | -55% (330, 15%) | -16% (387, 8%) | 12% (3, 33%) | -37% (15, 33%) |
| wide_sl50_tp100 | -55% (330, 17%) | -17% (387, 9%) | 12% (3, 33%) | -37% (15, 33%) |
| sl30_tp50 | -56% (330, 19%) | -17% (387, 9%) | 1% (3, 33%) | -37% (15, 33%) |
| sl50_tp50 | -56% (330, 22%) | -17% (387, 9%) | 1% (3, 33%) | -37% (15, 33%) |
| no_stop_tp100 | -55% (330, 18%) | -17% (387, 9%) | 12% (3, 33%) | -37% (15, 33%) |

Verdict: NOT ENOUGH DATA (need 30+ closed filter=1 trades and a CI above zero before believing anything).

Pools seen: 12700. Outcomes:

- missed_window: 8424
- low_liquidity: 2537
- proven_liquidity_gone: 658
- no_momentum: 440
- research_failed: 357
- simulated failed buy: 130
- proven_low_volume: 107
- proven_price_collapsed_or_parabolic: 17
- proven: 16
- proven_no_uptrend: 9
- dip: 3
- research_passed: 2

Warning: 84 judged pools had an unreadable mint/freeze value. Check mint_raw / freeze_raw in candidates.csv; the parsing may need fixing.
