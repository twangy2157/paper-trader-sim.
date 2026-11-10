# Paper trader summary

SIMULATION ONLY. No real trades.

Updated 2026-11-10T13:18:29Z. Bankroll cash (research-selected trades): 456.400154541351. Open positions: 9. Pools on watchlist: 62.

| group | n | win | avg | CI | P&L $ |
|---|---|---|---|---|---|
| research-picked | 16 | 25% | -33.9% | -64 to -3 | -544 |
| momentum, not picked | 1506 | 12% | -63.6% | -66 to -60 | -95857 |
| all momentum | 1522 | 12% | -63.2% | -66 to -60 | -96401 |
| control | 2206 | 5% | -18.0% | -19 to -17 | -39954 |
| dip buy | 15 | 13% | -32.7% | -58 to -8 | -491 |
| proven pools | 78 | 37% | -26.4% | -38 to -15 | -2065 |

What-if exit rules on the SAME trades. Cells: avg return (trades, win rate).

| exit rule | momentum | control | dip | proven |
|---|---|---|---|---|
| base_sl30_tp100 | -64% (1501, 13%) | -18% (2206, 5%) | -33% (15, 13%) | -26% (78, 37%) |
| wide_sl50_tp100 | -63% (1501, 14%) | -18% (2206, 5%) | -39% (15, 13%) | -27% (78, 37%) |
| sl30_tp50 | -65% (1501, 15%) | -18% (2206, 6%) | -37% (15, 13%) | -28% (78, 37%) |
| sl50_tp50 | -64% (1501, 17%) | -18% (2206, 6%) | -43% (15, 13%) | -28% (78, 37%) |
| no_stop_tp100 | -63% (1501, 15%) | -19% (2206, 5%) | -35% (15, 13%) | -27% (78, 37%) |

Verdict: NOT ENOUGH DATA (need 30+ closed filter=1 trades and a CI above zero before believing anything).

Pools seen: 56268. Outcomes:

- missed_window: 37499
- low_liquidity: 8949
- proven_liquidity_gone: 4226
- no_momentum: 2256
- research_failed: 1509
- proven_low_volume: 882
- simulated failed buy: 704
- proven_price_collapsed_or_parabolic: 99
- proven: 78
- proven_no_uptrend: 35
- research_passed: 16
- dip: 15

Warning: 474 judged pools had an unreadable mint/freeze value. Check mint_raw / freeze_raw in candidates.csv; the parsing may need fixing.
