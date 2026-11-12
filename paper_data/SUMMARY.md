# Paper trader summary

SIMULATION ONLY. No real trades.

Updated 2026-11-12T11:16:45Z. Bankroll cash (research-selected trades): 456.400154541351. Open positions: 22. Pools on watchlist: 50.

| group | n | win | avg | CI | P&L $ |
|---|---|---|---|---|---|
| research-picked | 16 | 25% | -33.9% | -64 to -3 | -544 |
| momentum, not picked | 1914 | 12% | -64.5% | -67 to -62 | -123575 |
| all momentum | 1930 | 12% | -64.2% | -67 to -62 | -124119 |
| control | 2685 | 6% | -18.1% | -19 to -17 | -48900 |
| dip buy | 27 | 26% | -19.9% | -44 to 4 | -539 |
| proven pools | 91 | 34% | -30.2% | -41 to -20 | -2754 |

What-if exit rules on the SAME trades. Cells: avg return (trades, win rate).

| exit rule | momentum | control | dip | proven |
|---|---|---|---|---|
| base_sl30_tp100 | -65% (1909, 12%) | -18% (2685, 6%) | -20% (27, 26%) | -30% (91, 34%) |
| wide_sl50_tp100 | -65% (1909, 14%) | -18% (2685, 6%) | -23% (27, 30%) | -32% (91, 34%) |
| sl30_tp50 | -66% (1909, 15%) | -18% (2685, 6%) | -25% (27, 30%) | -31% (91, 34%) |
| sl50_tp50 | -65% (1909, 16%) | -19% (2685, 7%) | -28% (27, 33%) | -33% (91, 34%) |
| no_stop_tp100 | -65% (1909, 14%) | -19% (2685, 6%) | -21% (27, 30%) | -33% (91, 34%) |

Verdict: NOT ENOUGH DATA (need 30+ closed filter=1 trades and a CI above zero before believing anything).

Pools seen: 68149. Outcomes:

- missed_window: 44981
- low_liquidity: 10965
- proven_liquidity_gone: 5365
- no_momentum: 2742
- research_failed: 1922
- proven_low_volume: 1029
- simulated failed buy: 853
- proven_price_collapsed_or_parabolic: 118
- proven: 92
- proven_no_uptrend: 39
- dip: 27
- research_passed: 16

Warning: 565 judged pools had an unreadable mint/freeze value. Check mint_raw / freeze_raw in candidates.csv; the parsing may need fixing.
