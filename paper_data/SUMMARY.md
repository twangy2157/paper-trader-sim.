# Paper trader summary

SIMULATION ONLY. No real trades.

Updated 2026-11-17T06:06:54Z. Bankroll cash (research-selected trades): 549.3536238229275. Open positions: 25. Pools on watchlist: 50.

| group | n | win | avg | CI | P&L $ |
|---|---|---|---|---|---|
| research-picked | 17 | 29% | -26.4% | -58 to 8 | -451 |
| momentum, not picked | 2799 | 12% | -66.1% | -68 to -64 | -185326 |
| all momentum | 2816 | 12% | -65.9% | -68 to -64 | -185776 |
| control | 3545 | 6% | -19.0% | -20 to -18 | -67649 |
| dip buy | 36 | 28% | -12.3% | -32 to 7 | -446 |
| proven pools | 115 | 33% | -34.2% | -44 to -25 | -3949 |

What-if exit rules on the SAME trades. Cells: avg return (trades, win rate).

| exit rule | momentum | control | dip | proven |
|---|---|---|---|---|
| base_sl30_tp100 | -66% (2795, 12%) | -19% (3545, 6%) | -12% (36, 28%) | -34% (115, 33%) |
| wide_sl50_tp100 | -66% (2795, 13%) | -19% (3545, 6%) | -15% (36, 31%) | -36% (115, 33%) |
| sl30_tp50 | -67% (2795, 14%) | -19% (3545, 7%) | -18% (36, 31%) | -34% (115, 34%) |
| sl50_tp50 | -67% (2795, 15%) | -19% (3545, 7%) | -19% (36, 36%) | -35% (115, 34%) |
| no_stop_tp100 | -66% (2795, 14%) | -19% (3545, 6%) | -13% (36, 31%) | -36% (115, 33%) |

Verdict: NOT ENOUGH DATA (need 30+ closed filter=1 trades and a CI above zero before believing anything).

Pools seen: 96008. Outcomes:

- missed_window: 62775
- low_liquidity: 15837
- proven_liquidity_gone: 8162
- no_momentum: 3604
- research_failed: 2808
- proven_low_volume: 1262
- simulated failed buy: 1185
- proven_price_collapsed_or_parabolic: 147
- proven: 116
- proven_no_uptrend: 59
- dip: 36
- research_passed: 17

Warning: 756 judged pools had an unreadable mint/freeze value. Check mint_raw / freeze_raw in candidates.csv; the parsing may need fixing.
