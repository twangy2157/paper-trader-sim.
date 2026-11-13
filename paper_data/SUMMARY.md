# Paper trader summary

SIMULATION ONLY. No real trades.

Updated 2026-11-13T00:30:15Z. Bankroll cash (research-selected trades): 456.400154541351. Open positions: 18. Pools on watchlist: 52.

| group | n | win | avg | CI | P&L $ |
|---|---|---|---|---|---|
| research-picked | 16 | 25% | -33.9% | -64 to -3 | -544 |
| momentum, not picked | 2023 | 12% | -64.8% | -67 to -62 | -131245 |
| all momentum | 2039 | 12% | -64.5% | -67 to -62 | -131788 |
| control | 2795 | 6% | -17.8% | -19 to -16 | -49985 |
| dip buy | 29 | 24% | -20.4% | -41 to 2 | -593 |
| proven pools | 97 | 34% | -31.8% | -42 to -21 | -3092 |

What-if exit rules on the SAME trades. Cells: avg return (trades, win rate).

| exit rule | momentum | control | dip | proven |
|---|---|---|---|---|
| base_sl30_tp100 | -65% (2018, 12%) | -18% (2795, 6%) | -20% (29, 24%) | -32% (97, 34%) |
| wide_sl50_tp100 | -65% (2018, 13%) | -18% (2795, 6%) | -24% (29, 28%) | -33% (97, 34%) |
| sl30_tp50 | -66% (2018, 15%) | -18% (2795, 6%) | -25% (29, 28%) | -32% (97, 35%) |
| sl50_tp50 | -66% (2018, 16%) | -18% (2795, 7%) | -28% (29, 31%) | -33% (97, 35%) |
| no_stop_tp100 | -65% (2018, 14%) | -18% (2795, 6%) | -22% (29, 28%) | -34% (97, 34%) |

Verdict: NOT ENOUGH DATA (need 30+ closed filter=1 trades and a CI above zero before believing anything).

Pools seen: 71574. Outcomes:

- missed_window: 47156
- low_liquidity: 11570
- proven_liquidity_gone: 5714
- no_momentum: 2847
- research_failed: 2030
- proven_low_volume: 1060
- simulated failed buy: 889
- proven_price_collapsed_or_parabolic: 121
- proven: 100
- proven_no_uptrend: 42
- dip: 29
- research_passed: 16

Warning: 587 judged pools had an unreadable mint/freeze value. Check mint_raw / freeze_raw in candidates.csv; the parsing may need fixing.
