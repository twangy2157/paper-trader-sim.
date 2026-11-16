# Paper trader summary

SIMULATION ONLY. No real trades.

Updated 2026-11-16T18:13:56Z. Bankroll cash (research-selected trades): 549.3536238229275. Open positions: 14. Pools on watchlist: 46.

| group | n | win | avg | CI | P&L $ |
|---|---|---|---|---|---|
| research-picked | 17 | 29% | -26.4% | -58 to 8 | -451 |
| momentum, not picked | 2731 | 12% | -66.0% | -68 to -64 | -180484 |
| all momentum | 2748 | 12% | -65.8% | -68 to -64 | -180934 |
| control | 3474 | 6% | -19.1% | -20 to -18 | -66607 |
| dip buy | 36 | 28% | -12.3% | -32 to 7 | -446 |
| proven pools | 114 | 33% | -34.3% | -43 to -25 | -3925 |

What-if exit rules on the SAME trades. Cells: avg return (trades, win rate).

| exit rule | momentum | control | dip | proven |
|---|---|---|---|---|
| base_sl30_tp100 | -66% (2727, 12%) | -19% (3474, 6%) | -12% (36, 28%) | -34% (114, 33%) |
| wide_sl50_tp100 | -66% (2727, 13%) | -19% (3474, 6%) | -15% (36, 31%) | -36% (114, 33%) |
| sl30_tp50 | -67% (2727, 14%) | -19% (3474, 7%) | -18% (36, 31%) | -34% (114, 34%) |
| sl50_tp50 | -67% (2727, 16%) | -19% (3474, 7%) | -19% (36, 36%) | -36% (114, 34%) |
| no_stop_tp100 | -66% (2727, 14%) | -20% (3474, 6%) | -13% (36, 31%) | -36% (114, 33%) |

Verdict: NOT ENOUGH DATA (need 30+ closed filter=1 trades and a CI above zero before believing anything).

Pools seen: 94193. Outcomes:

- missed_window: 61685
- low_liquidity: 15480
- proven_liquidity_gone: 7990
- no_momentum: 3525
- research_failed: 2738
- proven_low_volume: 1247
- simulated failed buy: 1157
- proven_price_collapsed_or_parabolic: 146
- proven: 114
- proven_no_uptrend: 58
- dip: 36
- research_passed: 17

Warning: 738 judged pools had an unreadable mint/freeze value. Check mint_raw / freeze_raw in candidates.csv; the parsing may need fixing.
