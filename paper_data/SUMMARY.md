# Paper trader summary

SIMULATION ONLY. No real trades.

Updated 2026-11-12T14:58:10Z. Bankroll cash (research-selected trades): 456.400154541351. Open positions: 23. Pools on watchlist: 62.

| group | n | win | avg | CI | P&L $ |
|---|---|---|---|---|---|
| research-picked | 16 | 25% | -33.9% | -64 to -3 | -544 |
| momentum, not picked | 1942 | 12% | -64.6% | -67 to -62 | -125596 |
| all momentum | 1958 | 12% | -64.3% | -67 to -62 | -126140 |
| control | 2717 | 6% | -18.1% | -19 to -17 | -49472 |
| dip buy | 27 | 26% | -19.9% | -44 to 4 | -539 |
| proven pools | 92 | 35% | -29.8% | -41 to -19 | -2749 |

What-if exit rules on the SAME trades. Cells: avg return (trades, win rate).

| exit rule | momentum | control | dip | proven |
|---|---|---|---|---|
| base_sl30_tp100 | -65% (1937, 12%) | -18% (2717, 6%) | -20% (27, 26%) | -30% (92, 35%) |
| wide_sl50_tp100 | -65% (1937, 13%) | -18% (2717, 6%) | -23% (27, 30%) | -31% (92, 35%) |
| sl30_tp50 | -66% (1937, 15%) | -18% (2717, 6%) | -25% (27, 30%) | -31% (92, 35%) |
| sl50_tp50 | -66% (1937, 16%) | -19% (2717, 7%) | -28% (27, 33%) | -32% (92, 35%) |
| no_stop_tp100 | -65% (1937, 14%) | -19% (2717, 6%) | -21% (27, 30%) | -32% (92, 35%) |

Verdict: NOT ENOUGH DATA (need 30+ closed filter=1 trades and a CI above zero before believing anything).

Pools seen: 69060. Outcomes:

- missed_window: 45553
- low_liquidity: 11116
- proven_liquidity_gone: 5464
- no_momentum: 2773
- research_failed: 1952
- proven_low_volume: 1041
- simulated failed buy: 866
- proven_price_collapsed_or_parabolic: 119
- proven: 93
- proven_no_uptrend: 40
- dip: 27
- research_passed: 16

Warning: 572 judged pools had an unreadable mint/freeze value. Check mint_raw / freeze_raw in candidates.csv; the parsing may need fixing.
