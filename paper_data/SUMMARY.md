# Paper trader summary

SIMULATION ONLY. No real trades.

Updated 2026-11-03T03:01:09Z. Bankroll cash (research-selected trades): 898.5. Open positions: 16. Pools on watchlist: 56.

| group | n | win | avg | CI | P&L $ |
|---|---|---|---|---|---|
| research-picked | 1 | 0% | -101.0% | - | -102 |
| momentum, not picked | 219 | 15% | -51.2% | -59 to -43 | -11228 |
| all momentum | 220 | 15% | -51.4% | -60 to -43 | -11329 |
| control | 247 | 9% | -16.3% | -21 to -12 | -4046 |
| dip buy | 0 | - | - | - | 0 |
| proven pools | 4 | 0% | -100.3% | - | -401 |

What-if exit rules on the SAME trades. Cells: avg return (trades, win rate).

| exit rule | momentum | control | dip | proven |
|---|---|---|---|---|
| base_sl30_tp100 | -53% (199, 16%) | -16% (247, 9%) | - | -100% (4, 0%) |
| wide_sl50_tp100 | -54% (199, 17%) | -17% (247, 9%) | - | -100% (4, 0%) |
| sl30_tp50 | -55% (199, 20%) | -18% (247, 9%) | - | -100% (4, 0%) |
| sl50_tp50 | -54% (199, 22%) | -18% (247, 9%) | - | -100% (4, 0%) |
| no_stop_tp100 | -54% (199, 18%) | -17% (247, 9%) | - | -100% (4, 0%) |

Verdict: NOT ENOUGH DATA (need 30+ closed filter=1 trades and a CI above zero before believing anything).

Pools seen: 8610. Outcomes:

- missed_window: 5721
- low_liquidity: 1922
- no_momentum: 300
- proven_liquidity_gone: 278
- research_failed: 226
- simulated failed buy: 85
- proven_low_volume: 58
- proven_price_collapsed_or_parabolic: 9
- proven_no_uptrend: 6
- proven: 4
- research_passed: 1

Warning: 58 judged pools had an unreadable mint/freeze value. Check mint_raw / freeze_raw in candidates.csv; the parsing may need fixing.
