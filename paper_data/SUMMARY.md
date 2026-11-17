# Paper trader summary

SIMULATION ONLY. No real trades.

Updated 2026-11-17T01:52:39Z. Bankroll cash (research-selected trades): 549.3536238229275. Open positions: 21. Pools on watchlist: 60.

| group | n | win | avg | CI | P&L $ |
|---|---|---|---|---|---|
| research-picked | 17 | 29% | -26.4% | -58 to 8 | -451 |
| momentum, not picked | 2759 | 12% | -66.1% | -68 to -64 | -182575 |
| all momentum | 2776 | 12% | -65.8% | -68 to -64 | -183025 |
| control | 3500 | 6% | -19.1% | -20 to -18 | -67227 |
| dip buy | 36 | 28% | -12.3% | -32 to 7 | -446 |
| proven pools | 114 | 33% | -34.3% | -43 to -25 | -3925 |

What-if exit rules on the SAME trades. Cells: avg return (trades, win rate).

| exit rule | momentum | control | dip | proven |
|---|---|---|---|---|
| base_sl30_tp100 | -66% (2755, 12%) | -19% (3500, 6%) | -12% (36, 28%) | -34% (114, 33%) |
| wide_sl50_tp100 | -66% (2755, 13%) | -19% (3500, 6%) | -15% (36, 31%) | -36% (114, 33%) |
| sl30_tp50 | -67% (2755, 14%) | -19% (3500, 7%) | -18% (36, 31%) | -34% (114, 34%) |
| sl50_tp50 | -67% (2755, 15%) | -20% (3500, 7%) | -19% (36, 36%) | -36% (114, 34%) |
| no_stop_tp100 | -66% (2755, 14%) | -20% (3500, 6%) | -13% (36, 31%) | -36% (114, 33%) |

Verdict: NOT ENOUGH DATA (need 30+ closed filter=1 trades and a CI above zero before believing anything).

Pools seen: 95044. Outcomes:

- missed_window: 62166
- low_liquidity: 15684
- proven_liquidity_gone: 8078
- no_momentum: 3554
- research_failed: 2769
- proven_low_volume: 1254
- simulated failed buy: 1166
- proven_price_collapsed_or_parabolic: 147
- proven: 115
- proven_no_uptrend: 58
- dip: 36
- research_passed: 17

Warning: 745 judged pools had an unreadable mint/freeze value. Check mint_raw / freeze_raw in candidates.csv; the parsing may need fixing.
