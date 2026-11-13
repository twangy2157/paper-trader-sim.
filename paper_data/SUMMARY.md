# Paper trader summary

SIMULATION ONLY. No real trades.

Updated 2026-11-13T03:08:31Z. Bankroll cash (research-selected trades): 456.400154541351. Open positions: 23. Pools on watchlist: 60.

| group | n | win | avg | CI | P&L $ |
|---|---|---|---|---|---|
| research-picked | 16 | 25% | -33.9% | -64 to -3 | -544 |
| momentum, not picked | 2040 | 12% | -64.7% | -67 to -62 | -132181 |
| all momentum | 2056 | 12% | -64.5% | -67 to -62 | -132724 |
| control | 2808 | 6% | -17.8% | -19 to -17 | -50233 |
| dip buy | 29 | 24% | -20.4% | -41 to 2 | -593 |
| proven pools | 100 | 33% | -33.6% | -43 to -23 | -3368 |

What-if exit rules on the SAME trades. Cells: avg return (trades, win rate).

| exit rule | momentum | control | dip | proven |
|---|---|---|---|---|
| base_sl30_tp100 | -65% (2035, 12%) | -18% (2808, 6%) | -20% (29, 24%) | -34% (100, 33%) |
| wide_sl50_tp100 | -65% (2035, 13%) | -18% (2808, 6%) | -24% (29, 28%) | -35% (100, 33%) |
| sl30_tp50 | -66% (2035, 15%) | -18% (2808, 6%) | -25% (29, 28%) | -33% (100, 34%) |
| sl50_tp50 | -66% (2035, 16%) | -18% (2808, 7%) | -28% (29, 31%) | -35% (100, 34%) |
| no_stop_tp100 | -65% (2035, 14%) | -18% (2808, 6%) | -22% (29, 28%) | -36% (100, 33%) |

Verdict: NOT ENOUGH DATA (need 30+ closed filter=1 trades and a CI above zero before believing anything).

Pools seen: 72196. Outcomes:

- missed_window: 47564
- low_liquidity: 11676
- proven_liquidity_gone: 5772
- no_momentum: 2861
- research_failed: 2051
- proven_low_volume: 1062
- simulated failed buy: 899
- proven_price_collapsed_or_parabolic: 121
- proven: 103
- proven_no_uptrend: 42
- dip: 29
- research_passed: 16

Warning: 591 judged pools had an unreadable mint/freeze value. Check mint_raw / freeze_raw in candidates.csv; the parsing may need fixing.
