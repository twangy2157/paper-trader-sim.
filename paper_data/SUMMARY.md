# Paper trader summary

SIMULATION ONLY. No real trades.

Updated 2026-11-02T23:17:44Z. Bankroll cash (research-selected trades): 898.5. Open positions: 13. Pools on watchlist: 42.

| group | n | win | avg | CI | P&L $ |
|---|---|---|---|---|---|
| research-picked | 1 | 0% | -101.0% | - | -102 |
| momentum, not picked | 197 | 15% | -52.3% | -61 to -44 | -10315 |
| all momentum | 198 | 15% | -52.5% | -61 to -44 | -10417 |
| control | 203 | 9% | -16.0% | -21 to -11 | -3268 |
| dip buy | 0 | - | - | - | 0 |
| proven pools | 3 | 0% | -100.0% | - | -300 |

What-if exit rules on the SAME trades. Cells: avg return (trades, win rate).

| exit rule | momentum | control | dip | proven |
|---|---|---|---|---|
| base_sl30_tp100 | -54% (177, 16%) | -16% (203, 9%) | - | -100% (3, 0%) |
| wide_sl50_tp100 | -55% (177, 17%) | -17% (203, 9%) | - | -100% (3, 0%) |
| sl30_tp50 | -55% (177, 20%) | -18% (203, 10%) | - | -100% (3, 0%) |
| sl50_tp50 | -55% (177, 22%) | -18% (203, 10%) | - | -100% (3, 0%) |
| no_stop_tp100 | -54% (177, 18%) | -17% (203, 9%) | - | -100% (3, 0%) |

Verdict: NOT ENOUGH DATA (need 30+ closed filter=1 trades and a CI above zero before believing anything).

Pools seen: 7636. Outcomes:

- missed_window: 5093
- low_liquidity: 1772
- no_momentum: 256
- research_failed: 201
- proven_liquidity_gone: 198
- simulated failed buy: 70
- proven_low_volume: 33
- proven_no_uptrend: 5
- proven_price_collapsed_or_parabolic: 4
- proven: 3
- research_passed: 1

Warning: 48 judged pools had an unreadable mint/freeze value. Check mint_raw / freeze_raw in candidates.csv; the parsing may need fixing.
