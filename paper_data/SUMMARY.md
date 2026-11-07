# Paper trader summary

SIMULATION ONLY. No real trades.

Updated 2026-11-07T12:10:09Z. Bankroll cash (research-selected trades): 605.1869477321155. Open positions: 20. Pools on watchlist: 42.

| group | n | win | avg | CI | P&L $ |
|---|---|---|---|---|---|
| research-picked | 12 | 25% | -32.7% | -67 to 6 | -395 |
| momentum, not picked | 979 | 13% | -60.9% | -65 to -57 | -59763 |
| all momentum | 991 | 13% | -60.6% | -64 to -57 | -60157 |
| control | 1259 | 6% | -20.1% | -22 to -18 | -25418 |
| dip buy | 10 | 10% | -40.3% | -73 to -7 | -404 |
| proven pools | 51 | 47% | -16.7% | -30 to -3 | -857 |

What-if exit rules on the SAME trades. Cells: avg return (trades, win rate).

| exit rule | momentum | control | dip | proven |
|---|---|---|---|---|
| base_sl30_tp100 | -61% (970, 13%) | -20% (1259, 6%) | -40% (10, 10%) | -17% (51, 47%) |
| wide_sl50_tp100 | -61% (970, 15%) | -21% (1259, 7%) | -43% (10, 10%) | -17% (51, 47%) |
| sl30_tp50 | -62% (970, 16%) | -20% (1259, 7%) | -44% (10, 10%) | -19% (51, 47%) |
| sl50_tp50 | -62% (970, 18%) | -21% (1259, 7%) | -47% (10, 10%) | -19% (51, 47%) |
| no_stop_tp100 | -61% (970, 16%) | -21% (1259, 7%) | -40% (10, 10%) | -17% (51, 47%) |

Verdict: NOT ENOUGH DATA (need 30+ closed filter=1 trades and a CI above zero before believing anything).

Pools seen: 34797. Outcomes:

- missed_window: 22515
- low_liquidity: 6301
- proven_liquidity_gone: 2708
- no_momentum: 1312
- research_failed: 989
- simulated failed buy: 432
- proven_low_volume: 385
- proven_price_collapsed_or_parabolic: 58
- proven: 52
- proven_no_uptrend: 23
- research_passed: 12
- dip: 10

Warning: 270 judged pools had an unreadable mint/freeze value. Check mint_raw / freeze_raw in candidates.csv; the parsing may need fixing.
