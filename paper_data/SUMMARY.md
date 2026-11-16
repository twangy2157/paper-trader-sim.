# Paper trader summary

SIMULATION ONLY. No real trades.

Updated 2026-11-16T06:48:29Z. Bankroll cash (research-selected trades): 456.400154541351. Open positions: 16. Pools on watchlist: 56.

| group | n | win | avg | CI | P&L $ |
|---|---|---|---|---|---|
| research-picked | 16 | 25% | -33.9% | -64 to -3 | -544 |
| momentum, not picked | 2649 | 12% | -66.0% | -68 to -64 | -175067 |
| all momentum | 2665 | 12% | -65.8% | -68 to -64 | -175611 |
| control | 3380 | 6% | -18.8% | -20 to -18 | -63992 |
| dip buy | 35 | 29% | -12.5% | -31 to 8 | -440 |
| proven pools | 114 | 33% | -34.3% | -43 to -25 | -3925 |

What-if exit rules on the SAME trades. Cells: avg return (trades, win rate).

| exit rule | momentum | control | dip | proven |
|---|---|---|---|---|
| base_sl30_tp100 | -66% (2644, 12%) | -19% (3380, 6%) | -13% (35, 29%) | -34% (114, 33%) |
| wide_sl50_tp100 | -66% (2644, 13%) | -19% (3380, 6%) | -15% (35, 31%) | -36% (114, 33%) |
| sl30_tp50 | -67% (2644, 14%) | -19% (3380, 7%) | -18% (35, 31%) | -34% (114, 34%) |
| sl50_tp50 | -67% (2644, 16%) | -19% (3380, 7%) | -19% (35, 37%) | -36% (114, 34%) |
| no_stop_tp100 | -66% (2644, 14%) | -19% (3380, 6%) | -13% (35, 31%) | -36% (114, 33%) |

Verdict: NOT ENOUGH DATA (need 30+ closed filter=1 trades and a CI above zero before believing anything).

Pools seen: 91946. Outcomes:

- missed_window: 60313
- low_liquidity: 15088
- proven_liquidity_gone: 7740
- no_momentum: 3433
- research_failed: 2656
- proven_low_volume: 1215
- simulated failed buy: 1134
- proven_price_collapsed_or_parabolic: 144
- proven: 114
- proven_no_uptrend: 58
- dip: 35
- research_passed: 16

Warning: 725 judged pools had an unreadable mint/freeze value. Check mint_raw / freeze_raw in candidates.csv; the parsing may need fixing.
