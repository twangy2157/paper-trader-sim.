# Paper trader summary

SIMULATION ONLY. No real trades.

Updated 2026-11-16T01:36:38Z. Bankroll cash (research-selected trades): 456.400154541351. Open positions: 0. Pools on watchlist: 43.

| group | n | win | avg | CI | P&L $ |
|---|---|---|---|---|---|
| research-picked | 16 | 25% | -33.9% | -64 to -3 | -544 |
| momentum, not picked | 2614 | 12% | -66.0% | -68 to -64 | -172698 |
| all momentum | 2630 | 12% | -65.8% | -68 to -64 | -173242 |
| control | 3348 | 6% | -18.7% | -20 to -18 | -62920 |
| dip buy | 35 | 29% | -12.5% | -31 to 8 | -440 |
| proven pools | 113 | 34% | -33.8% | -43 to -24 | -3825 |

What-if exit rules on the SAME trades. Cells: avg return (trades, win rate).

| exit rule | momentum | control | dip | proven |
|---|---|---|---|---|
| base_sl30_tp100 | -66% (2609, 12%) | -19% (3348, 6%) | -13% (35, 29%) | -34% (113, 34%) |
| wide_sl50_tp100 | -66% (2609, 13%) | -19% (3348, 6%) | -15% (35, 31%) | -35% (113, 34%) |
| sl30_tp50 | -67% (2609, 14%) | -19% (3348, 7%) | -18% (35, 31%) | -34% (113, 35%) |
| sl50_tp50 | -67% (2609, 16%) | -19% (3348, 7%) | -19% (35, 37%) | -35% (113, 35%) |
| no_stop_tp100 | -66% (2609, 14%) | -19% (3348, 6%) | -13% (35, 31%) | -36% (113, 34%) |

Verdict: NOT ENOUGH DATA (need 30+ closed filter=1 trades and a CI above zero before believing anything).

Pools seen: 90713. Outcomes:

- missed_window: 59504
- low_liquidity: 14905
- proven_liquidity_gone: 7614
- no_momentum: 3392
- research_failed: 2614
- proven_low_volume: 1204
- simulated failed buy: 1120
- proven_price_collapsed_or_parabolic: 138
- proven: 113
- proven_no_uptrend: 58
- dip: 35
- research_passed: 16

Warning: 716 judged pools had an unreadable mint/freeze value. Check mint_raw / freeze_raw in candidates.csv; the parsing may need fixing.
