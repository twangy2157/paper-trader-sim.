# Paper trader summary

SIMULATION ONLY. No real trades.

Updated 2026-11-12T16:44:34Z. Bankroll cash (research-selected trades): 456.400154541351. Open positions: 20. Pools on watchlist: 46.

| group | n | win | avg | CI | P&L $ |
|---|---|---|---|---|---|
| research-picked | 16 | 25% | -33.9% | -64 to -3 | -544 |
| momentum, not picked | 1960 | 12% | -64.7% | -67 to -62 | -127073 |
| all momentum | 1976 | 12% | -64.5% | -67 to -62 | -127617 |
| control | 2735 | 6% | -18.0% | -19 to -17 | -49550 |
| dip buy | 27 | 26% | -19.9% | -44 to 4 | -539 |
| proven pools | 92 | 35% | -29.8% | -41 to -19 | -2749 |

What-if exit rules on the SAME trades. Cells: avg return (trades, win rate).

| exit rule | momentum | control | dip | proven |
|---|---|---|---|---|
| base_sl30_tp100 | -65% (1955, 12%) | -18% (2735, 6%) | -20% (27, 26%) | -30% (92, 35%) |
| wide_sl50_tp100 | -65% (1955, 13%) | -18% (2735, 6%) | -23% (27, 30%) | -31% (92, 35%) |
| sl30_tp50 | -66% (1955, 15%) | -18% (2735, 6%) | -25% (27, 30%) | -31% (92, 35%) |
| sl50_tp50 | -66% (1955, 16%) | -19% (2735, 7%) | -28% (27, 33%) | -32% (92, 35%) |
| no_stop_tp100 | -65% (1955, 14%) | -18% (2735, 6%) | -21% (27, 30%) | -32% (92, 35%) |

Verdict: NOT ENOUGH DATA (need 30+ closed filter=1 trades and a CI above zero before believing anything).

Pools seen: 69510. Outcomes:

- missed_window: 45839
- low_liquidity: 11190
- proven_liquidity_gone: 5514
- no_momentum: 2782
- research_failed: 1974
- proven_low_volume: 1044
- simulated failed buy: 869
- proven_price_collapsed_or_parabolic: 119
- proven: 95
- proven_no_uptrend: 41
- dip: 27
- research_passed: 16

Warning: 574 judged pools had an unreadable mint/freeze value. Check mint_raw / freeze_raw in candidates.csv; the parsing may need fixing.
