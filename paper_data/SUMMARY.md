# Paper trader summary

SIMULATION ONLY. No real trades.

Updated 2026-11-10T04:26:01Z. Bankroll cash (research-selected trades): 456.400154541351. Open positions: 23. Pools on watchlist: 56.

| group | n | win | avg | CI | P&L $ |
|---|---|---|---|---|---|
| research-picked | 16 | 25% | -33.9% | -64 to -3 | -544 |
| momentum, not picked | 1434 | 12% | -63.4% | -66 to -60 | -91073 |
| all momentum | 1450 | 12% | -63.1% | -66 to -60 | -91616 |
| control | 2111 | 5% | -18.0% | -20 to -17 | -38294 |
| dip buy | 13 | 8% | -38.7% | -63 to -14 | -504 |
| proven pools | 75 | 37% | -25.7% | -37 to -14 | -1933 |

What-if exit rules on the SAME trades. Cells: avg return (trades, win rate).

| exit rule | momentum | control | dip | proven |
|---|---|---|---|---|
| base_sl30_tp100 | -63% (1429, 13%) | -18% (2111, 5%) | -39% (13, 8%) | -26% (75, 37%) |
| wide_sl50_tp100 | -63% (1429, 14%) | -18% (2111, 5%) | -45% (13, 8%) | -26% (75, 37%) |
| sl30_tp50 | -64% (1429, 15%) | -18% (2111, 6%) | -41% (13, 8%) | -27% (75, 37%) |
| sl50_tp50 | -64% (1429, 17%) | -19% (2111, 6%) | -48% (13, 8%) | -27% (75, 37%) |
| no_stop_tp100 | -63% (1429, 15%) | -19% (2111, 5%) | -43% (13, 8%) | -27% (75, 37%) |

Verdict: NOT ENOUGH DATA (need 30+ closed filter=1 trades and a CI above zero before believing anything).

Pools seen: 54181. Outcomes:

- missed_window: 36136
- low_liquidity: 8653
- proven_liquidity_gone: 4028
- no_momentum: 2167
- research_failed: 1443
- proven_low_volume: 842
- simulated failed buy: 681
- proven_price_collapsed_or_parabolic: 93
- proven: 76
- proven_no_uptrend: 32
- research_passed: 16
- dip: 14

Warning: 462 judged pools had an unreadable mint/freeze value. Check mint_raw / freeze_raw in candidates.csv; the parsing may need fixing.
