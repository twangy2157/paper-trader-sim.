# Paper trader summary

SIMULATION ONLY. No real trades.

Updated 2026-11-05T12:08:54Z. Bankroll cash (research-selected trades): 684.9661609033643. Open positions: 13. Pools on watchlist: 51.

| group | n | win | avg | CI | P&L $ |
|---|---|---|---|---|---|
| research-picked | 7 | 29% | -30.4% | -72 to 15 | -215 |
| momentum, not picked | 647 | 15% | -55.2% | -60 to -50 | -35801 |
| all momentum | 654 | 15% | -55.0% | -60 to -50 | -36016 |
| control | 780 | 7% | -18.7% | -21 to -16 | -14653 |
| dip buy | 6 | 17% | -25.8% | -68 to 15 | -155 |
| proven pools | 38 | 42% | -17.9% | -34 to -2 | -681 |

What-if exit rules on the SAME trades. Cells: avg return (trades, win rate).

| exit rule | momentum | control | dip | proven |
|---|---|---|---|---|
| base_sl30_tp100 | -56% (633, 15%) | -19% (780, 7%) | -26% (6, 17%) | -18% (38, 42%) |
| wide_sl50_tp100 | -56% (633, 17%) | -19% (780, 8%) | -26% (6, 17%) | -18% (38, 42%) |
| sl30_tp50 | -57% (633, 19%) | -19% (780, 8%) | -31% (6, 17%) | -20% (38, 42%) |
| sl50_tp50 | -56% (633, 21%) | -19% (780, 9%) | -31% (6, 17%) | -20% (38, 42%) |
| no_stop_tp100 | -55% (633, 18%) | -19% (780, 8%) | -26% (6, 17%) | -18% (38, 42%) |

Verdict: NOT ENOUGH DATA (need 30+ closed filter=1 trades and a CI above zero before believing anything).

Pools seen: 23121. Outcomes:

- missed_window: 15077
- low_liquidity: 4291
- proven_liquidity_gone: 1658
- no_momentum: 830
- research_failed: 653
- simulated failed buy: 263
- proven_low_volume: 229
- proven_price_collapsed_or_parabolic: 48
- proven: 38
- proven_no_uptrend: 20
- research_passed: 8
- dip: 6

Warning: 171 judged pools had an unreadable mint/freeze value. Check mint_raw / freeze_raw in candidates.csv; the parsing may need fixing.
