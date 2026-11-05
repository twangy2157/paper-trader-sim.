# Paper trader summary

SIMULATION ONLY. No real trades.

Updated 2026-11-05T08:37:33Z. Bankroll cash (research-selected trades): 751.6520680225926. Open positions: 22. Pools on watchlist: 49.

| group | n | win | avg | CI | P&L $ |
|---|---|---|---|---|---|
| research-picked | 6 | 17% | -41.1% | -82 to 7 | -248 |
| momentum, not picked | 620 | 15% | -54.7% | -59 to -50 | -33968 |
| all momentum | 626 | 15% | -54.6% | -59 to -50 | -34217 |
| control | 748 | 8% | -19.0% | -22 to -16 | -14272 |
| dip buy | 5 | 20% | -30.5% | - | -152 |
| proven pools | 35 | 43% | -17.0% | -34 to -1 | -597 |

What-if exit rules on the SAME trades. Cells: avg return (trades, win rate).

| exit rule | momentum | control | dip | proven |
|---|---|---|---|---|
| base_sl30_tp100 | -55% (605, 16%) | -19% (748, 8%) | -30% (5, 20%) | -17% (35, 43%) |
| wide_sl50_tp100 | -55% (605, 18%) | -19% (748, 8%) | -30% (5, 20%) | -17% (35, 43%) |
| sl30_tp50 | -56% (605, 20%) | -19% (748, 9%) | -37% (5, 20%) | -19% (35, 43%) |
| sl50_tp50 | -56% (605, 22%) | -20% (748, 9%) | -37% (5, 20%) | -19% (35, 43%) |
| no_stop_tp100 | -54% (605, 19%) | -20% (748, 8%) | -30% (5, 20%) | -17% (35, 43%) |

Verdict: NOT ENOUGH DATA (need 30+ closed filter=1 trades and a CI above zero before believing anything).

Pools seen: 22249. Outcomes:

- missed_window: 14564
- low_liquidity: 4092
- proven_liquidity_gone: 1566
- no_momentum: 801
- research_failed: 630
- simulated failed buy: 253
- proven_low_volume: 226
- proven_price_collapsed_or_parabolic: 48
- proven: 38
- proven_no_uptrend: 20
- research_passed: 6
- dip: 5

Warning: 167 judged pools had an unreadable mint/freeze value. Check mint_raw / freeze_raw in candidates.csv; the parsing may need fixing.
