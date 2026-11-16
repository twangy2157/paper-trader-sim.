# Paper trader summary

SIMULATION ONLY. No real trades.

Updated 2026-11-16T08:49:11Z. Bankroll cash (research-selected trades): 456.400154541351. Open positions: 10. Pools on watchlist: 42.

| group | n | win | avg | CI | P&L $ |
|---|---|---|---|---|---|
| research-picked | 16 | 25% | -33.9% | -64 to -3 | -544 |
| momentum, not picked | 2652 | 12% | -66.0% | -68 to -64 | -175272 |
| all momentum | 2668 | 12% | -65.8% | -68 to -64 | -175815 |
| control | 3385 | 6% | -18.8% | -20 to -18 | -64114 |
| dip buy | 35 | 29% | -12.5% | -31 to 8 | -440 |
| proven pools | 114 | 33% | -34.3% | -43 to -25 | -3925 |

What-if exit rules on the SAME trades. Cells: avg return (trades, win rate).

| exit rule | momentum | control | dip | proven |
|---|---|---|---|---|
| base_sl30_tp100 | -66% (2647, 12%) | -19% (3385, 6%) | -13% (35, 29%) | -34% (114, 33%) |
| wide_sl50_tp100 | -66% (2647, 13%) | -19% (3385, 6%) | -15% (35, 31%) | -36% (114, 33%) |
| sl30_tp50 | -67% (2647, 14%) | -19% (3385, 7%) | -18% (35, 31%) | -34% (114, 34%) |
| sl50_tp50 | -67% (2647, 15%) | -19% (3385, 7%) | -19% (35, 37%) | -36% (114, 34%) |
| no_stop_tp100 | -66% (2647, 14%) | -19% (3385, 6%) | -13% (35, 31%) | -36% (114, 33%) |

Verdict: NOT ENOUGH DATA (need 30+ closed filter=1 trades and a CI above zero before believing anything).

Pools seen: 92042. Outcomes:

- missed_window: 60394
- low_liquidity: 15090
- proven_liquidity_gone: 7751
- no_momentum: 3435
- research_failed: 2656
- proven_low_volume: 1215
- simulated failed buy: 1134
- proven_price_collapsed_or_parabolic: 144
- proven: 114
- proven_no_uptrend: 58
- dip: 35
- research_passed: 16

Warning: 725 judged pools had an unreadable mint/freeze value. Check mint_raw / freeze_raw in candidates.csv; the parsing may need fixing.
