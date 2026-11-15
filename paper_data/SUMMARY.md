# Paper trader summary

SIMULATION ONLY. No real trades.

Updated 2026-11-15T20:07:13Z. Bankroll cash (research-selected trades): 456.400154541351. Open positions: 13. Pools on watchlist: 62.

| group | n | win | avg | CI | P&L $ |
|---|---|---|---|---|---|
| research-picked | 16 | 25% | -33.9% | -64 to -3 | -544 |
| momentum, not picked | 2577 | 12% | -65.9% | -68 to -64 | -170067 |
| all momentum | 2593 | 12% | -65.7% | -68 to -64 | -170610 |
| control | 3305 | 6% | -18.6% | -20 to -17 | -61901 |
| dip buy | 34 | 29% | -11.9% | -32 to 8 | -406 |
| proven pools | 112 | 34% | -33.2% | -43 to -23 | -3725 |

What-if exit rules on the SAME trades. Cells: avg return (trades, win rate).

| exit rule | momentum | control | dip | proven |
|---|---|---|---|---|
| base_sl30_tp100 | -66% (2572, 12%) | -19% (3305, 6%) | -12% (34, 29%) | -33% (112, 34%) |
| wide_sl50_tp100 | -66% (2572, 13%) | -19% (3305, 6%) | -15% (34, 32%) | -34% (112, 34%) |
| sl30_tp50 | -67% (2572, 14%) | -19% (3305, 7%) | -18% (34, 32%) | -33% (112, 35%) |
| sl50_tp50 | -67% (2572, 16%) | -19% (3305, 7%) | -21% (34, 35%) | -34% (112, 35%) |
| no_stop_tp100 | -66% (2572, 14%) | -19% (3305, 6%) | -13% (34, 32%) | -35% (112, 34%) |

Verdict: NOT ENOUGH DATA (need 30+ closed filter=1 trades and a CI above zero before believing anything).

Pools seen: 89547. Outcomes:

- missed_window: 58781
- low_liquidity: 14682
- proven_liquidity_gone: 7483
- no_momentum: 3356
- research_failed: 2582
- proven_low_volume: 1196
- simulated failed buy: 1109
- proven_price_collapsed_or_parabolic: 138
- proven: 113
- proven_no_uptrend: 57
- dip: 34
- research_passed: 16

Warning: 707 judged pools had an unreadable mint/freeze value. Check mint_raw / freeze_raw in candidates.csv; the parsing may need fixing.
