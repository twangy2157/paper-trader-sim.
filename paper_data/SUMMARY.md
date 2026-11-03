# Paper trader summary

SIMULATION ONLY. No real trades.

Updated 2026-11-03T01:13:56Z. Bankroll cash (research-selected trades): 898.5. Open positions: 12. Pools on watchlist: 57.

| group | n | win | avg | CI | P&L $ |
|---|---|---|---|---|---|
| research-picked | 1 | 0% | -101.0% | - | -102 |
| momentum, not picked | 208 | 15% | -50.8% | -60 to -42 | -10589 |
| all momentum | 209 | 15% | -51.1% | -60 to -42 | -10690 |
| control | 226 | 9% | -16.4% | -21 to -11 | -3723 |
| dip buy | 0 | - | - | - | 0 |
| proven pools | 3 | 0% | -100.0% | - | -300 |

What-if exit rules on the SAME trades. Cells: avg return (trades, win rate).

| exit rule | momentum | control | dip | proven |
|---|---|---|---|---|
| base_sl30_tp100 | -53% (188, 16%) | -16% (226, 9%) | - | -100% (3, 0%) |
| wide_sl50_tp100 | -53% (188, 18%) | -17% (226, 9%) | - | -100% (3, 0%) |
| sl30_tp50 | -54% (188, 20%) | -18% (226, 9%) | - | -100% (3, 0%) |
| sl50_tp50 | -54% (188, 22%) | -18% (226, 10%) | - | -100% (3, 0%) |
| no_stop_tp100 | -53% (188, 18%) | -17% (226, 9%) | - | -100% (3, 0%) |

Verdict: NOT ENOUGH DATA (need 30+ closed filter=1 trades and a CI above zero before believing anything).

Pools seen: 8062. Outcomes:

- missed_window: 5351
- low_liquidity: 1841
- no_momentum: 278
- proven_liquidity_gone: 240
- research_failed: 211
- simulated failed buy: 77
- proven_low_volume: 46
- proven_price_collapsed_or_parabolic: 7
- proven_no_uptrend: 6
- proven: 4
- research_passed: 1

Warning: 55 judged pools had an unreadable mint/freeze value. Check mint_raw / freeze_raw in candidates.csv; the parsing may need fixing.
