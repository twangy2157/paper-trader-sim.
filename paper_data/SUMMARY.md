# Paper trader summary

SIMULATION ONLY. No real trades.

Updated 2026-11-13T08:51:42Z. Bankroll cash (research-selected trades): 456.400154541351. Open positions: 25. Pools on watchlist: 41.

| group | n | win | avg | CI | P&L $ |
|---|---|---|---|---|---|
| research-picked | 16 | 25% | -33.9% | -64 to -3 | -544 |
| momentum, not picked | 2085 | 12% | -64.8% | -67 to -62 | -135242 |
| all momentum | 2101 | 12% | -64.5% | -67 to -62 | -135785 |
| control | 2844 | 6% | -18.0% | -19 to -17 | -51318 |
| dip buy | 30 | 23% | -19.9% | -41 to 0 | -599 |
| proven pools | 103 | 35% | -32.5% | -42 to -23 | -3358 |

What-if exit rules on the SAME trades. Cells: avg return (trades, win rate).

| exit rule | momentum | control | dip | proven |
|---|---|---|---|---|
| base_sl30_tp100 | -65% (2080, 12%) | -18% (2844, 6%) | -20% (30, 23%) | -33% (103, 35%) |
| wide_sl50_tp100 | -65% (2080, 13%) | -18% (2844, 6%) | -23% (30, 27%) | -34% (103, 35%) |
| sl30_tp50 | -66% (2080, 15%) | -18% (2844, 7%) | -24% (30, 27%) | -32% (103, 36%) |
| sl50_tp50 | -66% (2080, 16%) | -19% (2844, 7%) | -27% (30, 30%) | -34% (103, 36%) |
| no_stop_tp100 | -65% (2080, 14%) | -18% (2844, 6%) | -21% (30, 27%) | -35% (103, 35%) |

Verdict: NOT ENOUGH DATA (need 30+ closed filter=1 trades and a CI above zero before believing anything).

Pools seen: 73760. Outcomes:

- missed_window: 48627
- low_liquidity: 11900
- proven_liquidity_gone: 5936
- no_momentum: 2900
- research_failed: 2098
- proven_low_volume: 1068
- simulated failed buy: 917
- proven_price_collapsed_or_parabolic: 123
- proven: 103
- proven_no_uptrend: 42
- dip: 30
- research_passed: 16

Warning: 599 judged pools had an unreadable mint/freeze value. Check mint_raw / freeze_raw in candidates.csv; the parsing may need fixing.
