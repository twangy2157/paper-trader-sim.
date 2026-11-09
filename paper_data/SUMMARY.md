# Paper trader summary

SIMULATION ONLY. No real trades.

Updated 2026-11-09T23:21:54Z. Bankroll cash (research-selected trades): 456.400154541351. Open positions: 26. Pools on watchlist: 72.

| group | n | win | avg | CI | P&L $ |
|---|---|---|---|---|---|
| research-picked | 16 | 25% | -33.9% | -64 to -3 | -544 |
| momentum, not picked | 1394 | 12% | -63.6% | -67 to -61 | -88747 |
| all momentum | 1410 | 12% | -63.2% | -66 to -60 | -89291 |
| control | 2044 | 5% | -18.1% | -20 to -17 | -37215 |
| dip buy | 13 | 8% | -38.7% | -63 to -14 | -504 |
| proven pools | 75 | 37% | -25.7% | -37 to -14 | -1933 |

What-if exit rules on the SAME trades. Cells: avg return (trades, win rate).

| exit rule | momentum | control | dip | proven |
|---|---|---|---|---|
| base_sl30_tp100 | -64% (1389, 13%) | -18% (2044, 5%) | -39% (13, 8%) | -26% (75, 37%) |
| wide_sl50_tp100 | -63% (1389, 14%) | -18% (2044, 5%) | -45% (13, 8%) | -26% (75, 37%) |
| sl30_tp50 | -64% (1389, 16%) | -18% (2044, 6%) | -41% (13, 8%) | -27% (75, 37%) |
| sl50_tp50 | -64% (1389, 17%) | -19% (2044, 6%) | -48% (13, 8%) | -27% (75, 37%) |
| no_stop_tp100 | -63% (1389, 15%) | -19% (2044, 5%) | -43% (13, 8%) | -27% (75, 37%) |

Verdict: NOT ENOUGH DATA (need 30+ closed filter=1 trades and a CI above zero before believing anything).

Pools seen: 52807. Outcomes:

- missed_window: 35218
- low_liquidity: 8462
- proven_liquidity_gone: 3920
- no_momentum: 2107
- research_failed: 1401
- proven_low_volume: 811
- simulated failed buy: 665
- proven_price_collapsed_or_parabolic: 87
- proven: 75
- proven_no_uptrend: 32
- research_passed: 16
- dip: 13

Warning: 457 judged pools had an unreadable mint/freeze value. Check mint_raw / freeze_raw in candidates.csv; the parsing may need fixing.
