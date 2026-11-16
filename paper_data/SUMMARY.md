# Paper trader summary

SIMULATION ONLY. No real trades.

Updated 2026-11-16T04:16:27Z. Bankroll cash (research-selected trades): 456.400154541351. Open positions: 11. Pools on watchlist: 30.

| group | n | win | avg | CI | P&L $ |
|---|---|---|---|---|---|
| research-picked | 16 | 25% | -33.9% | -64 to -3 | -544 |
| momentum, not picked | 2637 | 12% | -66.0% | -68 to -64 | -174193 |
| all momentum | 2653 | 12% | -65.8% | -68 to -64 | -174736 |
| control | 3366 | 6% | -18.8% | -20 to -18 | -63506 |
| dip buy | 35 | 29% | -12.5% | -31 to 8 | -440 |
| proven pools | 113 | 34% | -33.8% | -43 to -24 | -3825 |

What-if exit rules on the SAME trades. Cells: avg return (trades, win rate).

| exit rule | momentum | control | dip | proven |
|---|---|---|---|---|
| base_sl30_tp100 | -66% (2632, 12%) | -19% (3366, 6%) | -13% (35, 29%) | -34% (113, 34%) |
| wide_sl50_tp100 | -66% (2632, 13%) | -19% (3366, 6%) | -15% (35, 31%) | -35% (113, 34%) |
| sl30_tp50 | -67% (2632, 14%) | -19% (3366, 7%) | -18% (35, 31%) | -34% (113, 35%) |
| sl50_tp50 | -67% (2632, 16%) | -19% (3366, 7%) | -19% (35, 37%) | -35% (113, 35%) |
| no_stop_tp100 | -66% (2632, 14%) | -19% (3366, 6%) | -13% (35, 31%) | -36% (113, 34%) |

Verdict: NOT ENOUGH DATA (need 30+ closed filter=1 trades and a CI above zero before believing anything).

Pools seen: 91398. Outcomes:

- missed_window: 59963
- low_liquidity: 15002
- proven_liquidity_gone: 7671
- no_momentum: 3416
- research_failed: 2641
- proven_low_volume: 1211
- simulated failed buy: 1128
- proven_price_collapsed_or_parabolic: 143
- proven: 114
- proven_no_uptrend: 58
- dip: 35
- research_passed: 16

Warning: 720 judged pools had an unreadable mint/freeze value. Check mint_raw / freeze_raw in candidates.csv; the parsing may need fixing.
