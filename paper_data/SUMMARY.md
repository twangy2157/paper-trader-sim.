# Paper trader summary

SIMULATION ONLY. No real trades.

Updated 2026-11-09T07:41:00Z. Bankroll cash (research-selected trades): 456.400154541351. Open positions: 6. Pools on watchlist: 74.

| group | n | win | avg | CI | P&L $ |
|---|---|---|---|---|---|
| research-picked | 16 | 25% | -33.9% | -64 to -3 | -544 |
| momentum, not picked | 1277 | 12% | -63.6% | -67 to -60 | -81377 |
| all momentum | 1293 | 13% | -63.3% | -66 to -60 | -81921 |
| control | 1788 | 5% | -18.6% | -20 to -17 | -33458 |
| dip buy | 13 | 8% | -38.7% | -63 to -14 | -504 |
| proven pools | 61 | 44% | -16.9% | -29 to -5 | -1035 |

What-if exit rules on the SAME trades. Cells: avg return (trades, win rate).

| exit rule | momentum | control | dip | proven |
|---|---|---|---|---|
| base_sl30_tp100 | -64% (1272, 13%) | -19% (1788, 5%) | -39% (13, 8%) | -17% (61, 44%) |
| wide_sl50_tp100 | -63% (1272, 14%) | -19% (1788, 6%) | -45% (13, 8%) | -17% (61, 44%) |
| sl30_tp50 | -64% (1272, 16%) | -19% (1788, 6%) | -41% (13, 8%) | -18% (61, 44%) |
| sl50_tp50 | -64% (1272, 17%) | -19% (1788, 6%) | -48% (13, 8%) | -18% (61, 44%) |
| no_stop_tp100 | -63% (1272, 15%) | -19% (1788, 6%) | -43% (13, 8%) | -17% (61, 44%) |

Verdict: NOT ENOUGH DATA (need 30+ closed filter=1 trades and a CI above zero before believing anything).

Pools seen: 47675. Outcomes:

- missed_window: 31649
- low_liquidity: 7843
- proven_liquidity_gone: 3612
- no_momentum: 1834
- research_failed: 1280
- proven_low_volume: 680
- simulated failed buy: 577
- proven_price_collapsed_or_parabolic: 82
- proven: 62
- proven_no_uptrend: 27
- research_passed: 16
- dip: 13

Warning: 382 judged pools had an unreadable mint/freeze value. Check mint_raw / freeze_raw in candidates.csv; the parsing may need fixing.
