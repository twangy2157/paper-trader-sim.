# Paper trader summary

SIMULATION ONLY. No real trades.

Updated 2026-11-13T01:21:11Z. Bankroll cash (research-selected trades): 456.400154541351. Open positions: 5. Pools on watchlist: 85.

| group | n | win | avg | CI | P&L $ |
|---|---|---|---|---|---|
| research-picked | 16 | 25% | -33.9% | -64 to -3 | -544 |
| momentum, not picked | 2029 | 12% | -64.7% | -67 to -62 | -131504 |
| all momentum | 2045 | 12% | -64.5% | -67 to -62 | -132047 |
| control | 2802 | 6% | -17.8% | -19 to -16 | -50060 |
| dip buy | 29 | 24% | -20.4% | -41 to 2 | -593 |
| proven pools | 99 | 33% | -32.9% | -43 to -22 | -3268 |

What-if exit rules on the SAME trades. Cells: avg return (trades, win rate).

| exit rule | momentum | control | dip | proven |
|---|---|---|---|---|
| base_sl30_tp100 | -65% (2024, 12%) | -18% (2802, 6%) | -20% (29, 24%) | -33% (99, 33%) |
| wide_sl50_tp100 | -65% (2024, 13%) | -18% (2802, 6%) | -24% (29, 28%) | -34% (99, 33%) |
| sl30_tp50 | -66% (2024, 15%) | -18% (2802, 6%) | -25% (29, 28%) | -33% (99, 34%) |
| sl50_tp50 | -66% (2024, 16%) | -18% (2802, 7%) | -28% (29, 31%) | -34% (99, 34%) |
| no_stop_tp100 | -65% (2024, 14%) | -18% (2802, 6%) | -22% (29, 28%) | -35% (99, 33%) |

Verdict: NOT ENOUGH DATA (need 30+ closed filter=1 trades and a CI above zero before believing anything).

Pools seen: 71674. Outcomes:

- missed_window: 47236
- low_liquidity: 11575
- proven_liquidity_gone: 5725
- no_momentum: 2848
- research_failed: 2031
- proven_low_volume: 1060
- simulated failed buy: 891
- proven_price_collapsed_or_parabolic: 121
- proven: 100
- proven_no_uptrend: 42
- dip: 29
- research_passed: 16

Warning: 587 judged pools had an unreadable mint/freeze value. Check mint_raw / freeze_raw in candidates.csv; the parsing may need fixing.
