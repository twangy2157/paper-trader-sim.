# Paper trader summary

SIMULATION ONLY. No real trades.

Updated 2026-11-13T00:10:09Z. Bankroll cash (research-selected trades): 456.400154541351. Open positions: 21. Pools on watchlist: 52.

| group | n | win | avg | CI | P&L $ |
|---|---|---|---|---|---|
| research-picked | 16 | 25% | -33.9% | -64 to -3 | -544 |
| momentum, not picked | 2017 | 12% | -64.8% | -67 to -62 | -130904 |
| all momentum | 2033 | 12% | -64.6% | -67 to -62 | -131447 |
| control | 2793 | 6% | -17.8% | -19 to -16 | -49969 |
| dip buy | 28 | 25% | -19.9% | -41 to 3 | -559 |
| proven pools | 97 | 34% | -31.8% | -42 to -21 | -3092 |

What-if exit rules on the SAME trades. Cells: avg return (trades, win rate).

| exit rule | momentum | control | dip | proven |
|---|---|---|---|---|
| base_sl30_tp100 | -65% (2012, 12%) | -18% (2793, 6%) | -20% (28, 25%) | -32% (97, 34%) |
| wide_sl50_tp100 | -65% (2012, 13%) | -18% (2793, 6%) | -23% (28, 29%) | -33% (97, 34%) |
| sl30_tp50 | -66% (2012, 15%) | -18% (2793, 6%) | -24% (28, 29%) | -32% (97, 35%) |
| sl50_tp50 | -66% (2012, 16%) | -18% (2793, 7%) | -27% (28, 32%) | -33% (97, 35%) |
| no_stop_tp100 | -65% (2012, 14%) | -18% (2793, 6%) | -20% (28, 29%) | -34% (97, 34%) |

Verdict: NOT ENOUGH DATA (need 30+ closed filter=1 trades and a CI above zero before believing anything).

Pools seen: 71476. Outcomes:

- missed_window: 47084
- low_liquidity: 11559
- proven_liquidity_gone: 5706
- no_momentum: 2844
- research_failed: 2027
- proven_low_volume: 1059
- simulated failed buy: 889
- proven_price_collapsed_or_parabolic: 121
- proven: 100
- proven_no_uptrend: 42
- dip: 29
- research_passed: 16

Warning: 587 judged pools had an unreadable mint/freeze value. Check mint_raw / freeze_raw in candidates.csv; the parsing may need fixing.
