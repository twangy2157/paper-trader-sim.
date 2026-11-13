# Paper trader summary

SIMULATION ONLY. No real trades.

Updated 2026-11-13T12:25:30Z. Bankroll cash (research-selected trades): 456.400154541351. Open positions: 14. Pools on watchlist: 69.

| group | n | win | avg | CI | P&L $ |
|---|---|---|---|---|---|
| research-picked | 16 | 25% | -33.9% | -64 to -3 | -544 |
| momentum, not picked | 2131 | 12% | -64.6% | -67 to -62 | -137759 |
| all momentum | 2147 | 12% | -64.3% | -67 to -62 | -138303 |
| control | 2874 | 6% | -18.0% | -19 to -17 | -52073 |
| dip buy | 30 | 23% | -19.9% | -41 to 0 | -599 |
| proven pools | 103 | 35% | -32.5% | -42 to -23 | -3359 |

What-if exit rules on the SAME trades. Cells: avg return (trades, win rate).

| exit rule | momentum | control | dip | proven |
|---|---|---|---|---|
| base_sl30_tp100 | -65% (2126, 12%) | -18% (2874, 6%) | -20% (30, 23%) | -33% (103, 35%) |
| wide_sl50_tp100 | -65% (2126, 13%) | -18% (2874, 6%) | -23% (30, 27%) | -34% (103, 35%) |
| sl30_tp50 | -66% (2126, 15%) | -18% (2874, 7%) | -24% (30, 27%) | -32% (103, 36%) |
| sl50_tp50 | -66% (2126, 16%) | -19% (2874, 7%) | -27% (30, 30%) | -34% (103, 36%) |
| no_stop_tp100 | -65% (2126, 14%) | -19% (2874, 6%) | -21% (30, 27%) | -35% (103, 35%) |

Verdict: NOT ENOUGH DATA (need 30+ closed filter=1 trades and a CI above zero before believing anything).

Pools seen: 74630. Outcomes:

- missed_window: 49186
- low_liquidity: 12030
- proven_liquidity_gone: 6033
- no_momentum: 2928
- research_failed: 2135
- proven_low_volume: 1075
- simulated failed buy: 929
- proven_price_collapsed_or_parabolic: 123
- proven: 103
- proven_no_uptrend: 42
- dip: 30
- research_passed: 16

Warning: 606 judged pools had an unreadable mint/freeze value. Check mint_raw / freeze_raw in candidates.csv; the parsing may need fixing.
