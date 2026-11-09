# Paper trader summary

SIMULATION ONLY. No real trades.

Updated 2026-11-09T20:18:21Z. Bankroll cash (research-selected trades): 456.400154541351. Open positions: 43. Pools on watchlist: 90.

| group | n | win | avg | CI | P&L $ |
|---|---|---|---|---|---|
| research-picked | 16 | 25% | -33.9% | -64 to -3 | -544 |
| momentum, not picked | 1363 | 13% | -63.5% | -67 to -60 | -86641 |
| all momentum | 1379 | 13% | -63.1% | -66 to -60 | -87185 |
| control | 1953 | 5% | -18.5% | -20 to -17 | -36230 |
| dip buy | 13 | 8% | -38.7% | -63 to -14 | -504 |
| proven pools | 74 | 38% | -26.0% | -38 to -14 | -1931 |

What-if exit rules on the SAME trades. Cells: avg return (trades, win rate).

| exit rule | momentum | control | dip | proven |
|---|---|---|---|---|
| base_sl30_tp100 | -64% (1358, 13%) | -18% (1953, 5%) | -39% (13, 8%) | -26% (74, 38%) |
| wide_sl50_tp100 | -63% (1358, 14%) | -19% (1953, 6%) | -45% (13, 8%) | -26% (74, 38%) |
| sl30_tp50 | -64% (1358, 16%) | -19% (1953, 6%) | -41% (13, 8%) | -27% (74, 38%) |
| sl50_tp50 | -64% (1358, 17%) | -19% (1953, 6%) | -48% (13, 8%) | -28% (74, 38%) |
| no_stop_tp100 | -63% (1358, 15%) | -19% (1953, 6%) | -43% (13, 8%) | -27% (74, 38%) |

Verdict: NOT ENOUGH DATA (need 30+ closed filter=1 trades and a CI above zero before believing anything).

Pools seen: 51648. Outcomes:

- missed_window: 34439
- low_liquidity: 8299
- proven_liquidity_gone: 3869
- no_momentum: 2032
- research_failed: 1370
- proven_low_volume: 770
- simulated failed buy: 646
- proven_price_collapsed_or_parabolic: 87
- proven: 75
- proven_no_uptrend: 32
- research_passed: 16
- dip: 13

Warning: 438 judged pools had an unreadable mint/freeze value. Check mint_raw / freeze_raw in candidates.csv; the parsing may need fixing.
