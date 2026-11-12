# Paper trader summary

SIMULATION ONLY. No real trades.

Updated 2026-11-12T16:55:09Z. Bankroll cash (research-selected trades): 456.400154541351. Open positions: 23. Pools on watchlist: 54.

| group | n | win | avg | CI | P&L $ |
|---|---|---|---|---|---|
| research-picked | 16 | 25% | -33.9% | -64 to -3 | -544 |
| momentum, not picked | 1962 | 12% | -64.8% | -67 to -62 | -127274 |
| all momentum | 1978 | 12% | -64.5% | -67 to -62 | -127818 |
| control | 2735 | 6% | -18.0% | -19 to -17 | -49550 |
| dip buy | 27 | 26% | -19.9% | -44 to 4 | -539 |
| proven pools | 92 | 35% | -29.8% | -41 to -19 | -2749 |

What-if exit rules on the SAME trades. Cells: avg return (trades, win rate).

| exit rule | momentum | control | dip | proven |
|---|---|---|---|---|
| base_sl30_tp100 | -65% (1957, 12%) | -18% (2735, 6%) | -20% (27, 26%) | -30% (92, 35%) |
| wide_sl50_tp100 | -65% (1957, 13%) | -18% (2735, 6%) | -23% (27, 30%) | -31% (92, 35%) |
| sl30_tp50 | -66% (1957, 15%) | -18% (2735, 6%) | -25% (27, 30%) | -31% (92, 35%) |
| sl50_tp50 | -66% (1957, 16%) | -19% (2735, 7%) | -28% (27, 33%) | -32% (92, 35%) |
| no_stop_tp100 | -65% (1957, 14%) | -18% (2735, 6%) | -21% (27, 30%) | -32% (92, 35%) |

Verdict: NOT ENOUGH DATA (need 30+ closed filter=1 trades and a CI above zero before believing anything).

Pools seen: 69550. Outcomes:

- missed_window: 45857
- low_liquidity: 11203
- proven_liquidity_gone: 5517
- no_momentum: 2787
- research_failed: 1974
- proven_low_volume: 1045
- simulated failed buy: 869
- proven_price_collapsed_or_parabolic: 119
- proven: 95
- proven_no_uptrend: 41
- dip: 27
- research_passed: 16

Warning: 574 judged pools had an unreadable mint/freeze value. Check mint_raw / freeze_raw in candidates.csv; the parsing may need fixing.
