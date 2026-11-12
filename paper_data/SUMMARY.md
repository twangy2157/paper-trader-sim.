# Paper trader summary

SIMULATION ONLY. No real trades.

Updated 2026-11-12T22:44:55Z. Bankroll cash (research-selected trades): 456.400154541351. Open positions: 17. Pools on watchlist: 45.

| group | n | win | avg | CI | P&L $ |
|---|---|---|---|---|---|
| research-picked | 16 | 25% | -33.9% | -64 to -3 | -544 |
| momentum, not picked | 2007 | 12% | -64.9% | -67 to -62 | -130384 |
| all momentum | 2023 | 12% | -64.6% | -67 to -62 | -130927 |
| control | 2782 | 6% | -17.8% | -19 to -17 | -49813 |
| dip buy | 28 | 25% | -19.9% | -41 to 3 | -559 |
| proven pools | 97 | 34% | -31.8% | -42 to -21 | -3092 |

What-if exit rules on the SAME trades. Cells: avg return (trades, win rate).

| exit rule | momentum | control | dip | proven |
|---|---|---|---|---|
| base_sl30_tp100 | -65% (2002, 12%) | -18% (2782, 6%) | -20% (28, 25%) | -32% (97, 34%) |
| wide_sl50_tp100 | -65% (2002, 13%) | -18% (2782, 6%) | -23% (28, 29%) | -33% (97, 34%) |
| sl30_tp50 | -66% (2002, 15%) | -18% (2782, 6%) | -24% (28, 29%) | -32% (97, 35%) |
| sl50_tp50 | -66% (2002, 16%) | -18% (2782, 7%) | -27% (28, 32%) | -33% (97, 35%) |
| no_stop_tp100 | -65% (2002, 14%) | -18% (2782, 6%) | -20% (28, 29%) | -34% (97, 34%) |

Verdict: NOT ENOUGH DATA (need 30+ closed filter=1 trades and a CI above zero before believing anything).

Pools seen: 71062. Outcomes:

- missed_window: 46810
- low_liquidity: 11486
- proven_liquidity_gone: 5669
- no_momentum: 2834
- research_failed: 2014
- proven_low_volume: 1056
- simulated failed buy: 887
- proven_price_collapsed_or_parabolic: 121
- proven: 99
- proven_no_uptrend: 42
- dip: 28
- research_passed: 16

Warning: 584 judged pools had an unreadable mint/freeze value. Check mint_raw / freeze_raw in candidates.csv; the parsing may need fixing.
