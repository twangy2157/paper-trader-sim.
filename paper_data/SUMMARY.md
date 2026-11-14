# Paper trader summary

SIMULATION ONLY. No real trades.

Updated 2026-11-14T06:22:36Z. Bankroll cash (research-selected trades): 456.400154541351. Open positions: 20. Pools on watchlist: 39.

| group | n | win | avg | CI | P&L $ |
|---|---|---|---|---|---|
| research-picked | 16 | 25% | -33.9% | -64 to -3 | -544 |
| momentum, not picked | 2259 | 12% | -64.6% | -67 to -62 | -146220 |
| all momentum | 2275 | 12% | -64.4% | -67 to -62 | -146764 |
| control | 3006 | 6% | -18.5% | -20 to -17 | -55742 |
| dip buy | 32 | 28% | -15.4% | -37 to 5 | -493 |
| proven pools | 107 | 35% | -33.0% | -43 to -23 | -3544 |

What-if exit rules on the SAME trades. Cells: avg return (trades, win rate).

| exit rule | momentum | control | dip | proven |
|---|---|---|---|---|
| base_sl30_tp100 | -65% (2254, 12%) | -18% (3006, 6%) | -15% (32, 28%) | -33% (107, 35%) |
| wide_sl50_tp100 | -65% (2254, 14%) | -19% (3006, 6%) | -18% (32, 31%) | -34% (107, 35%) |
| sl30_tp50 | -66% (2254, 15%) | -19% (3006, 7%) | -20% (32, 31%) | -33% (107, 36%) |
| sl50_tp50 | -66% (2254, 16%) | -19% (3006, 7%) | -23% (32, 34%) | -34% (107, 36%) |
| no_stop_tp100 | -65% (2254, 14%) | -19% (3006, 6%) | -16% (32, 31%) | -35% (107, 35%) |

Verdict: NOT ENOUGH DATA (need 30+ closed filter=1 trades and a CI above zero before believing anything).

Pools seen: 79265. Outcomes:

- missed_window: 52007
- low_liquidity: 13002
- proven_liquidity_gone: 6511
- no_momentum: 3059
- research_failed: 2270
- proven_low_volume: 1105
- simulated failed buy: 981
- proven_price_collapsed_or_parabolic: 128
- proven: 107
- proven_no_uptrend: 47
- dip: 32
- research_passed: 16

Warning: 635 judged pools had an unreadable mint/freeze value. Check mint_raw / freeze_raw in candidates.csv; the parsing may need fixing.
