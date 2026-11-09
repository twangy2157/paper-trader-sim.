# Paper trader summary

SIMULATION ONLY. No real trades.

Updated 2026-11-09T08:34:30Z. Bankroll cash (research-selected trades): 456.400154541351. Open positions: 26. Pools on watchlist: 55.

| group | n | win | avg | CI | P&L $ |
|---|---|---|---|---|---|
| research-picked | 16 | 25% | -33.9% | -64 to -3 | -544 |
| momentum, not picked | 1280 | 12% | -63.5% | -67 to -60 | -81395 |
| all momentum | 1296 | 13% | -63.1% | -66 to -60 | -81939 |
| control | 1789 | 5% | -18.7% | -20 to -17 | -33559 |
| dip buy | 13 | 8% | -38.7% | -63 to -14 | -504 |
| proven pools | 61 | 44% | -16.9% | -29 to -5 | -1036 |

What-if exit rules on the SAME trades. Cells: avg return (trades, win rate).

| exit rule | momentum | control | dip | proven |
|---|---|---|---|---|
| base_sl30_tp100 | -64% (1275, 13%) | -19% (1789, 5%) | -39% (13, 8%) | -17% (61, 44%) |
| wide_sl50_tp100 | -63% (1275, 14%) | -19% (1789, 6%) | -45% (13, 8%) | -17% (61, 44%) |
| sl30_tp50 | -64% (1275, 16%) | -19% (1789, 6%) | -41% (13, 8%) | -18% (61, 44%) |
| sl50_tp50 | -64% (1275, 17%) | -19% (1789, 6%) | -48% (13, 8%) | -18% (61, 44%) |
| no_stop_tp100 | -63% (1275, 15%) | -19% (1789, 6%) | -43% (13, 8%) | -17% (61, 44%) |

Verdict: NOT ENOUGH DATA (need 30+ closed filter=1 trades and a CI above zero before believing anything).

Pools seen: 47944. Outcomes:

- missed_window: 31810
- low_liquidity: 7888
- proven_liquidity_gone: 3635
- no_momentum: 1848
- research_failed: 1289
- proven_low_volume: 692
- simulated failed buy: 581
- proven_price_collapsed_or_parabolic: 82
- proven: 63
- proven_no_uptrend: 27
- research_passed: 16
- dip: 13

Warning: 383 judged pools had an unreadable mint/freeze value. Check mint_raw / freeze_raw in candidates.csv; the parsing may need fixing.
