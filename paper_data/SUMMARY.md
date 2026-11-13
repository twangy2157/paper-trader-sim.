# Paper trader summary

SIMULATION ONLY. No real trades.

Updated 2026-11-13T01:53:12Z. Bankroll cash (research-selected trades): 456.400154541351. Open positions: 14. Pools on watchlist: 65.

| group | n | win | avg | CI | P&L $ |
|---|---|---|---|---|---|
| research-picked | 16 | 25% | -33.9% | -64 to -3 | -544 |
| momentum, not picked | 2030 | 12% | -64.7% | -67 to -62 | -131604 |
| all momentum | 2046 | 12% | -64.5% | -67 to -62 | -132148 |
| control | 2803 | 6% | -17.8% | -19 to -17 | -50068 |
| dip buy | 29 | 24% | -20.4% | -41 to 2 | -593 |
| proven pools | 99 | 33% | -32.9% | -43 to -22 | -3268 |

What-if exit rules on the SAME trades. Cells: avg return (trades, win rate).

| exit rule | momentum | control | dip | proven |
|---|---|---|---|---|
| base_sl30_tp100 | -65% (2025, 12%) | -18% (2803, 6%) | -20% (29, 24%) | -33% (99, 33%) |
| wide_sl50_tp100 | -65% (2025, 13%) | -18% (2803, 6%) | -24% (29, 28%) | -34% (99, 33%) |
| sl30_tp50 | -66% (2025, 15%) | -18% (2803, 6%) | -25% (29, 28%) | -33% (99, 34%) |
| sl50_tp50 | -66% (2025, 16%) | -18% (2803, 7%) | -28% (29, 31%) | -34% (99, 34%) |
| no_stop_tp100 | -65% (2025, 14%) | -18% (2803, 6%) | -22% (29, 28%) | -35% (99, 33%) |

Verdict: NOT ENOUGH DATA (need 30+ closed filter=1 trades and a CI above zero before believing anything).

Pools seen: 71858. Outcomes:

- missed_window: 47355
- low_liquidity: 11608
- proven_liquidity_gone: 5744
- no_momentum: 2849
- research_failed: 2039
- proven_low_volume: 1061
- simulated failed buy: 892
- proven_price_collapsed_or_parabolic: 121
- proven: 102
- proven_no_uptrend: 42
- dip: 29
- research_passed: 16

Warning: 588 judged pools had an unreadable mint/freeze value. Check mint_raw / freeze_raw in candidates.csv; the parsing may need fixing.
