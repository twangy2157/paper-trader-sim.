# Paper trader summary

SIMULATION ONLY. No real trades.

Updated 2026-11-15T03:27:46Z. Bankroll cash (research-selected trades): 456.400154541351. Open positions: 20. Pools on watchlist: 50.

| group | n | win | avg | CI | P&L $ |
|---|---|---|---|---|---|
| research-picked | 16 | 25% | -33.9% | -64 to -3 | -544 |
| momentum, not picked | 2425 | 12% | -65.5% | -68 to -63 | -159043 |
| all momentum | 2441 | 12% | -65.3% | -68 to -63 | -159587 |
| control | 3158 | 6% | -18.8% | -20 to -17 | -59519 |
| dip buy | 33 | 30% | -12.1% | -32 to 8 | -402 |
| proven pools | 110 | 34% | -34.0% | -44 to -24 | -3747 |

What-if exit rules on the SAME trades. Cells: avg return (trades, win rate).

| exit rule | momentum | control | dip | proven |
|---|---|---|---|---|
| base_sl30_tp100 | -66% (2420, 12%) | -19% (3158, 6%) | -12% (33, 30%) | -34% (110, 34%) |
| wide_sl50_tp100 | -66% (2420, 13%) | -19% (3158, 6%) | -15% (33, 33%) | -35% (110, 34%) |
| sl30_tp50 | -67% (2420, 14%) | -19% (3158, 7%) | -18% (33, 33%) | -34% (110, 35%) |
| sl50_tp50 | -66% (2420, 16%) | -19% (3158, 7%) | -21% (33, 36%) | -35% (110, 35%) |
| no_stop_tp100 | -65% (2420, 14%) | -19% (3158, 6%) | -13% (33, 33%) | -36% (110, 34%) |

Verdict: NOT ENOUGH DATA (need 30+ closed filter=1 trades and a CI above zero before believing anything).

Pools seen: 85350. Outcomes:

- missed_window: 56111
- low_liquidity: 14011
- proven_liquidity_gone: 7059
- no_momentum: 3208
- research_failed: 2439
- proven_low_volume: 1139
- simulated failed buy: 1037
- proven_price_collapsed_or_parabolic: 135
- proven: 110
- proven_no_uptrend: 52
- dip: 33
- research_passed: 16

Warning: 661 judged pools had an unreadable mint/freeze value. Check mint_raw / freeze_raw in candidates.csv; the parsing may need fixing.
