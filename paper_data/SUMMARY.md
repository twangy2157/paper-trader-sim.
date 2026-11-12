# Paper trader summary

SIMULATION ONLY. No real trades.

Updated 2026-11-12T14:06:10Z. Bankroll cash (research-selected trades): 456.400154541351. Open positions: 20. Pools on watchlist: 64.

| group | n | win | avg | CI | P&L $ |
|---|---|---|---|---|---|
| research-picked | 16 | 25% | -33.9% | -64 to -3 | -544 |
| momentum, not picked | 1935 | 12% | -64.5% | -67 to -62 | -125042 |
| all momentum | 1951 | 12% | -64.3% | -67 to -61 | -125586 |
| control | 2710 | 6% | -18.1% | -20 to -17 | -49355 |
| dip buy | 27 | 26% | -19.9% | -44 to 4 | -539 |
| proven pools | 91 | 34% | -30.2% | -41 to -20 | -2754 |

What-if exit rules on the SAME trades. Cells: avg return (trades, win rate).

| exit rule | momentum | control | dip | proven |
|---|---|---|---|---|
| base_sl30_tp100 | -65% (1930, 12%) | -18% (2710, 6%) | -20% (27, 26%) | -30% (91, 34%) |
| wide_sl50_tp100 | -65% (1930, 13%) | -18% (2710, 6%) | -23% (27, 30%) | -32% (91, 34%) |
| sl30_tp50 | -66% (1930, 15%) | -18% (2710, 6%) | -25% (27, 30%) | -31% (91, 34%) |
| sl50_tp50 | -66% (1930, 16%) | -19% (2710, 7%) | -28% (27, 33%) | -33% (91, 34%) |
| no_stop_tp100 | -65% (1930, 14%) | -19% (2710, 6%) | -21% (27, 30%) | -33% (91, 34%) |

Verdict: NOT ENOUGH DATA (need 30+ closed filter=1 trades and a CI above zero before believing anything).

Pools seen: 68815. Outcomes:

- missed_window: 45395
- low_liquidity: 11079
- proven_liquidity_gone: 5437
- no_momentum: 2765
- research_failed: 1942
- proven_low_volume: 1041
- simulated failed buy: 861
- proven_price_collapsed_or_parabolic: 119
- proven: 93
- proven_no_uptrend: 40
- dip: 27
- research_passed: 16

Warning: 570 judged pools had an unreadable mint/freeze value. Check mint_raw / freeze_raw in candidates.csv; the parsing may need fixing.
