# Paper trader summary

SIMULATION ONLY. No real trades.

Updated 2026-11-12T14:37:09Z. Bankroll cash (research-selected trades): 456.400154541351. Open positions: 18. Pools on watchlist: 31.

| group | n | win | avg | CI | P&L $ |
|---|---|---|---|---|---|
| research-picked | 16 | 25% | -33.9% | -64 to -3 | -544 |
| momentum, not picked | 1941 | 12% | -64.6% | -67 to -62 | -125495 |
| all momentum | 1957 | 12% | -64.3% | -67 to -62 | -126039 |
| control | 2713 | 6% | -18.1% | -20 to -17 | -49445 |
| dip buy | 27 | 26% | -19.9% | -44 to 4 | -539 |
| proven pools | 92 | 35% | -29.8% | -41 to -19 | -2749 |

What-if exit rules on the SAME trades. Cells: avg return (trades, win rate).

| exit rule | momentum | control | dip | proven |
|---|---|---|---|---|
| base_sl30_tp100 | -65% (1936, 12%) | -18% (2713, 6%) | -20% (27, 26%) | -30% (92, 35%) |
| wide_sl50_tp100 | -65% (1936, 13%) | -18% (2713, 6%) | -23% (27, 30%) | -31% (92, 35%) |
| sl30_tp50 | -66% (1936, 15%) | -18% (2713, 6%) | -25% (27, 30%) | -31% (92, 35%) |
| sl50_tp50 | -66% (1936, 16%) | -19% (2713, 7%) | -28% (27, 33%) | -32% (92, 35%) |
| no_stop_tp100 | -65% (1936, 14%) | -19% (2713, 6%) | -21% (27, 30%) | -32% (92, 35%) |

Verdict: NOT ENOUGH DATA (need 30+ closed filter=1 trades and a CI above zero before believing anything).

Pools seen: 68995. Outcomes:

- missed_window: 45525
- low_liquidity: 11100
- proven_liquidity_gone: 5457
- no_momentum: 2768
- research_failed: 1947
- proven_low_volume: 1041
- simulated failed buy: 862
- proven_price_collapsed_or_parabolic: 119
- proven: 93
- proven_no_uptrend: 40
- dip: 27
- research_passed: 16

Warning: 570 judged pools had an unreadable mint/freeze value. Check mint_raw / freeze_raw in candidates.csv; the parsing may need fixing.
