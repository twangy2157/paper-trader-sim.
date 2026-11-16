# Paper trader summary

SIMULATION ONLY. No real trades.

Updated 2026-11-16T06:37:13Z. Bankroll cash (research-selected trades): 456.400154541351. Open positions: 13. Pools on watchlist: 48.

| group | n | win | avg | CI | P&L $ |
|---|---|---|---|---|---|
| research-picked | 16 | 25% | -33.9% | -64 to -3 | -544 |
| momentum, not picked | 2648 | 12% | -66.0% | -68 to -64 | -174967 |
| all momentum | 2664 | 12% | -65.8% | -68 to -63 | -175511 |
| control | 3379 | 6% | -18.9% | -20 to -18 | -64034 |
| dip buy | 35 | 29% | -12.5% | -31 to 8 | -440 |
| proven pools | 114 | 33% | -34.3% | -43 to -25 | -3925 |

What-if exit rules on the SAME trades. Cells: avg return (trades, win rate).

| exit rule | momentum | control | dip | proven |
|---|---|---|---|---|
| base_sl30_tp100 | -66% (2643, 12%) | -19% (3379, 6%) | -13% (35, 29%) | -34% (114, 33%) |
| wide_sl50_tp100 | -66% (2643, 13%) | -19% (3379, 6%) | -15% (35, 31%) | -36% (114, 33%) |
| sl30_tp50 | -67% (2643, 14%) | -19% (3379, 7%) | -18% (35, 31%) | -34% (114, 34%) |
| sl50_tp50 | -67% (2643, 16%) | -19% (3379, 7%) | -19% (35, 37%) | -36% (114, 34%) |
| no_stop_tp100 | -66% (2643, 14%) | -19% (3379, 6%) | -13% (35, 31%) | -36% (114, 33%) |

Verdict: NOT ENOUGH DATA (need 30+ closed filter=1 trades and a CI above zero before believing anything).

Pools seen: 91906. Outcomes:

- missed_window: 60290
- low_liquidity: 15082
- proven_liquidity_gone: 7735
- no_momentum: 3432
- research_failed: 2652
- proven_low_volume: 1215
- simulated failed buy: 1133
- proven_price_collapsed_or_parabolic: 144
- proven: 114
- proven_no_uptrend: 58
- dip: 35
- research_passed: 16

Warning: 724 judged pools had an unreadable mint/freeze value. Check mint_raw / freeze_raw in candidates.csv; the parsing may need fixing.
