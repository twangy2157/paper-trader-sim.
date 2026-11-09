# Paper trader summary

SIMULATION ONLY. No real trades.

Updated 2026-11-09T09:06:29Z. Bankroll cash (research-selected trades): 456.400154541351. Open positions: 29. Pools on watchlist: 47.

| group | n | win | avg | CI | P&L $ |
|---|---|---|---|---|---|
| research-picked | 16 | 25% | -33.9% | -64 to -3 | -544 |
| momentum, not picked | 1285 | 12% | -63.6% | -67 to -60 | -81896 |
| all momentum | 1301 | 13% | -63.3% | -67 to -60 | -82440 |
| control | 1796 | 5% | -18.7% | -20 to -17 | -33675 |
| dip buy | 13 | 8% | -38.7% | -63 to -14 | -504 |
| proven pools | 61 | 44% | -16.9% | -29 to -5 | -1036 |

What-if exit rules on the SAME trades. Cells: avg return (trades, win rate).

| exit rule | momentum | control | dip | proven |
|---|---|---|---|---|
| base_sl30_tp100 | -64% (1280, 13%) | -19% (1796, 5%) | -39% (13, 8%) | -17% (61, 44%) |
| wide_sl50_tp100 | -63% (1280, 14%) | -19% (1796, 6%) | -45% (13, 8%) | -17% (61, 44%) |
| sl30_tp50 | -64% (1280, 16%) | -19% (1796, 6%) | -41% (13, 8%) | -18% (61, 44%) |
| sl50_tp50 | -64% (1280, 17%) | -19% (1796, 7%) | -48% (13, 8%) | -18% (61, 44%) |
| no_stop_tp100 | -63% (1280, 15%) | -19% (1796, 6%) | -43% (13, 8%) | -17% (61, 44%) |

Verdict: NOT ENOUGH DATA (need 30+ closed filter=1 trades and a CI above zero before believing anything).

Pools seen: 48098. Outcomes:

- missed_window: 31919
- low_liquidity: 7908
- proven_liquidity_gone: 3641
- no_momentum: 1855
- research_failed: 1296
- proven_low_volume: 695
- simulated failed buy: 582
- proven_price_collapsed_or_parabolic: 82
- proven: 64
- proven_no_uptrend: 27
- research_passed: 16
- dip: 13

Warning: 383 judged pools had an unreadable mint/freeze value. Check mint_raw / freeze_raw in candidates.csv; the parsing may need fixing.
