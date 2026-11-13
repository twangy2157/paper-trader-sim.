# Paper trader summary

SIMULATION ONLY. No real trades.

Updated 2026-11-13T12:46:56Z. Bankroll cash (research-selected trades): 456.400154541351. Open positions: 14. Pools on watchlist: 43.

| group | n | win | avg | CI | P&L $ |
|---|---|---|---|---|---|
| research-picked | 16 | 25% | -33.9% | -64 to -3 | -544 |
| momentum, not picked | 2134 | 12% | -64.5% | -67 to -62 | -137776 |
| all momentum | 2150 | 12% | -64.2% | -67 to -62 | -138320 |
| control | 2876 | 6% | -18.0% | -19 to -17 | -52086 |
| dip buy | 30 | 23% | -19.9% | -41 to 0 | -599 |
| proven pools | 103 | 35% | -32.5% | -42 to -23 | -3359 |

What-if exit rules on the SAME trades. Cells: avg return (trades, win rate).

| exit rule | momentum | control | dip | proven |
|---|---|---|---|---|
| base_sl30_tp100 | -65% (2129, 12%) | -18% (2876, 6%) | -20% (30, 23%) | -33% (103, 35%) |
| wide_sl50_tp100 | -65% (2129, 13%) | -18% (2876, 6%) | -23% (30, 27%) | -34% (103, 35%) |
| sl30_tp50 | -66% (2129, 15%) | -18% (2876, 7%) | -24% (30, 27%) | -32% (103, 36%) |
| sl50_tp50 | -66% (2129, 16%) | -19% (2876, 7%) | -27% (30, 30%) | -34% (103, 36%) |
| no_stop_tp100 | -65% (2129, 14%) | -19% (2876, 6%) | -21% (30, 27%) | -35% (103, 35%) |

Verdict: NOT ENOUGH DATA (need 30+ closed filter=1 trades and a CI above zero before believing anything).

Pools seen: 74731. Outcomes:

- missed_window: 49250
- low_liquidity: 12048
- proven_liquidity_gone: 6046
- no_momentum: 2931
- research_failed: 2136
- proven_low_volume: 1075
- simulated failed buy: 930
- proven_price_collapsed_or_parabolic: 123
- proven: 104
- proven_no_uptrend: 42
- dip: 30
- research_passed: 16

Warning: 607 judged pools had an unreadable mint/freeze value. Check mint_raw / freeze_raw in candidates.csv; the parsing may need fixing.
