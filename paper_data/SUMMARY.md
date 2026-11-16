# Paper trader summary

SIMULATION ONLY. No real trades.

Updated 2026-11-16T05:20:41Z. Bankroll cash (research-selected trades): 456.400154541351. Open positions: 12. Pools on watchlist: 51.

| group | n | win | avg | CI | P&L $ |
|---|---|---|---|---|---|
| research-picked | 16 | 25% | -33.9% | -64 to -3 | -544 |
| momentum, not picked | 2641 | 12% | -66.0% | -68 to -64 | -174421 |
| all momentum | 2657 | 12% | -65.8% | -68 to -63 | -174965 |
| control | 3372 | 6% | -18.8% | -20 to -18 | -63813 |
| dip buy | 35 | 29% | -12.5% | -31 to 8 | -440 |
| proven pools | 113 | 34% | -33.8% | -43 to -24 | -3825 |

What-if exit rules on the SAME trades. Cells: avg return (trades, win rate).

| exit rule | momentum | control | dip | proven |
|---|---|---|---|---|
| base_sl30_tp100 | -66% (2636, 12%) | -19% (3372, 6%) | -13% (35, 29%) | -34% (113, 34%) |
| wide_sl50_tp100 | -66% (2636, 13%) | -19% (3372, 6%) | -15% (35, 31%) | -35% (113, 34%) |
| sl30_tp50 | -67% (2636, 14%) | -19% (3372, 7%) | -18% (35, 31%) | -34% (113, 35%) |
| sl50_tp50 | -67% (2636, 16%) | -19% (3372, 7%) | -19% (35, 37%) | -35% (113, 35%) |
| no_stop_tp100 | -66% (2636, 14%) | -19% (3372, 6%) | -13% (35, 31%) | -36% (113, 34%) |

Verdict: NOT ENOUGH DATA (need 30+ closed filter=1 trades and a CI above zero before believing anything).

Pools seen: 91614. Outcomes:

- missed_window: 60096
- low_liquidity: 15041
- proven_liquidity_gone: 7700
- no_momentum: 3422
- research_failed: 2646
- proven_low_volume: 1214
- simulated failed buy: 1129
- proven_price_collapsed_or_parabolic: 143
- proven: 114
- proven_no_uptrend: 58
- dip: 35
- research_passed: 16

Warning: 721 judged pools had an unreadable mint/freeze value. Check mint_raw / freeze_raw in candidates.csv; the parsing may need fixing.
