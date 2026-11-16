# Paper trader summary

SIMULATION ONLY. No real trades.

Updated 2026-11-16T11:49:53Z. Bankroll cash (research-selected trades): 549.3536238229275. Open positions: 13. Pools on watchlist: 50.

| group | n | win | avg | CI | P&L $ |
|---|---|---|---|---|---|
| research-picked | 17 | 29% | -26.4% | -58 to 8 | -451 |
| momentum, not picked | 2687 | 12% | -66.1% | -68 to -64 | -177923 |
| all momentum | 2704 | 12% | -65.9% | -68 to -64 | -178374 |
| control | 3408 | 6% | -18.8% | -20 to -18 | -64490 |
| dip buy | 35 | 29% | -12.5% | -31 to 8 | -440 |
| proven pools | 114 | 33% | -34.3% | -43 to -25 | -3925 |

What-if exit rules on the SAME trades. Cells: avg return (trades, win rate).

| exit rule | momentum | control | dip | proven |
|---|---|---|---|---|
| base_sl30_tp100 | -66% (2683, 12%) | -19% (3408, 6%) | -13% (35, 29%) | -34% (114, 33%) |
| wide_sl50_tp100 | -66% (2683, 13%) | -19% (3408, 6%) | -15% (35, 31%) | -36% (114, 33%) |
| sl30_tp50 | -67% (2683, 14%) | -19% (3408, 7%) | -18% (35, 31%) | -34% (114, 34%) |
| sl50_tp50 | -67% (2683, 15%) | -19% (3408, 7%) | -19% (35, 37%) | -36% (114, 34%) |
| no_stop_tp100 | -66% (2683, 14%) | -19% (3408, 6%) | -13% (35, 31%) | -36% (114, 33%) |

Verdict: NOT ENOUGH DATA (need 30+ closed filter=1 trades and a CI above zero before believing anything).

Pools seen: 92780. Outcomes:

- missed_window: 60864
- low_liquidity: 15197
- proven_liquidity_gone: 7828
- no_momentum: 3460
- research_failed: 2692
- proven_low_volume: 1231
- simulated failed buy: 1139
- proven_price_collapsed_or_parabolic: 145
- proven: 114
- proven_no_uptrend: 58
- dip: 35
- research_passed: 17

Warning: 727 judged pools had an unreadable mint/freeze value. Check mint_raw / freeze_raw in candidates.csv; the parsing may need fixing.
