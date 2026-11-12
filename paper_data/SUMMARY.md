# Paper trader summary

SIMULATION ONLY. No real trades.

Updated 2026-11-12T09:28:10Z. Bankroll cash (research-selected trades): 456.400154541351. Open positions: 28. Pools on watchlist: 45.

| group | n | win | avg | CI | P&L $ |
|---|---|---|---|---|---|
| research-picked | 16 | 25% | -33.9% | -64 to -3 | -544 |
| momentum, not picked | 1896 | 12% | -64.6% | -67 to -62 | -122747 |
| all momentum | 1912 | 12% | -64.4% | -67 to -62 | -123291 |
| control | 2666 | 6% | -18.0% | -19 to -17 | -48335 |
| dip buy | 26 | 27% | -16.9% | -40 to 7 | -440 |
| proven pools | 91 | 34% | -30.2% | -41 to -20 | -2754 |

What-if exit rules on the SAME trades. Cells: avg return (trades, win rate).

| exit rule | momentum | control | dip | proven |
|---|---|---|---|---|
| base_sl30_tp100 | -65% (1891, 12%) | -18% (2666, 6%) | -17% (26, 27%) | -30% (91, 34%) |
| wide_sl50_tp100 | -65% (1891, 13%) | -18% (2666, 6%) | -20% (26, 31%) | -32% (91, 34%) |
| sl30_tp50 | -66% (1891, 15%) | -18% (2666, 6%) | -26% (26, 27%) | -31% (91, 34%) |
| sl50_tp50 | -66% (1891, 16%) | -19% (2666, 7%) | -30% (26, 31%) | -33% (91, 34%) |
| no_stop_tp100 | -65% (1891, 14%) | -18% (2666, 6%) | -18% (26, 31%) | -33% (91, 34%) |

Verdict: NOT ENOUGH DATA (need 30+ closed filter=1 trades and a CI above zero before believing anything).

Pools seen: 67738. Outcomes:

- missed_window: 44729
- low_liquidity: 10894
- proven_liquidity_gone: 5319
- no_momentum: 2721
- research_failed: 1912
- proven_low_volume: 1026
- simulated failed buy: 847
- proven_price_collapsed_or_parabolic: 117
- proven: 91
- proven_no_uptrend: 39
- dip: 27
- research_passed: 16

Warning: 561 judged pools had an unreadable mint/freeze value. Check mint_raw / freeze_raw in candidates.csv; the parsing may need fixing.
