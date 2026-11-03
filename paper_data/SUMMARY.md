# Paper trader summary

SIMULATION ONLY. No real trades.

Updated 2026-11-03T07:09:34Z. Bankroll cash (research-selected trades): 898.0. Open positions: 18. Pools on watchlist: 28.

| group | n | win | avg | CI | P&L $ |
|---|---|---|---|---|---|
| research-picked | 1 | 0% | -101.0% | - | -102 |
| momentum, not picked | 248 | 15% | -51.1% | -59 to -43 | -12700 |
| all momentum | 249 | 15% | -51.3% | -60 to -43 | -12802 |
| control | 281 | 9% | -16.8% | -21 to -12 | -4755 |
| dip buy | 1 | 100% | 57.9% | - | 58 |
| proven pools | 5 | 20% | -79.4% | - | -397 |

What-if exit rules on the SAME trades. Cells: avg return (trades, win rate).

| exit rule | momentum | control | dip | proven |
|---|---|---|---|---|
| base_sl30_tp100 | -53% (228, 16%) | -17% (281, 9%) | 58% (1, 100%) | -79% (5, 20%) |
| wide_sl50_tp100 | -53% (228, 18%) | -17% (281, 9%) | 58% (1, 100%) | -79% (5, 20%) |
| sl30_tp50 | -54% (228, 21%) | -18% (281, 9%) | 24% (1, 100%) | -79% (5, 20%) |
| sl50_tp50 | -53% (228, 23%) | -18% (281, 10%) | 24% (1, 100%) | -79% (5, 20%) |
| no_stop_tp100 | -53% (228, 18%) | -17% (281, 9%) | 58% (1, 100%) | -79% (5, 20%) |

Verdict: NOT ENOUGH DATA (need 30+ closed filter=1 trades and a CI above zero before believing anything).

Pools seen: 9655. Outcomes:

- missed_window: 6398
- low_liquidity: 2095
- proven_liquidity_gone: 383
- no_momentum: 333
- research_failed: 256
- simulated failed buy: 97
- proven_low_volume: 65
- proven_price_collapsed_or_parabolic: 11
- proven_no_uptrend: 8
- proven: 7
- research_passed: 1
- dip: 1

Warning: 64 judged pools had an unreadable mint/freeze value. Check mint_raw / freeze_raw in candidates.csv; the parsing may need fixing.
