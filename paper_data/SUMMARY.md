# Paper trader summary

SIMULATION ONLY. No real trades.

Updated 2026-11-04T20:45:10Z. Bankroll cash (research-selected trades): 816.8065461812329. Open positions: 16. Pools on watchlist: 73.

| group | n | win | avg | CI | P&L $ |
|---|---|---|---|---|---|
| research-picked | 5 | 20% | -36.3% | - | -183 |
| momentum, not picked | 528 | 16% | -53.0% | -58 to -47 | -28026 |
| all momentum | 533 | 16% | -52.8% | -58 to -47 | -28210 |
| control | 643 | 7% | -18.8% | -22 to -16 | -12172 |
| dip buy | 4 | 25% | -13.1% | - | -52 |
| proven pools | 29 | 41% | -18.2% | -37 to -1 | -530 |

What-if exit rules on the SAME trades. Cells: avg return (trades, win rate).

| exit rule | momentum | control | dip | proven |
|---|---|---|---|---|
| base_sl30_tp100 | -53% (512, 16%) | -19% (643, 7%) | -13% (4, 25%) | -18% (29, 41%) |
| wide_sl50_tp100 | -53% (512, 18%) | -19% (643, 8%) | -13% (4, 25%) | -18% (29, 41%) |
| sl30_tp50 | -55% (512, 20%) | -19% (643, 8%) | -22% (4, 25%) | -20% (29, 41%) |
| sl50_tp50 | -54% (512, 23%) | -19% (643, 9%) | -22% (4, 25%) | -20% (29, 41%) |
| no_stop_tp100 | -52% (512, 20%) | -20% (643, 8%) | -13% (4, 25%) | -18% (29, 41%) |

Verdict: NOT ENOUGH DATA (need 30+ closed filter=1 trades and a CI above zero before believing anything).

Pools seen: 19605. Outcomes:

- missed_window: 12964
- low_liquidity: 3625
- proven_liquidity_gone: 1282
- no_momentum: 694
- research_failed: 535
- simulated failed buy: 223
- proven_low_volume: 182
- proven_price_collapsed_or_parabolic: 40
- proven: 31
- proven_no_uptrend: 20
- research_passed: 5
- dip: 4

Warning: 150 judged pools had an unreadable mint/freeze value. Check mint_raw / freeze_raw in candidates.csv; the parsing may need fixing.
