# Paper trader summary

SIMULATION ONLY. No real trades.

Updated 2026-11-22T21:55:15Z. Bankroll cash (research-selected trades): 563.74568815387. Open positions: 10. Pools on watchlist: 68.

| group | n | win | avg | CI | P&L $ |
|---|---|---|---|---|---|
| research-picked | 20 | 35% | -21.7% | -51 to 10 | -436 |
| momentum, not picked | 3512 | 12% | -66.0% | -68 to -64 | -232069 |
| all momentum | 3532 | 12% | -65.7% | -68 to -64 | -232506 |
| control | 4251 | 6% | -19.3% | -20 to -18 | -82366 |
| dip buy | 47 | 28% | -12.8% | -30 to 4 | -606 |
| proven pools | 129 | 33% | -31.0% | -40 to -22 | -4017 |

What-if exit rules on the SAME trades. Cells: avg return (trades, win rate).

| exit rule | momentum | control | dip | proven |
|---|---|---|---|---|
| base_sl30_tp100 | -66% (3511, 12%) | -19% (4251, 6%) | -13% (47, 28%) | -31% (129, 33%) |
| wide_sl50_tp100 | -66% (3511, 13%) | -20% (4251, 6%) | -13% (47, 32%) | -32% (129, 33%) |
| sl30_tp50 | -67% (3511, 14%) | -19% (4251, 7%) | -17% (47, 34%) | -31% (129, 33%) |
| sl50_tp50 | -67% (3511, 15%) | -20% (4251, 8%) | -18% (47, 38%) | -32% (129, 33%) |
| no_stop_tp100 | -65% (3511, 14%) | -20% (4251, 7%) | -12% (47, 32%) | -33% (129, 33%) |

Verdict: NOT ENOUGH DATA (need 30+ closed filter=1 trades and a CI above zero before believing anything).

Pools seen: 115826. Outcomes:

- missed_window: 75033
- low_liquidity: 19670
- proven_liquidity_gone: 9958
- no_momentum: 4301
- research_failed: 3516
- proven_low_volume: 1466
- simulated failed buy: 1459
- proven_price_collapsed_or_parabolic: 163
- proven: 129
- proven_no_uptrend: 64
- dip: 47
- research_passed: 20

Warning: 904 judged pools had an unreadable mint/freeze value. Check mint_raw / freeze_raw in candidates.csv; the parsing may need fixing.
