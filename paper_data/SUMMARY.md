# Paper trader summary

SIMULATION ONLY. No real trades.

Updated 2026-11-16T05:42:06Z. Bankroll cash (research-selected trades): 456.400154541351. Open positions: 12. Pools on watchlist: 45.

| group | n | win | avg | CI | P&L $ |
|---|---|---|---|---|---|
| research-picked | 16 | 25% | -33.9% | -64 to -3 | -544 |
| momentum, not picked | 2642 | 12% | -65.9% | -68 to -64 | -174430 |
| all momentum | 2658 | 12% | -65.7% | -68 to -64 | -174973 |
| control | 3375 | 6% | -18.8% | -20 to -18 | -63910 |
| dip buy | 35 | 29% | -12.5% | -31 to 8 | -440 |
| proven pools | 113 | 34% | -33.8% | -43 to -24 | -3825 |

What-if exit rules on the SAME trades. Cells: avg return (trades, win rate).

| exit rule | momentum | control | dip | proven |
|---|---|---|---|---|
| base_sl30_tp100 | -66% (2637, 12%) | -19% (3375, 6%) | -13% (35, 29%) | -34% (113, 34%) |
| wide_sl50_tp100 | -66% (2637, 13%) | -19% (3375, 6%) | -15% (35, 31%) | -35% (113, 34%) |
| sl30_tp50 | -67% (2637, 14%) | -19% (3375, 7%) | -18% (35, 31%) | -34% (113, 35%) |
| sl50_tp50 | -67% (2637, 16%) | -19% (3375, 7%) | -19% (35, 37%) | -35% (113, 35%) |
| no_stop_tp100 | -66% (2637, 14%) | -19% (3375, 6%) | -13% (35, 31%) | -36% (113, 34%) |

Verdict: NOT ENOUGH DATA (need 30+ closed filter=1 trades and a CI above zero before believing anything).

Pools seen: 91698. Outcomes:

- missed_window: 60155
- low_liquidity: 15052
- proven_liquidity_gone: 7709
- no_momentum: 3423
- research_failed: 2649
- proven_low_volume: 1215
- simulated failed buy: 1129
- proven_price_collapsed_or_parabolic: 143
- proven: 114
- proven_no_uptrend: 58
- dip: 35
- research_passed: 16

Warning: 721 judged pools had an unreadable mint/freeze value. Check mint_raw / freeze_raw in candidates.csv; the parsing may need fixing.
