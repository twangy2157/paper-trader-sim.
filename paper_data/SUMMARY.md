# Paper trader summary

SIMULATION ONLY. No real trades.

Updated 2026-11-12T23:17:38Z. Bankroll cash (research-selected trades): 456.400154541351. Open positions: 22. Pools on watchlist: 80.

| group | n | win | avg | CI | P&L $ |
|---|---|---|---|---|---|
| research-picked | 16 | 25% | -33.9% | -64 to -3 | -544 |
| momentum, not picked | 2009 | 12% | -64.9% | -67 to -62 | -130521 |
| all momentum | 2025 | 12% | -64.6% | -67 to -62 | -131065 |
| control | 2787 | 6% | -17.8% | -19 to -16 | -49834 |
| dip buy | 28 | 25% | -19.9% | -41 to 3 | -559 |
| proven pools | 97 | 34% | -31.8% | -42 to -21 | -3092 |

What-if exit rules on the SAME trades. Cells: avg return (trades, win rate).

| exit rule | momentum | control | dip | proven |
|---|---|---|---|---|
| base_sl30_tp100 | -65% (2004, 12%) | -18% (2787, 6%) | -20% (28, 25%) | -32% (97, 34%) |
| wide_sl50_tp100 | -65% (2004, 13%) | -18% (2787, 6%) | -23% (28, 29%) | -33% (97, 34%) |
| sl30_tp50 | -66% (2004, 15%) | -18% (2787, 6%) | -24% (28, 29%) | -32% (97, 35%) |
| sl50_tp50 | -66% (2004, 16%) | -18% (2787, 7%) | -27% (28, 32%) | -33% (97, 35%) |
| no_stop_tp100 | -65% (2004, 14%) | -18% (2787, 6%) | -20% (28, 29%) | -34% (97, 34%) |

Verdict: NOT ENOUGH DATA (need 30+ closed filter=1 trades and a CI above zero before believing anything).

Pools seen: 71197. Outcomes:

- missed_window: 46894
- low_liquidity: 11512
- proven_liquidity_gone: 5681
- no_momentum: 2838
- research_failed: 2020
- proven_low_volume: 1056
- simulated failed buy: 888
- proven_price_collapsed_or_parabolic: 121
- proven: 100
- proven_no_uptrend: 42
- dip: 29
- research_passed: 16

Warning: 585 judged pools had an unreadable mint/freeze value. Check mint_raw / freeze_raw in candidates.csv; the parsing may need fixing.
