# Paper trader summary

SIMULATION ONLY. No real trades.

Updated 2026-11-04T20:33:40Z. Bankroll cash (research-selected trades): 816.8065461812329. Open positions: 18. Pools on watchlist: 77.

| group | n | win | avg | CI | P&L $ |
|---|---|---|---|---|---|
| research-picked | 5 | 20% | -36.3% | - | -183 |
| momentum, not picked | 526 | 16% | -52.8% | -58 to -47 | -27826 |
| all momentum | 531 | 16% | -52.7% | -58 to -47 | -28009 |
| control | 640 | 7% | -18.9% | -22 to -16 | -12152 |
| dip buy | 4 | 25% | -13.1% | - | -52 |
| proven pools | 29 | 41% | -18.2% | -37 to -1 | -530 |

What-if exit rules on the SAME trades. Cells: avg return (trades, win rate).

| exit rule | momentum | control | dip | proven |
|---|---|---|---|---|
| base_sl30_tp100 | -53% (510, 16%) | -19% (640, 7%) | -13% (4, 25%) | -18% (29, 41%) |
| wide_sl50_tp100 | -53% (510, 18%) | -19% (640, 8%) | -13% (4, 25%) | -18% (29, 41%) |
| sl30_tp50 | -55% (510, 20%) | -19% (640, 8%) | -22% (4, 25%) | -20% (29, 41%) |
| sl50_tp50 | -54% (510, 23%) | -19% (640, 9%) | -22% (4, 25%) | -20% (29, 41%) |
| no_stop_tp100 | -52% (510, 20%) | -20% (640, 8%) | -13% (4, 25%) | -18% (29, 41%) |

Verdict: NOT ENOUGH DATA (need 30+ closed filter=1 trades and a CI above zero before believing anything).

Pools seen: 19542. Outcomes:

- missed_window: 12916
- low_liquidity: 3614
- proven_liquidity_gone: 1282
- no_momentum: 693
- research_failed: 533
- simulated failed buy: 222
- proven_low_volume: 182
- proven_price_collapsed_or_parabolic: 40
- proven: 31
- proven_no_uptrend: 20
- research_passed: 5
- dip: 4

Warning: 150 judged pools had an unreadable mint/freeze value. Check mint_raw / freeze_raw in candidates.csv; the parsing may need fixing.
