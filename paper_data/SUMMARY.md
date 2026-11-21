# Paper trader summary

SIMULATION ONLY. No real trades.

Updated 2026-11-21T00:46:44Z. Bankroll cash (research-selected trades): 563.74568815387. Open positions: 10. Pools on watchlist: 43.

| group | n | win | avg | CI | P&L $ |
|---|---|---|---|---|---|
| research-picked | 20 | 35% | -21.7% | -51 to 10 | -436 |
| momentum, not picked | 3309 | 12% | -66.7% | -69 to -65 | -220915 |
| all momentum | 3329 | 12% | -66.4% | -68 to -64 | -221351 |
| control | 4042 | 6% | -19.2% | -20 to -18 | -78018 |
| dip buy | 45 | 27% | -13.2% | -30 to 5 | -596 |
| proven pools | 126 | 33% | -30.7% | -39 to -21 | -3879 |

What-if exit rules on the SAME trades. Cells: avg return (trades, win rate).

| exit rule | momentum | control | dip | proven |
|---|---|---|---|---|
| base_sl30_tp100 | -67% (3308, 12%) | -19% (4042, 6%) | -13% (45, 27%) | -31% (126, 33%) |
| wide_sl50_tp100 | -66% (3308, 13%) | -19% (4042, 7%) | -13% (45, 31%) | -32% (126, 33%) |
| sl30_tp50 | -68% (3308, 14%) | -19% (4042, 7%) | -16% (45, 33%) | -31% (126, 34%) |
| sl50_tp50 | -68% (3308, 15%) | -20% (4042, 8%) | -18% (45, 38%) | -32% (126, 34%) |
| no_stop_tp100 | -66% (3308, 14%) | -20% (4042, 7%) | -12% (45, 31%) | -32% (126, 33%) |

Verdict: NOT ENOUGH DATA (need 30+ closed filter=1 trades and a CI above zero before believing anything).

Pools seen: 109306. Outcomes:

- missed_window: 70849
- low_liquidity: 18415
- proven_liquidity_gone: 9460
- no_momentum: 4093
- research_failed: 3312
- proven_low_volume: 1397
- simulated failed buy: 1369
- proven_price_collapsed_or_parabolic: 158
- proven: 126
- proven_no_uptrend: 62
- dip: 45
- research_passed: 20

Warning: 866 judged pools had an unreadable mint/freeze value. Check mint_raw / freeze_raw in candidates.csv; the parsing may need fixing.
