# Paper trader summary

SIMULATION ONLY. No real trades.

Updated 2026-11-03T02:49:43Z. Bankroll cash (research-selected trades): 898.5. Open positions: 21. Pools on watchlist: 63.

| group | n | win | avg | CI | P&L $ |
|---|---|---|---|---|---|
| research-picked | 1 | 0% | -101.0% | - | -102 |
| momentum, not picked | 217 | 15% | -51.1% | -60 to -43 | -11115 |
| all momentum | 218 | 15% | -51.4% | -59 to -43 | -11216 |
| control | 242 | 8% | -16.5% | -21 to -12 | -4016 |
| dip buy | 0 | - | - | - | 0 |
| proven pools | 4 | 0% | -100.3% | - | -401 |

What-if exit rules on the SAME trades. Cells: avg return (trades, win rate).

| exit rule | momentum | control | dip | proven |
|---|---|---|---|---|
| base_sl30_tp100 | -53% (197, 16%) | -17% (242, 8%) | - | -100% (4, 0%) |
| wide_sl50_tp100 | -54% (197, 17%) | -17% (242, 8%) | - | -100% (4, 0%) |
| sl30_tp50 | -55% (197, 20%) | -18% (242, 9%) | - | -100% (4, 0%) |
| sl50_tp50 | -54% (197, 22%) | -18% (242, 9%) | - | -100% (4, 0%) |
| no_stop_tp100 | -53% (197, 18%) | -17% (242, 8%) | - | -100% (4, 0%) |

Verdict: NOT ENOUGH DATA (need 30+ closed filter=1 trades and a CI above zero before believing anything).

Pools seen: 8557. Outcomes:

- missed_window: 5681
- low_liquidity: 1917
- no_momentum: 298
- proven_liquidity_gone: 275
- research_failed: 226
- simulated failed buy: 84
- proven_low_volume: 56
- proven_price_collapsed_or_parabolic: 9
- proven_no_uptrend: 6
- proven: 4
- research_passed: 1

Warning: 57 judged pools had an unreadable mint/freeze value. Check mint_raw / freeze_raw in candidates.csv; the parsing may need fixing.
