# Paper trader summary

SIMULATION ONLY. No real trades.

Updated 2026-11-02T23:29:12Z. Bankroll cash (research-selected trades): 898.5. Open positions: 15. Pools on watchlist: 71.

| group | n | win | avg | CI | P&L $ |
|---|---|---|---|---|---|
| research-picked | 1 | 0% | -101.0% | - | -102 |
| momentum, not picked | 199 | 15% | -51.3% | -60 to -42 | -10227 |
| all momentum | 200 | 15% | -51.6% | -60 to -43 | -10328 |
| control | 205 | 10% | -15.7% | -21 to -10 | -3235 |
| dip buy | 0 | - | - | - | 0 |
| proven pools | 3 | 0% | -100.0% | - | -300 |

What-if exit rules on the SAME trades. Cells: avg return (trades, win rate).

| exit rule | momentum | control | dip | proven |
|---|---|---|---|---|
| base_sl30_tp100 | -53% (179, 16%) | -16% (205, 10%) | - | -100% (3, 0%) |
| wide_sl50_tp100 | -54% (179, 17%) | -16% (205, 10%) | - | -100% (3, 0%) |
| sl30_tp50 | -55% (179, 20%) | -17% (205, 10%) | - | -100% (3, 0%) |
| sl50_tp50 | -54% (179, 22%) | -17% (205, 11%) | - | -100% (3, 0%) |
| no_stop_tp100 | -53% (179, 18%) | -16% (205, 10%) | - | -100% (3, 0%) |

Verdict: NOT ENOUGH DATA (need 30+ closed filter=1 trades and a CI above zero before believing anything).

Pools seen: 7666. Outcomes:

- missed_window: 5104
- low_liquidity: 1777
- no_momentum: 261
- research_failed: 202
- proven_liquidity_gone: 202
- simulated failed buy: 70
- proven_low_volume: 36
- proven_no_uptrend: 5
- proven_price_collapsed_or_parabolic: 5
- proven: 3
- research_passed: 1

Warning: 48 judged pools had an unreadable mint/freeze value. Check mint_raw / freeze_raw in candidates.csv; the parsing may need fixing.
