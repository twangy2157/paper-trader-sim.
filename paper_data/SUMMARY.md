# Paper trader summary

SIMULATION ONLY. No real trades.

Updated 2026-11-17T03:16:32Z. Bankroll cash (research-selected trades): 549.3536238229275. Open positions: 31. Pools on watchlist: 76.

| group | n | win | avg | CI | P&L $ |
|---|---|---|---|---|---|
| research-picked | 17 | 29% | -26.4% | -58 to 8 | -451 |
| momentum, not picked | 2774 | 12% | -66.1% | -68 to -64 | -183663 |
| all momentum | 2791 | 12% | -65.9% | -68 to -64 | -184114 |
| control | 3512 | 6% | -19.1% | -20 to -18 | -67417 |
| dip buy | 36 | 28% | -12.3% | -32 to 7 | -446 |
| proven pools | 114 | 33% | -34.3% | -43 to -25 | -3925 |

What-if exit rules on the SAME trades. Cells: avg return (trades, win rate).

| exit rule | momentum | control | dip | proven |
|---|---|---|---|---|
| base_sl30_tp100 | -66% (2770, 12%) | -19% (3512, 6%) | -12% (36, 28%) | -34% (114, 33%) |
| wide_sl50_tp100 | -66% (2770, 13%) | -19% (3512, 6%) | -15% (36, 31%) | -36% (114, 33%) |
| sl30_tp50 | -67% (2770, 14%) | -19% (3512, 7%) | -18% (36, 31%) | -34% (114, 34%) |
| sl50_tp50 | -67% (2770, 16%) | -20% (3512, 7%) | -19% (36, 36%) | -36% (114, 34%) |
| no_stop_tp100 | -66% (2770, 14%) | -20% (3512, 6%) | -13% (36, 31%) | -36% (114, 33%) |

Verdict: NOT ENOUGH DATA (need 30+ closed filter=1 trades and a CI above zero before believing anything).

Pools seen: 95327. Outcomes:

- missed_window: 62326
- low_liquidity: 15747
- proven_liquidity_gone: 8087
- no_momentum: 3570
- research_failed: 2789
- proven_low_volume: 1255
- simulated failed buy: 1179
- proven_price_collapsed_or_parabolic: 147
- proven: 116
- proven_no_uptrend: 58
- dip: 36
- research_passed: 17

Warning: 751 judged pools had an unreadable mint/freeze value. Check mint_raw / freeze_raw in candidates.csv; the parsing may need fixing.
