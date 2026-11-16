# Paper trader summary

SIMULATION ONLY. No real trades.

Updated 2026-11-16T14:17:51Z. Bankroll cash (research-selected trades): 549.3536238229275. Open positions: 27. Pools on watchlist: 56.

| group | n | win | avg | CI | P&L $ |
|---|---|---|---|---|---|
| research-picked | 17 | 29% | -26.4% | -58 to 8 | -451 |
| momentum, not picked | 2707 | 12% | -66.0% | -68 to -64 | -179017 |
| all momentum | 2724 | 12% | -65.8% | -68 to -64 | -179468 |
| control | 3432 | 6% | -19.0% | -20 to -18 | -65506 |
| dip buy | 35 | 29% | -12.5% | -31 to 8 | -440 |
| proven pools | 114 | 33% | -34.3% | -43 to -25 | -3925 |

What-if exit rules on the SAME trades. Cells: avg return (trades, win rate).

| exit rule | momentum | control | dip | proven |
|---|---|---|---|---|
| base_sl30_tp100 | -66% (2703, 12%) | -19% (3432, 6%) | -13% (35, 29%) | -34% (114, 33%) |
| wide_sl50_tp100 | -66% (2703, 13%) | -19% (3432, 6%) | -15% (35, 31%) | -36% (114, 33%) |
| sl30_tp50 | -67% (2703, 14%) | -19% (3432, 7%) | -18% (35, 31%) | -34% (114, 34%) |
| sl50_tp50 | -67% (2703, 15%) | -19% (3432, 7%) | -19% (35, 37%) | -36% (114, 34%) |
| no_stop_tp100 | -66% (2703, 14%) | -19% (3432, 6%) | -13% (35, 31%) | -36% (114, 33%) |

Verdict: NOT ENOUGH DATA (need 30+ closed filter=1 trades and a CI above zero before believing anything).

Pools seen: 93399. Outcomes:

- missed_window: 61205
- low_liquidity: 15335
- proven_liquidity_gone: 7893
- no_momentum: 3489
- research_failed: 2720
- proven_low_volume: 1241
- simulated failed buy: 1146
- proven_price_collapsed_or_parabolic: 145
- proven: 114
- proven_no_uptrend: 58
- dip: 36
- research_passed: 17

Warning: 733 judged pools had an unreadable mint/freeze value. Check mint_raw / freeze_raw in candidates.csv; the parsing may need fixing.
