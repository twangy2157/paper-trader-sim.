# Paper trader summary

SIMULATION ONLY. No real trades.

Updated 2026-11-03T01:24:00Z. Bankroll cash (research-selected trades): 898.5. Open positions: 8. Pools on watchlist: 74.

| group | n | win | avg | CI | P&L $ |
|---|---|---|---|---|---|
| research-picked | 1 | 0% | -101.0% | - | -102 |
| momentum, not picked | 210 | 15% | -51.1% | -59 to -43 | -10757 |
| all momentum | 211 | 15% | -51.4% | -60 to -43 | -10858 |
| control | 230 | 9% | -16.6% | -22 to -12 | -3850 |
| dip buy | 0 | - | - | - | 0 |
| proven pools | 3 | 0% | -100.0% | - | -300 |

What-if exit rules on the SAME trades. Cells: avg return (trades, win rate).

| exit rule | momentum | control | dip | proven |
|---|---|---|---|---|
| base_sl30_tp100 | -53% (190, 16%) | -17% (230, 9%) | - | -100% (3, 0%) |
| wide_sl50_tp100 | -54% (190, 17%) | -17% (230, 9%) | - | -100% (3, 0%) |
| sl30_tp50 | -55% (190, 20%) | -18% (230, 9%) | - | -100% (3, 0%) |
| sl50_tp50 | -54% (190, 22%) | -18% (230, 10%) | - | -100% (3, 0%) |
| no_stop_tp100 | -53% (190, 18%) | -17% (230, 9%) | - | -100% (3, 0%) |

Verdict: NOT ENOUGH DATA (need 30+ closed filter=1 trades and a CI above zero before believing anything).

Pools seen: 8100. Outcomes:

- missed_window: 5378
- low_liquidity: 1846
- no_momentum: 278
- proven_liquidity_gone: 243
- research_failed: 213
- simulated failed buy: 78
- proven_low_volume: 46
- proven_price_collapsed_or_parabolic: 7
- proven_no_uptrend: 6
- proven: 4
- research_passed: 1

Warning: 55 judged pools had an unreadable mint/freeze value. Check mint_raw / freeze_raw in candidates.csv; the parsing may need fixing.
