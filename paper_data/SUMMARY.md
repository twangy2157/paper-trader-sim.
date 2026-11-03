# Paper trader summary

SIMULATION ONLY. No real trades.

Updated 2026-11-03T01:35:32Z. Bankroll cash (research-selected trades): 898.5. Open positions: 11. Pools on watchlist: 79.

| group | n | win | avg | CI | P&L $ |
|---|---|---|---|---|---|
| research-picked | 1 | 0% | -101.0% | - | -102 |
| momentum, not picked | 210 | 15% | -51.1% | -59 to -43 | -10757 |
| all momentum | 211 | 15% | -51.4% | -60 to -43 | -10859 |
| control | 232 | 9% | -16.6% | -22 to -12 | -3863 |
| dip buy | 0 | - | - | - | 0 |
| proven pools | 3 | 0% | -100.0% | - | -300 |

What-if exit rules on the SAME trades. Cells: avg return (trades, win rate).

| exit rule | momentum | control | dip | proven |
|---|---|---|---|---|
| base_sl30_tp100 | -53% (190, 16%) | -17% (232, 9%) | - | -100% (3, 0%) |
| wide_sl50_tp100 | -54% (190, 17%) | -17% (232, 9%) | - | -100% (3, 0%) |
| sl30_tp50 | -55% (190, 20%) | -18% (232, 9%) | - | -100% (3, 0%) |
| sl50_tp50 | -54% (190, 22%) | -18% (232, 9%) | - | -100% (3, 0%) |
| no_stop_tp100 | -53% (190, 18%) | -17% (232, 9%) | - | -100% (3, 0%) |

Verdict: NOT ENOUGH DATA (need 30+ closed filter=1 trades and a CI above zero before believing anything).

Pools seen: 8163. Outcomes:

- missed_window: 5419
- low_liquidity: 1854
- no_momentum: 281
- proven_liquidity_gone: 245
- research_failed: 215
- simulated failed buy: 80
- proven_low_volume: 50
- proven_price_collapsed_or_parabolic: 8
- proven_no_uptrend: 6
- proven: 4
- research_passed: 1

Warning: 56 judged pools had an unreadable mint/freeze value. Check mint_raw / freeze_raw in candidates.csv; the parsing may need fixing.
