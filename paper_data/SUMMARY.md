# Paper trader summary

SIMULATION ONLY. No real trades.

Updated 2026-11-03T15:02:12Z. Bankroll cash (research-selected trades): 898.0. Open positions: 19. Pools on watchlist: 62.

| group | n | win | avg | CI | P&L $ |
|---|---|---|---|---|---|
| research-picked | 1 | 0% | -101.0% | - | -102 |
| momentum, not picked | 320 | 14% | -54.3% | -61 to -47 | -17417 |
| all momentum | 321 | 14% | -54.5% | -61 to -48 | -17519 |
| control | 353 | 8% | -16.6% | -21 to -13 | -5880 |
| dip buy | 2 | 50% | 24.4% | - | 49 |
| proven pools | 14 | 36% | -32.3% | -61 to -5 | -453 |

What-if exit rules on the SAME trades. Cells: avg return (trades, win rate).

| exit rule | momentum | control | dip | proven |
|---|---|---|---|---|
| base_sl30_tp100 | -56% (300, 15%) | -17% (353, 8%) | 24% (2, 50%) | -32% (14, 36%) |
| wide_sl50_tp100 | -55% (300, 17%) | -17% (353, 8%) | 24% (2, 50%) | -32% (14, 36%) |
| sl30_tp50 | -57% (300, 19%) | -18% (353, 8%) | 7% (2, 50%) | -32% (14, 36%) |
| sl50_tp50 | -56% (300, 22%) | -18% (353, 9%) | 7% (2, 50%) | -32% (14, 36%) |
| no_stop_tp100 | -55% (300, 18%) | -17% (353, 8%) | 24% (2, 50%) | -32% (14, 36%) |

Verdict: NOT ENOUGH DATA (need 30+ closed filter=1 trades and a CI above zero before believing anything).

Pools seen: 11692. Outcomes:

- missed_window: 7732
- low_liquidity: 2397
- proven_liquidity_gone: 570
- no_momentum: 408
- research_failed: 327
- simulated failed buy: 120
- proven_low_volume: 96
- proven: 15
- proven_price_collapsed_or_parabolic: 15
- proven_no_uptrend: 9
- dip: 2
- research_passed: 1

Warning: 76 judged pools had an unreadable mint/freeze value. Check mint_raw / freeze_raw in candidates.csv; the parsing may need fixing.
