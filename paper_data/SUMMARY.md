# Paper trader summary

SIMULATION ONLY. No real trades.

Updated 2026-11-12T12:42:01Z. Bankroll cash (research-selected trades): 456.400154541351. Open positions: 18. Pools on watchlist: 40.

| group | n | win | avg | CI | P&L $ |
|---|---|---|---|---|---|
| research-picked | 16 | 25% | -33.9% | -64 to -3 | -544 |
| momentum, not picked | 1924 | 12% | -64.5% | -67 to -62 | -124313 |
| all momentum | 1940 | 12% | -64.3% | -67 to -61 | -124856 |
| control | 2700 | 6% | -18.1% | -20 to -17 | -49236 |
| dip buy | 27 | 26% | -19.9% | -44 to 4 | -539 |
| proven pools | 91 | 34% | -30.2% | -41 to -20 | -2754 |

What-if exit rules on the SAME trades. Cells: avg return (trades, win rate).

| exit rule | momentum | control | dip | proven |
|---|---|---|---|---|
| base_sl30_tp100 | -65% (1919, 12%) | -18% (2700, 6%) | -20% (27, 26%) | -30% (91, 34%) |
| wide_sl50_tp100 | -65% (1919, 13%) | -18% (2700, 6%) | -23% (27, 30%) | -32% (91, 34%) |
| sl30_tp50 | -66% (1919, 15%) | -18% (2700, 6%) | -25% (27, 30%) | -31% (91, 34%) |
| sl50_tp50 | -66% (1919, 16%) | -19% (2700, 7%) | -28% (27, 33%) | -33% (91, 34%) |
| no_stop_tp100 | -65% (1919, 14%) | -19% (2700, 6%) | -21% (27, 30%) | -33% (91, 34%) |

Verdict: NOT ENOUGH DATA (need 30+ closed filter=1 trades and a CI above zero before believing anything).

Pools seen: 68496. Outcomes:

- missed_window: 45194
- low_liquidity: 11024
- proven_liquidity_gone: 5407
- no_momentum: 2754
- research_failed: 1931
- proven_low_volume: 1037
- simulated failed buy: 856
- proven_price_collapsed_or_parabolic: 119
- proven: 92
- proven_no_uptrend: 39
- dip: 27
- research_passed: 16

Warning: 566 judged pools had an unreadable mint/freeze value. Check mint_raw / freeze_raw in candidates.csv; the parsing may need fixing.
