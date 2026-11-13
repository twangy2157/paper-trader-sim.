# Paper trader summary

SIMULATION ONLY. No real trades.

Updated 2026-11-13T13:42:13Z. Bankroll cash (research-selected trades): 456.400154541351. Open positions: 13. Pools on watchlist: 54.

| group | n | win | avg | CI | P&L $ |
|---|---|---|---|---|---|
| research-picked | 16 | 25% | -33.9% | -64 to -3 | -544 |
| momentum, not picked | 2136 | 12% | -64.5% | -67 to -62 | -137923 |
| all momentum | 2152 | 12% | -64.3% | -67 to -62 | -138466 |
| control | 2886 | 6% | -18.0% | -19 to -17 | -52343 |
| dip buy | 30 | 23% | -19.9% | -41 to 0 | -599 |
| proven pools | 103 | 35% | -32.5% | -42 to -23 | -3359 |

What-if exit rules on the SAME trades. Cells: avg return (trades, win rate).

| exit rule | momentum | control | dip | proven |
|---|---|---|---|---|
| base_sl30_tp100 | -65% (2131, 12%) | -18% (2886, 6%) | -20% (30, 23%) | -33% (103, 35%) |
| wide_sl50_tp100 | -65% (2131, 13%) | -18% (2886, 6%) | -23% (30, 27%) | -34% (103, 35%) |
| sl30_tp50 | -66% (2131, 15%) | -18% (2886, 7%) | -24% (30, 27%) | -32% (103, 36%) |
| sl50_tp50 | -66% (2131, 16%) | -19% (2886, 7%) | -27% (30, 30%) | -34% (103, 36%) |
| no_stop_tp100 | -65% (2131, 14%) | -19% (2886, 6%) | -21% (30, 27%) | -35% (103, 35%) |

Verdict: NOT ENOUGH DATA (need 30+ closed filter=1 trades and a CI above zero before believing anything).

Pools seen: 74911. Outcomes:

- missed_window: 49365
- low_liquidity: 12078
- proven_liquidity_gone: 6060
- no_momentum: 2935
- research_failed: 2142
- proven_low_volume: 1078
- simulated failed buy: 934
- proven_price_collapsed_or_parabolic: 125
- proven: 104
- proven_no_uptrend: 43
- dip: 31
- research_passed: 16

Warning: 609 judged pools had an unreadable mint/freeze value. Check mint_raw / freeze_raw in candidates.csv; the parsing may need fixing.
