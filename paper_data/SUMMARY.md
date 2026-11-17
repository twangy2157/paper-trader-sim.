# Paper trader summary

SIMULATION ONLY. No real trades.

Updated 2026-11-17T02:45:21Z. Bankroll cash (research-selected trades): 549.3536238229275. Open positions: 35. Pools on watchlist: 33.

| group | n | win | avg | CI | P&L $ |
|---|---|---|---|---|---|
| research-picked | 17 | 29% | -26.4% | -58 to 8 | -451 |
| momentum, not picked | 2764 | 12% | -66.1% | -68 to -64 | -182893 |
| all momentum | 2781 | 12% | -65.8% | -68 to -64 | -183344 |
| control | 3506 | 6% | -19.1% | -20 to -18 | -67370 |
| dip buy | 36 | 28% | -12.3% | -32 to 7 | -446 |
| proven pools | 114 | 33% | -34.3% | -43 to -25 | -3925 |

What-if exit rules on the SAME trades. Cells: avg return (trades, win rate).

| exit rule | momentum | control | dip | proven |
|---|---|---|---|---|
| base_sl30_tp100 | -66% (2760, 12%) | -19% (3506, 6%) | -12% (36, 28%) | -34% (114, 33%) |
| wide_sl50_tp100 | -66% (2760, 13%) | -19% (3506, 6%) | -15% (36, 31%) | -36% (114, 33%) |
| sl30_tp50 | -67% (2760, 14%) | -19% (3506, 7%) | -18% (36, 31%) | -34% (114, 34%) |
| sl50_tp50 | -67% (2760, 15%) | -20% (3506, 7%) | -19% (36, 36%) | -36% (114, 34%) |
| no_stop_tp100 | -66% (2760, 14%) | -20% (3506, 6%) | -13% (36, 31%) | -36% (114, 33%) |

Verdict: NOT ENOUGH DATA (need 30+ closed filter=1 trades and a CI above zero before believing anything).

Pools seen: 95234. Outcomes:

- missed_window: 62270
- low_liquidity: 15736
- proven_liquidity_gone: 8078
- no_momentum: 3564
- research_failed: 2784
- proven_low_volume: 1254
- simulated failed buy: 1175
- proven_price_collapsed_or_parabolic: 147
- proven: 115
- proven_no_uptrend: 58
- dip: 36
- research_passed: 17

Warning: 749 judged pools had an unreadable mint/freeze value. Check mint_raw / freeze_raw in candidates.csv; the parsing may need fixing.
