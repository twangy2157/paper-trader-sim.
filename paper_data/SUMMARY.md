# Paper trader summary

SIMULATION ONLY. No real trades.

Updated 2026-11-16T19:17:41Z. Bankroll cash (research-selected trades): 549.3536238229275. Open positions: 22. Pools on watchlist: 51.

| group | n | win | avg | CI | P&L $ |
|---|---|---|---|---|---|
| research-picked | 17 | 29% | -26.4% | -58 to 8 | -451 |
| momentum, not picked | 2738 | 12% | -65.9% | -68 to -64 | -180821 |
| all momentum | 2755 | 12% | -65.7% | -68 to -64 | -181272 |
| control | 3481 | 6% | -19.1% | -20 to -18 | -66765 |
| dip buy | 36 | 28% | -12.3% | -32 to 7 | -446 |
| proven pools | 114 | 33% | -34.3% | -43 to -25 | -3925 |

What-if exit rules on the SAME trades. Cells: avg return (trades, win rate).

| exit rule | momentum | control | dip | proven |
|---|---|---|---|---|
| base_sl30_tp100 | -66% (2734, 12%) | -19% (3481, 6%) | -12% (36, 28%) | -34% (114, 33%) |
| wide_sl50_tp100 | -66% (2734, 13%) | -19% (3481, 6%) | -15% (36, 31%) | -36% (114, 33%) |
| sl30_tp50 | -67% (2734, 14%) | -19% (3481, 7%) | -18% (36, 31%) | -34% (114, 34%) |
| sl50_tp50 | -67% (2734, 16%) | -19% (3481, 7%) | -19% (36, 36%) | -36% (114, 34%) |
| no_stop_tp100 | -66% (2734, 14%) | -20% (3481, 6%) | -13% (36, 31%) | -36% (114, 33%) |

Verdict: NOT ENOUGH DATA (need 30+ closed filter=1 trades and a CI above zero before believing anything).

Pools seen: 94421. Outcomes:

- missed_window: 61782
- low_liquidity: 15554
- proven_liquidity_gone: 8012
- no_momentum: 3535
- research_failed: 2750
- proven_low_volume: 1250
- simulated failed buy: 1166
- proven_price_collapsed_or_parabolic: 147
- proven: 114
- proven_no_uptrend: 58
- dip: 36
- research_passed: 17

Warning: 744 judged pools had an unreadable mint/freeze value. Check mint_raw / freeze_raw in candidates.csv; the parsing may need fixing.
