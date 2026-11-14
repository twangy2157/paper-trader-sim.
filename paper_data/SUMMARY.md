# Paper trader summary

SIMULATION ONLY. No real trades.

Updated 2026-11-14T08:50:54Z. Bankroll cash (research-selected trades): 456.400154541351. Open positions: 18. Pools on watchlist: 53.

| group | n | win | avg | CI | P&L $ |
|---|---|---|---|---|---|
| research-picked | 16 | 25% | -33.9% | -64 to -3 | -544 |
| momentum, not picked | 2278 | 12% | -64.7% | -67 to -62 | -147650 |
| all momentum | 2294 | 12% | -64.5% | -67 to -62 | -148193 |
| control | 3025 | 6% | -18.4% | -20 to -17 | -56059 |
| dip buy | 32 | 28% | -15.4% | -37 to 5 | -493 |
| proven pools | 107 | 35% | -33.0% | -43 to -23 | -3544 |

What-if exit rules on the SAME trades. Cells: avg return (trades, win rate).

| exit rule | momentum | control | dip | proven |
|---|---|---|---|---|
| base_sl30_tp100 | -65% (2273, 12%) | -18% (3025, 6%) | -15% (32, 28%) | -33% (107, 35%) |
| wide_sl50_tp100 | -65% (2273, 14%) | -19% (3025, 6%) | -18% (32, 31%) | -34% (107, 35%) |
| sl30_tp50 | -66% (2273, 15%) | -19% (3025, 7%) | -20% (32, 31%) | -33% (107, 36%) |
| sl50_tp50 | -66% (2273, 16%) | -19% (3025, 7%) | -23% (32, 34%) | -34% (107, 36%) |
| no_stop_tp100 | -65% (2273, 14%) | -19% (3025, 6%) | -16% (32, 31%) | -35% (107, 35%) |

Verdict: NOT ENOUGH DATA (need 30+ closed filter=1 trades and a CI above zero before believing anything).

Pools seen: 79771. Outcomes:

- missed_window: 52296
- low_liquidity: 13114
- proven_liquidity_gone: 6573
- no_momentum: 3078
- research_failed: 2287
- proven_low_volume: 1107
- simulated failed buy: 985
- proven_price_collapsed_or_parabolic: 129
- proven: 107
- proven_no_uptrend: 47
- dip: 32
- research_passed: 16

Warning: 638 judged pools had an unreadable mint/freeze value. Check mint_raw / freeze_raw in candidates.csv; the parsing may need fixing.
