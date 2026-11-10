# Paper trader summary

SIMULATION ONLY. No real trades.

Updated 2026-11-10T02:20:08Z. Bankroll cash (research-selected trades): 456.400154541351. Open positions: 15. Pools on watchlist: 54.

| group | n | win | avg | CI | P&L $ |
|---|---|---|---|---|---|
| research-picked | 16 | 25% | -33.9% | -64 to -3 | -544 |
| momentum, not picked | 1421 | 12% | -63.3% | -66 to -60 | -90058 |
| all momentum | 1437 | 12% | -63.0% | -66 to -60 | -90601 |
| control | 2086 | 5% | -18.0% | -19 to -17 | -37697 |
| dip buy | 13 | 8% | -38.7% | -63 to -14 | -504 |
| proven pools | 75 | 37% | -25.7% | -37 to -14 | -1933 |

What-if exit rules on the SAME trades. Cells: avg return (trades, win rate).

| exit rule | momentum | control | dip | proven |
|---|---|---|---|---|
| base_sl30_tp100 | -63% (1416, 13%) | -18% (2086, 5%) | -39% (13, 8%) | -26% (75, 37%) |
| wide_sl50_tp100 | -63% (1416, 14%) | -18% (2086, 5%) | -45% (13, 8%) | -26% (75, 37%) |
| sl30_tp50 | -64% (1416, 16%) | -18% (2086, 6%) | -41% (13, 8%) | -27% (75, 37%) |
| sl50_tp50 | -64% (1416, 17%) | -18% (2086, 6%) | -48% (13, 8%) | -27% (75, 37%) |
| no_stop_tp100 | -63% (1416, 15%) | -19% (2086, 5%) | -43% (13, 8%) | -27% (75, 37%) |

Verdict: NOT ENOUGH DATA (need 30+ closed filter=1 trades and a CI above zero before believing anything).

Pools seen: 53569. Outcomes:

- missed_window: 35724
- low_liquidity: 8565
- proven_liquidity_gone: 3981
- no_momentum: 2139
- research_failed: 1427
- proven_low_volume: 835
- simulated failed buy: 673
- proven_price_collapsed_or_parabolic: 89
- proven: 75
- proven_no_uptrend: 32
- research_passed: 16
- dip: 13

Warning: 459 judged pools had an unreadable mint/freeze value. Check mint_raw / freeze_raw in candidates.csv; the parsing may need fixing.
