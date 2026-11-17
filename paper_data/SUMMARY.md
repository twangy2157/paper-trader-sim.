# Paper trader summary

SIMULATION ONLY. No real trades.

Updated 2026-11-17T01:09:12Z. Bankroll cash (research-selected trades): 549.3536238229275. Open positions: 9. Pools on watchlist: 29.

| group | n | win | avg | CI | P&L $ |
|---|---|---|---|---|---|
| research-picked | 17 | 29% | -26.4% | -58 to 8 | -451 |
| momentum, not picked | 2758 | 12% | -66.1% | -68 to -64 | -182475 |
| all momentum | 2775 | 12% | -65.8% | -68 to -64 | -182925 |
| control | 3496 | 6% | -19.1% | -20 to -18 | -67161 |
| dip buy | 36 | 28% | -12.3% | -32 to 7 | -446 |
| proven pools | 114 | 33% | -34.3% | -43 to -25 | -3925 |

What-if exit rules on the SAME trades. Cells: avg return (trades, win rate).

| exit rule | momentum | control | dip | proven |
|---|---|---|---|---|
| base_sl30_tp100 | -66% (2754, 12%) | -19% (3496, 6%) | -12% (36, 28%) | -34% (114, 33%) |
| wide_sl50_tp100 | -66% (2754, 13%) | -19% (3496, 6%) | -15% (36, 31%) | -36% (114, 33%) |
| sl30_tp50 | -67% (2754, 14%) | -19% (3496, 7%) | -18% (36, 31%) | -34% (114, 34%) |
| sl50_tp50 | -67% (2754, 16%) | -20% (3496, 7%) | -19% (36, 36%) | -36% (114, 34%) |
| no_stop_tp100 | -66% (2754, 14%) | -20% (3496, 6%) | -13% (36, 31%) | -36% (114, 33%) |

Verdict: NOT ENOUGH DATA (need 30+ closed filter=1 trades and a CI above zero before believing anything).

Pools seen: 94843. Outcomes:

- missed_window: 62049
- low_liquidity: 15633
- proven_liquidity_gone: 8062
- no_momentum: 3546
- research_failed: 2760
- proven_low_volume: 1254
- simulated failed buy: 1166
- proven_price_collapsed_or_parabolic: 147
- proven: 115
- proven_no_uptrend: 58
- dip: 36
- research_passed: 17

Warning: 745 judged pools had an unreadable mint/freeze value. Check mint_raw / freeze_raw in candidates.csv; the parsing may need fixing.
