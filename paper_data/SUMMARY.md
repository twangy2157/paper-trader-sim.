# Paper trader summary

SIMULATION ONLY. No real trades.

Updated 2026-11-02T20:26:40Z. Bankroll cash (research-selected trades): 898.5. Open positions: 23. Pools on watchlist: 45.

| group | n | win | avg | CI | P&L $ |
|---|---|---|---|---|---|
| research-picked | 1 | 0% | -101.0% | - | -102 |
| momentum, not picked | 181 | 15% | -52.5% | -62 to -43 | -9526 |
| all momentum | 182 | 15% | -52.8% | -61 to -44 | -9627 |
| control | 166 | 11% | -15.6% | -22 to -10 | -2609 |
| dip buy | 0 | - | - | - | 0 |
| proven pools | 1 | 0% | -100.0% | - | -100 |

What-if exit rules on the SAME trades. Cells: avg return (trades, win rate).

| exit rule | momentum | control | dip | proven |
|---|---|---|---|---|
| base_sl30_tp100 | -55% (161, 16%) | -16% (166, 11%) | - | -100% (1, 0%) |
| wide_sl50_tp100 | -56% (161, 17%) | -16% (166, 11%) | - | -100% (1, 0%) |
| sl30_tp50 | -57% (161, 19%) | -18% (166, 12%) | - | -100% (1, 0%) |
| sl50_tp50 | -56% (161, 22%) | -17% (166, 13%) | - | -100% (1, 0%) |
| no_stop_tp100 | -55% (161, 18%) | -17% (166, 11%) | - | -100% (1, 0%) |

Verdict: NOT ENOUGH DATA (need 30+ closed filter=1 trades and a CI above zero before believing anything).

Pools seen: 6757. Outcomes:

- missed_window: 4449
- low_liquidity: 1660
- no_momentum: 225
- research_failed: 187
- proven_liquidity_gone: 147
- simulated failed buy: 62
- proven_low_volume: 18
- proven: 3
- proven_price_collapsed_or_parabolic: 3
- proven_no_uptrend: 2
- research_passed: 1

Warning: 39 judged pools had an unreadable mint/freeze value. Check mint_raw / freeze_raw in candidates.csv; the parsing may need fixing.
