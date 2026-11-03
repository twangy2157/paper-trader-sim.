# Paper trader summary

SIMULATION ONLY. No real trades.

Updated 2026-11-03T11:43:56Z. Bankroll cash (research-selected trades): 898.0. Open positions: 25. Pools on watchlist: 62.

| group | n | win | avg | CI | P&L $ |
|---|---|---|---|---|---|
| research-picked | 1 | 0% | -101.0% | - | -102 |
| momentum, not picked | 287 | 15% | -52.7% | -60 to -45 | -15151 |
| all momentum | 288 | 15% | -52.9% | -60 to -46 | -15253 |
| control | 330 | 8% | -17.1% | -21 to -13 | -5684 |
| dip buy | 2 | 50% | 24.4% | - | 49 |
| proven pools | 11 | 36% | -41.8% | -73 to -11 | -461 |

What-if exit rules on the SAME trades. Cells: avg return (trades, win rate).

| exit rule | momentum | control | dip | proven |
|---|---|---|---|---|
| base_sl30_tp100 | -54% (267, 16%) | -17% (330, 8%) | 24% (2, 50%) | -42% (11, 36%) |
| wide_sl50_tp100 | -55% (267, 17%) | -18% (330, 8%) | 24% (2, 50%) | -42% (11, 36%) |
| sl30_tp50 | -56% (267, 20%) | -18% (330, 8%) | 7% (2, 50%) | -42% (11, 36%) |
| sl50_tp50 | -55% (267, 22%) | -18% (330, 9%) | 7% (2, 50%) | -42% (11, 36%) |
| no_stop_tp100 | -55% (267, 18%) | -18% (330, 8%) | 24% (2, 50%) | -42% (11, 36%) |

Verdict: NOT ENOUGH DATA (need 30+ closed filter=1 trades and a CI above zero before believing anything).

Pools seen: 10813. Outcomes:

- missed_window: 7147
- low_liquidity: 2259
- proven_liquidity_gone: 489
- no_momentum: 383
- research_failed: 300
- simulated failed buy: 111
- proven_low_volume: 85
- proven: 14
- proven_price_collapsed_or_parabolic: 13
- proven_no_uptrend: 9
- dip: 2
- research_passed: 1

Warning: 71 judged pools had an unreadable mint/freeze value. Check mint_raw / freeze_raw in candidates.csv; the parsing may need fixing.
