# Paper trader summary

SIMULATION ONLY. No real trades.

Updated 2026-11-13T04:45:39Z. Bankroll cash (research-selected trades): 456.400154541351. Open positions: 20. Pools on watchlist: 51.

| group | n | win | avg | CI | P&L $ |
|---|---|---|---|---|---|
| research-picked | 16 | 25% | -33.9% | -64 to -3 | -544 |
| momentum, not picked | 2056 | 12% | -64.8% | -67 to -62 | -133426 |
| all momentum | 2072 | 12% | -64.6% | -67 to -62 | -133969 |
| control | 2820 | 6% | -17.9% | -19 to -17 | -50675 |
| dip buy | 29 | 24% | -20.4% | -41 to 2 | -593 |
| proven pools | 101 | 34% | -33.2% | -43 to -23 | -3367 |

What-if exit rules on the SAME trades. Cells: avg return (trades, win rate).

| exit rule | momentum | control | dip | proven |
|---|---|---|---|---|
| base_sl30_tp100 | -65% (2051, 12%) | -18% (2820, 6%) | -20% (29, 24%) | -33% (101, 34%) |
| wide_sl50_tp100 | -65% (2051, 13%) | -18% (2820, 6%) | -24% (29, 28%) | -35% (101, 34%) |
| sl30_tp50 | -66% (2051, 15%) | -18% (2820, 6%) | -25% (29, 28%) | -33% (101, 35%) |
| sl50_tp50 | -66% (2051, 16%) | -18% (2820, 7%) | -28% (29, 31%) | -35% (101, 35%) |
| no_stop_tp100 | -65% (2051, 14%) | -18% (2820, 6%) | -22% (29, 28%) | -36% (101, 34%) |

Verdict: NOT ENOUGH DATA (need 30+ closed filter=1 trades and a CI above zero before believing anything).

Pools seen: 72710. Outcomes:

- missed_window: 47929
- low_liquidity: 11741
- proven_liquidity_gone: 5822
- no_momentum: 2875
- research_failed: 2063
- proven_low_volume: 1065
- simulated failed buy: 904
- proven_price_collapsed_or_parabolic: 121
- proven: 103
- proven_no_uptrend: 42
- dip: 29
- research_passed: 16

Warning: 594 judged pools had an unreadable mint/freeze value. Check mint_raw / freeze_raw in candidates.csv; the parsing may need fixing.
