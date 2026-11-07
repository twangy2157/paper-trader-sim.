# Paper trader summary

SIMULATION ONLY. No real trades.

Updated 2026-11-07T12:54:21Z. Bankroll cash (research-selected trades): 605.1869477321155. Open positions: 14. Pools on watchlist: 43.

| group | n | win | avg | CI | P&L $ |
|---|---|---|---|---|---|
| research-picked | 12 | 25% | -32.7% | -67 to 6 | -395 |
| momentum, not picked | 987 | 13% | -61.1% | -65 to -57 | -60377 |
| all momentum | 999 | 13% | -60.7% | -64 to -57 | -60771 |
| control | 1262 | 6% | -20.1% | -22 to -18 | -25444 |
| dip buy | 10 | 10% | -40.3% | -73 to -7 | -404 |
| proven pools | 51 | 47% | -16.7% | -30 to -3 | -857 |

What-if exit rules on the SAME trades. Cells: avg return (trades, win rate).

| exit rule | momentum | control | dip | proven |
|---|---|---|---|---|
| base_sl30_tp100 | -61% (978, 13%) | -20% (1262, 6%) | -40% (10, 10%) | -17% (51, 47%) |
| wide_sl50_tp100 | -61% (978, 15%) | -21% (1262, 7%) | -43% (10, 10%) | -17% (51, 47%) |
| sl30_tp50 | -62% (978, 16%) | -20% (1262, 7%) | -44% (10, 10%) | -19% (51, 47%) |
| sl50_tp50 | -62% (978, 18%) | -21% (1262, 7%) | -47% (10, 10%) | -19% (51, 47%) |
| no_stop_tp100 | -61% (978, 16%) | -21% (1262, 7%) | -40% (10, 10%) | -17% (51, 47%) |

Verdict: NOT ENOUGH DATA (need 30+ closed filter=1 trades and a CI above zero before believing anything).

Pools seen: 34918. Outcomes:

- missed_window: 22591
- low_liquidity: 6321
- proven_liquidity_gone: 2722
- no_momentum: 1312
- research_failed: 994
- simulated failed buy: 434
- proven_low_volume: 388
- proven_price_collapsed_or_parabolic: 58
- proven: 52
- proven_no_uptrend: 24
- research_passed: 12
- dip: 10

Warning: 271 judged pools had an unreadable mint/freeze value. Check mint_raw / freeze_raw in candidates.csv; the parsing may need fixing.
