# Paper trader summary

SIMULATION ONLY. No real trades.

Updated 2026-11-13T14:13:20Z. Bankroll cash (research-selected trades): 456.400154541351. Open positions: 21. Pools on watchlist: 29.

| group | n | win | avg | CI | P&L $ |
|---|---|---|---|---|---|
| research-picked | 16 | 25% | -33.9% | -64 to -3 | -544 |
| momentum, not picked | 2138 | 12% | -64.4% | -67 to -62 | -137939 |
| all momentum | 2154 | 12% | -64.2% | -67 to -62 | -138483 |
| control | 2887 | 6% | -18.0% | -19 to -17 | -52354 |
| dip buy | 30 | 23% | -19.9% | -41 to 0 | -599 |
| proven pools | 103 | 35% | -32.5% | -42 to -23 | -3359 |

What-if exit rules on the SAME trades. Cells: avg return (trades, win rate).

| exit rule | momentum | control | dip | proven |
|---|---|---|---|---|
| base_sl30_tp100 | -64% (2133, 12%) | -18% (2887, 6%) | -20% (30, 23%) | -33% (103, 35%) |
| wide_sl50_tp100 | -65% (2133, 14%) | -18% (2887, 6%) | -23% (30, 27%) | -34% (103, 35%) |
| sl30_tp50 | -66% (2133, 15%) | -18% (2887, 7%) | -24% (30, 27%) | -32% (103, 36%) |
| sl50_tp50 | -66% (2133, 16%) | -19% (2887, 7%) | -27% (30, 30%) | -34% (103, 36%) |
| no_stop_tp100 | -65% (2133, 14%) | -19% (2887, 6%) | -21% (30, 27%) | -35% (103, 35%) |

Verdict: NOT ENOUGH DATA (need 30+ closed filter=1 trades and a CI above zero before believing anything).

Pools seen: 75070. Outcomes:

- missed_window: 49457
- low_liquidity: 12114
- proven_liquidity_gone: 6077
- no_momentum: 2941
- research_failed: 2147
- proven_low_volume: 1078
- simulated failed buy: 937
- proven_price_collapsed_or_parabolic: 125
- proven: 104
- proven_no_uptrend: 43
- dip: 31
- research_passed: 16

Warning: 611 judged pools had an unreadable mint/freeze value. Check mint_raw / freeze_raw in candidates.csv; the parsing may need fixing.
