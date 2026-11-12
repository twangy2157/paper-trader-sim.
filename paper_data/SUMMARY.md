# Paper trader summary

SIMULATION ONLY. No real trades.

Updated 2026-11-12T13:34:09Z. Bankroll cash (research-selected trades): 456.400154541351. Open positions: 17. Pools on watchlist: 55.

| group | n | win | avg | CI | P&L $ |
|---|---|---|---|---|---|
| research-picked | 16 | 25% | -33.9% | -64 to -3 | -544 |
| momentum, not picked | 1928 | 12% | -64.5% | -67 to -62 | -124438 |
| all momentum | 1944 | 12% | -64.2% | -67 to -62 | -124981 |
| control | 2709 | 6% | -18.1% | -19 to -17 | -49254 |
| dip buy | 27 | 26% | -19.9% | -44 to 4 | -539 |
| proven pools | 91 | 34% | -30.2% | -41 to -20 | -2754 |

What-if exit rules on the SAME trades. Cells: avg return (trades, win rate).

| exit rule | momentum | control | dip | proven |
|---|---|---|---|---|
| base_sl30_tp100 | -64% (1923, 12%) | -18% (2709, 6%) | -20% (27, 26%) | -30% (91, 34%) |
| wide_sl50_tp100 | -65% (1923, 14%) | -18% (2709, 6%) | -23% (27, 30%) | -32% (91, 34%) |
| sl30_tp50 | -66% (1923, 15%) | -18% (2709, 6%) | -25% (27, 30%) | -31% (91, 34%) |
| sl50_tp50 | -66% (1923, 16%) | -19% (2709, 7%) | -28% (27, 33%) | -33% (91, 34%) |
| no_stop_tp100 | -65% (1923, 14%) | -19% (2709, 6%) | -21% (27, 30%) | -33% (91, 34%) |

Verdict: NOT ENOUGH DATA (need 30+ closed filter=1 trades and a CI above zero before believing anything).

Pools seen: 68673. Outcomes:

- missed_window: 45309
- low_liquidity: 11050
- proven_liquidity_gone: 5424
- no_momentum: 2756
- research_failed: 1941
- proven_low_volume: 1039
- simulated failed buy: 860
- proven_price_collapsed_or_parabolic: 119
- proven: 92
- proven_no_uptrend: 40
- dip: 27
- research_passed: 16

Warning: 569 judged pools had an unreadable mint/freeze value. Check mint_raw / freeze_raw in candidates.csv; the parsing may need fixing.
