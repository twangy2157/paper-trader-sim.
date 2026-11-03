# Paper trader summary

SIMULATION ONLY. No real trades.

Updated 2026-11-03T03:51:42Z. Bankroll cash (research-selected trades): 898.0. Open positions: 20. Pools on watchlist: 59.

| group | n | win | avg | CI | P&L $ |
|---|---|---|---|---|---|
| research-picked | 1 | 0% | -101.0% | - | -102 |
| momentum, not picked | 226 | 15% | -50.9% | -59 to -43 | -11532 |
| all momentum | 227 | 15% | -51.2% | -59 to -42 | -11634 |
| control | 254 | 9% | -16.1% | -21 to -11 | -4113 |
| dip buy | 0 | - | - | - | 0 |
| proven pools | 4 | 0% | -100.3% | - | -401 |

What-if exit rules on the SAME trades. Cells: avg return (trades, win rate).

| exit rule | momentum | control | dip | proven |
|---|---|---|---|---|
| base_sl30_tp100 | -53% (206, 17%) | -16% (254, 9%) | - | -100% (4, 0%) |
| wide_sl50_tp100 | -53% (206, 17%) | -17% (254, 9%) | - | -100% (4, 0%) |
| sl30_tp50 | -55% (206, 20%) | -17% (254, 9%) | - | -100% (4, 0%) |
| sl50_tp50 | -54% (206, 22%) | -17% (254, 9%) | - | -100% (4, 0%) |
| no_stop_tp100 | -53% (206, 18%) | -17% (254, 9%) | - | -100% (4, 0%) |

Verdict: NOT ENOUGH DATA (need 30+ closed filter=1 trades and a CI above zero before believing anything).

Pools seen: 8847. Outcomes:

- missed_window: 5877
- low_liquidity: 1953
- no_momentum: 308
- proven_liquidity_gone: 302
- research_failed: 234
- simulated failed buy: 91
- proven_low_volume: 60
- proven_price_collapsed_or_parabolic: 9
- proven_no_uptrend: 6
- proven: 5
- research_passed: 1
- dip: 1

Warning: 60 judged pools had an unreadable mint/freeze value. Check mint_raw / freeze_raw in candidates.csv; the parsing may need fixing.
