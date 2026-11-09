# Paper trader summary

SIMULATION ONLY. No real trades.

Updated 2026-11-09T22:05:38Z. Bankroll cash (research-selected trades): 456.400154541351. Open positions: 47. Pools on watchlist: 96.

| group | n | win | avg | CI | P&L $ |
|---|---|---|---|---|---|
| research-picked | 16 | 25% | -33.9% | -64 to -3 | -544 |
| momentum, not picked | 1375 | 12% | -63.5% | -67 to -60 | -87500 |
| all momentum | 1391 | 13% | -63.2% | -66 to -60 | -88044 |
| control | 2011 | 5% | -18.3% | -20 to -17 | -36938 |
| dip buy | 13 | 8% | -38.7% | -63 to -14 | -504 |
| proven pools | 74 | 38% | -26.0% | -38 to -14 | -1931 |

What-if exit rules on the SAME trades. Cells: avg return (trades, win rate).

| exit rule | momentum | control | dip | proven |
|---|---|---|---|---|
| base_sl30_tp100 | -64% (1370, 13%) | -18% (2011, 5%) | -39% (13, 8%) | -26% (74, 38%) |
| wide_sl50_tp100 | -63% (1370, 14%) | -19% (2011, 6%) | -45% (13, 8%) | -26% (74, 38%) |
| sl30_tp50 | -64% (1370, 16%) | -19% (2011, 6%) | -41% (13, 8%) | -27% (74, 38%) |
| sl50_tp50 | -64% (1370, 17%) | -19% (2011, 6%) | -48% (13, 8%) | -28% (74, 38%) |
| no_stop_tp100 | -63% (1370, 15%) | -19% (2011, 6%) | -43% (13, 8%) | -27% (74, 38%) |

Verdict: NOT ENOUGH DATA (need 30+ closed filter=1 trades and a CI above zero before believing anything).

Pools seen: 52328. Outcomes:

- missed_window: 34902
- low_liquidity: 8382
- proven_liquidity_gone: 3903
- no_momentum: 2085
- research_failed: 1391
- proven_low_volume: 788
- simulated failed buy: 654
- proven_price_collapsed_or_parabolic: 87
- proven: 75
- proven_no_uptrend: 32
- research_passed: 16
- dip: 13

Warning: 447 judged pools had an unreadable mint/freeze value. Check mint_raw / freeze_raw in candidates.csv; the parsing may need fixing.
