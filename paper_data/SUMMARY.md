# Paper trader summary

SIMULATION ONLY. No real trades.

Updated 2026-11-03T03:11:12Z. Bankroll cash (research-selected trades): 898.5. Open positions: 19. Pools on watchlist: 43.

| group | n | win | avg | CI | P&L $ |
|---|---|---|---|---|---|
| research-picked | 1 | 0% | -101.0% | - | -102 |
| momentum, not picked | 220 | 15% | -51.4% | -59 to -43 | -11328 |
| all momentum | 221 | 15% | -51.6% | -60 to -43 | -11430 |
| control | 248 | 8% | -16.2% | -21 to -12 | -4051 |
| dip buy | 0 | - | - | - | 0 |
| proven pools | 4 | 0% | -100.3% | - | -401 |

What-if exit rules on the SAME trades. Cells: avg return (trades, win rate).

| exit rule | momentum | control | dip | proven |
|---|---|---|---|---|
| base_sl30_tp100 | -53% (200, 16%) | -16% (248, 8%) | - | -100% (4, 0%) |
| wide_sl50_tp100 | -54% (200, 17%) | -17% (248, 8%) | - | -100% (4, 0%) |
| sl30_tp50 | -55% (200, 20%) | -18% (248, 9%) | - | -100% (4, 0%) |
| sl50_tp50 | -54% (200, 22%) | -18% (248, 9%) | - | -100% (4, 0%) |
| no_stop_tp100 | -54% (200, 18%) | -17% (248, 8%) | - | -100% (4, 0%) |

Verdict: NOT ENOUGH DATA (need 30+ closed filter=1 trades and a CI above zero before believing anything).

Pools seen: 8661. Outcomes:

- missed_window: 5756
- low_liquidity: 1926
- no_momentum: 302
- proven_liquidity_gone: 283
- research_failed: 229
- simulated failed buy: 86
- proven_low_volume: 59
- proven_price_collapsed_or_parabolic: 9
- proven_no_uptrend: 6
- proven: 4
- research_passed: 1

Warning: 59 judged pools had an unreadable mint/freeze value. Check mint_raw / freeze_raw in candidates.csv; the parsing may need fixing.
