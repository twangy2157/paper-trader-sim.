# Paper trader summary

SIMULATION ONLY. No real trades.

Updated 2026-11-05T11:37:20Z. Bankroll cash (research-selected trades): 551.1520680225926. Open positions: 16. Pools on watchlist: 34.

| group | n | win | avg | CI | P&L $ |
|---|---|---|---|---|---|
| research-picked | 6 | 17% | -41.1% | -82 to 7 | -249 |
| momentum, not picked | 642 | 15% | -55.2% | -60 to -50 | -35496 |
| all momentum | 648 | 15% | -55.1% | -60 to -50 | -35744 |
| control | 776 | 7% | -18.8% | -21 to -16 | -14663 |
| dip buy | 6 | 17% | -25.8% | -68 to 15 | -155 |
| proven pools | 38 | 42% | -17.9% | -34 to -2 | -681 |

What-if exit rules on the SAME trades. Cells: avg return (trades, win rate).

| exit rule | momentum | control | dip | proven |
|---|---|---|---|---|
| base_sl30_tp100 | -56% (627, 15%) | -19% (776, 7%) | -26% (6, 17%) | -18% (38, 42%) |
| wide_sl50_tp100 | -56% (627, 17%) | -19% (776, 8%) | -26% (6, 17%) | -18% (38, 42%) |
| sl30_tp50 | -57% (627, 19%) | -19% (776, 8%) | -31% (6, 17%) | -20% (38, 42%) |
| sl50_tp50 | -56% (627, 21%) | -19% (776, 9%) | -31% (6, 17%) | -20% (38, 42%) |
| no_stop_tp100 | -55% (627, 18%) | -19% (776, 8%) | -26% (6, 17%) | -18% (38, 42%) |

Verdict: NOT ENOUGH DATA (need 30+ closed filter=1 trades and a CI above zero before believing anything).

Pools seen: 23002. Outcomes:

- missed_window: 15011
- low_liquidity: 4264
- proven_liquidity_gone: 1639
- no_momentum: 826
- research_failed: 650
- simulated failed buy: 263
- proven_low_volume: 229
- proven_price_collapsed_or_parabolic: 48
- proven: 38
- proven_no_uptrend: 20
- research_passed: 8
- dip: 6

Warning: 171 judged pools had an unreadable mint/freeze value. Check mint_raw / freeze_raw in candidates.csv; the parsing may need fixing.
