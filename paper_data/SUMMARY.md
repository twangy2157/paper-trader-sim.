# Paper trader summary

SIMULATION ONLY. No real trades.

Updated 2026-11-12T22:55:45Z. Bankroll cash (research-selected trades): 456.400154541351. Open positions: 13. Pools on watchlist: 49.

| group | n | win | avg | CI | P&L $ |
|---|---|---|---|---|---|
| research-picked | 16 | 25% | -33.9% | -64 to -3 | -544 |
| momentum, not picked | 2008 | 12% | -64.9% | -67 to -62 | -130484 |
| all momentum | 2024 | 12% | -64.6% | -67 to -62 | -131027 |
| control | 2786 | 6% | -17.8% | -19 to -17 | -49886 |
| dip buy | 28 | 25% | -19.9% | -41 to 3 | -559 |
| proven pools | 97 | 34% | -31.8% | -42 to -21 | -3092 |

What-if exit rules on the SAME trades. Cells: avg return (trades, win rate).

| exit rule | momentum | control | dip | proven |
|---|---|---|---|---|
| base_sl30_tp100 | -65% (2003, 12%) | -18% (2786, 6%) | -20% (28, 25%) | -32% (97, 34%) |
| wide_sl50_tp100 | -65% (2003, 13%) | -18% (2786, 6%) | -23% (28, 29%) | -33% (97, 34%) |
| sl30_tp50 | -66% (2003, 15%) | -18% (2786, 6%) | -24% (28, 29%) | -32% (97, 35%) |
| sl50_tp50 | -66% (2003, 16%) | -18% (2786, 7%) | -27% (28, 32%) | -33% (97, 35%) |
| no_stop_tp100 | -65% (2003, 14%) | -18% (2786, 6%) | -20% (28, 29%) | -34% (97, 34%) |

Verdict: NOT ENOUGH DATA (need 30+ closed filter=1 trades and a CI above zero before believing anything).

Pools seen: 71105. Outcomes:

- missed_window: 46843
- low_liquidity: 11493
- proven_liquidity_gone: 5671
- no_momentum: 2834
- research_failed: 2015
- proven_low_volume: 1056
- simulated failed buy: 887
- proven_price_collapsed_or_parabolic: 121
- proven: 99
- proven_no_uptrend: 42
- dip: 28
- research_passed: 16

Warning: 584 judged pools had an unreadable mint/freeze value. Check mint_raw / freeze_raw in candidates.csv; the parsing may need fixing.
