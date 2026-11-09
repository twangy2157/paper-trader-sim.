# Paper trader summary

SIMULATION ONLY. No real trades.

Updated 2026-11-09T13:23:30Z. Bankroll cash (research-selected trades): 456.400154541351. Open positions: 20. Pools on watchlist: 89.

| group | n | win | avg | CI | P&L $ |
|---|---|---|---|---|---|
| research-picked | 16 | 25% | -33.9% | -64 to -3 | -544 |
| momentum, not picked | 1322 | 13% | -63.2% | -66 to -60 | -83605 |
| all momentum | 1338 | 13% | -62.8% | -66 to -60 | -84148 |
| control | 1848 | 5% | -18.8% | -20 to -17 | -34874 |
| dip buy | 13 | 8% | -38.7% | -63 to -14 | -504 |
| proven pools | 64 | 44% | -19.2% | -32 to -7 | -1233 |

What-if exit rules on the SAME trades. Cells: avg return (trades, win rate).

| exit rule | momentum | control | dip | proven |
|---|---|---|---|---|
| base_sl30_tp100 | -63% (1317, 13%) | -19% (1848, 5%) | -39% (13, 8%) | -19% (64, 44%) |
| wide_sl50_tp100 | -63% (1317, 15%) | -19% (1848, 6%) | -45% (13, 8%) | -19% (64, 44%) |
| sl30_tp50 | -64% (1317, 16%) | -19% (1848, 6%) | -41% (13, 8%) | -21% (64, 44%) |
| sl50_tp50 | -64% (1317, 18%) | -19% (1848, 6%) | -48% (13, 8%) | -21% (64, 44%) |
| no_stop_tp100 | -62% (1317, 15%) | -19% (1848, 6%) | -43% (13, 8%) | -19% (64, 44%) |

Verdict: NOT ENOUGH DATA (need 30+ closed filter=1 trades and a CI above zero before believing anything).

Pools seen: 49271. Outcomes:

- missed_window: 32701
- low_liquidity: 8078
- proven_liquidity_gone: 3745
- no_momentum: 1902
- research_failed: 1331
- proven_low_volume: 709
- simulated failed buy: 599
- proven_price_collapsed_or_parabolic: 83
- proven: 65
- proven_no_uptrend: 29
- research_passed: 16
- dip: 13

Warning: 399 judged pools had an unreadable mint/freeze value. Check mint_raw / freeze_raw in candidates.csv; the parsing may need fixing.
