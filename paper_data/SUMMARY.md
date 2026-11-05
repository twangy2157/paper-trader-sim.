# Paper trader summary

SIMULATION ONLY. No real trades.

Updated 2026-11-05T11:15:33Z. Bankroll cash (research-selected trades): 651.1520680225926. Open positions: 17. Pools on watchlist: 32.

| group | n | win | avg | CI | P&L $ |
|---|---|---|---|---|---|
| research-picked | 6 | 17% | -41.1% | -82 to 7 | -249 |
| momentum, not picked | 640 | 15% | -55.1% | -60 to -50 | -35296 |
| all momentum | 646 | 15% | -54.9% | -60 to -50 | -35544 |
| control | 772 | 7% | -18.9% | -21 to -16 | -14642 |
| dip buy | 6 | 17% | -25.8% | -68 to 15 | -155 |
| proven pools | 38 | 42% | -17.9% | -34 to -2 | -681 |

What-if exit rules on the SAME trades. Cells: avg return (trades, win rate).

| exit rule | momentum | control | dip | proven |
|---|---|---|---|---|
| base_sl30_tp100 | -56% (625, 16%) | -19% (772, 7%) | -26% (6, 17%) | -18% (38, 42%) |
| wide_sl50_tp100 | -56% (625, 17%) | -19% (772, 8%) | -26% (6, 17%) | -18% (38, 42%) |
| sl30_tp50 | -57% (625, 19%) | -19% (772, 8%) | -31% (6, 17%) | -20% (38, 42%) |
| sl50_tp50 | -56% (625, 21%) | -19% (772, 9%) | -31% (6, 17%) | -20% (38, 42%) |
| no_stop_tp100 | -55% (625, 18%) | -20% (772, 8%) | -26% (6, 17%) | -18% (38, 42%) |

Verdict: NOT ENOUGH DATA (need 30+ closed filter=1 trades and a CI above zero before believing anything).

Pools seen: 22920. Outcomes:

- missed_window: 14968
- low_liquidity: 4243
- proven_liquidity_gone: 1629
- no_momentum: 824
- research_failed: 648
- simulated failed buy: 262
- proven_low_volume: 227
- proven_price_collapsed_or_parabolic: 48
- proven: 38
- proven_no_uptrend: 20
- research_passed: 7
- dip: 6

Warning: 170 judged pools had an unreadable mint/freeze value. Check mint_raw / freeze_raw in candidates.csv; the parsing may need fixing.
