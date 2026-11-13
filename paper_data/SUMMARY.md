# Paper trader summary

SIMULATION ONLY. No real trades.

Updated 2026-11-13T11:52:32Z. Bankroll cash (research-selected trades): 456.400154541351. Open positions: 28. Pools on watchlist: 49.

| group | n | win | avg | CI | P&L $ |
|---|---|---|---|---|---|
| research-picked | 16 | 25% | -33.9% | -64 to -3 | -544 |
| momentum, not picked | 2119 | 12% | -64.6% | -67 to -62 | -137166 |
| all momentum | 2135 | 12% | -64.4% | -67 to -62 | -137709 |
| control | 2866 | 6% | -18.1% | -19 to -17 | -52012 |
| dip buy | 30 | 23% | -19.9% | -41 to 0 | -599 |
| proven pools | 103 | 35% | -32.5% | -42 to -23 | -3359 |

What-if exit rules on the SAME trades. Cells: avg return (trades, win rate).

| exit rule | momentum | control | dip | proven |
|---|---|---|---|---|
| base_sl30_tp100 | -65% (2114, 12%) | -18% (2866, 6%) | -20% (30, 23%) | -33% (103, 35%) |
| wide_sl50_tp100 | -65% (2114, 13%) | -18% (2866, 6%) | -23% (30, 27%) | -34% (103, 35%) |
| sl30_tp50 | -66% (2114, 15%) | -18% (2866, 7%) | -24% (30, 27%) | -32% (103, 36%) |
| sl50_tp50 | -66% (2114, 16%) | -19% (2866, 7%) | -27% (30, 30%) | -34% (103, 36%) |
| no_stop_tp100 | -65% (2114, 14%) | -19% (2866, 6%) | -21% (30, 27%) | -35% (103, 35%) |

Verdict: NOT ENOUGH DATA (need 30+ closed filter=1 trades and a CI above zero before believing anything).

Pools seen: 74502. Outcomes:

- missed_window: 49093
- low_liquidity: 12021
- proven_liquidity_gone: 6016
- no_momentum: 2923
- research_failed: 2134
- proven_low_volume: 1074
- simulated failed buy: 927
- proven_price_collapsed_or_parabolic: 123
- proven: 103
- proven_no_uptrend: 42
- dip: 30
- research_passed: 16

Warning: 604 judged pools had an unreadable mint/freeze value. Check mint_raw / freeze_raw in candidates.csv; the parsing may need fixing.
