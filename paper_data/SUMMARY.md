# Paper trader summary

SIMULATION ONLY. No real trades.

Updated 2026-11-07T14:49:11Z. Bankroll cash (research-selected trades): 605.1869477321155. Open positions: 17. Pools on watchlist: 59.

| group | n | win | avg | CI | P&L $ |
|---|---|---|---|---|---|
| research-picked | 12 | 25% | -32.7% | -67 to 6 | -395 |
| momentum, not picked | 1002 | 13% | -61.1% | -65 to -57 | -61315 |
| all momentum | 1014 | 13% | -60.8% | -64 to -57 | -61710 |
| control | 1280 | 6% | -20.1% | -22 to -18 | -25786 |
| dip buy | 10 | 10% | -40.3% | -73 to -7 | -404 |
| proven pools | 52 | 48% | -15.9% | -30 to -3 | -832 |

What-if exit rules on the SAME trades. Cells: avg return (trades, win rate).

| exit rule | momentum | control | dip | proven |
|---|---|---|---|---|
| base_sl30_tp100 | -61% (993, 13%) | -20% (1280, 6%) | -40% (10, 10%) | -16% (52, 48%) |
| wide_sl50_tp100 | -61% (993, 15%) | -20% (1280, 7%) | -43% (10, 10%) | -16% (52, 48%) |
| sl30_tp50 | -62% (993, 16%) | -20% (1280, 7%) | -44% (10, 10%) | -18% (52, 48%) |
| sl50_tp50 | -62% (993, 18%) | -21% (1280, 8%) | -47% (10, 10%) | -18% (52, 48%) |
| no_stop_tp100 | -61% (993, 16%) | -21% (1280, 7%) | -40% (10, 10%) | -16% (52, 48%) |

Verdict: NOT ENOUGH DATA (need 30+ closed filter=1 trades and a CI above zero before believing anything).

Pools seen: 35486. Outcomes:

- missed_window: 22962
- low_liquidity: 6421
- proven_liquidity_gone: 2773
- no_momentum: 1334
- research_failed: 1008
- simulated failed buy: 438
- proven_low_volume: 393
- proven_price_collapsed_or_parabolic: 58
- proven: 53
- proven_no_uptrend: 24
- research_passed: 12
- dip: 10

Warning: 276 judged pools had an unreadable mint/freeze value. Check mint_raw / freeze_raw in candidates.csv; the parsing may need fixing.
