# Paper trader summary

SIMULATION ONLY. No real trades.

Updated 2026-11-09T16:57:09Z. Bankroll cash (research-selected trades): 456.400154541351. Open positions: 25. Pools on watchlist: 61.

| group | n | win | avg | CI | P&L $ |
|---|---|---|---|---|---|
| research-picked | 16 | 25% | -33.9% | -64 to -3 | -544 |
| momentum, not picked | 1350 | 13% | -63.5% | -67 to -60 | -85912 |
| all momentum | 1366 | 13% | -63.2% | -66 to -60 | -86456 |
| control | 1891 | 5% | -18.7% | -20 to -17 | -35577 |
| dip buy | 13 | 8% | -38.7% | -63 to -14 | -504 |
| proven pools | 69 | 41% | -22.7% | -35 to -11 | -1572 |

What-if exit rules on the SAME trades. Cells: avg return (trades, win rate).

| exit rule | momentum | control | dip | proven |
|---|---|---|---|---|
| base_sl30_tp100 | -64% (1345, 13%) | -19% (1891, 5%) | -39% (13, 8%) | -23% (69, 41%) |
| wide_sl50_tp100 | -63% (1345, 14%) | -19% (1891, 6%) | -45% (13, 8%) | -23% (69, 41%) |
| sl30_tp50 | -64% (1345, 16%) | -19% (1891, 6%) | -41% (13, 8%) | -24% (69, 41%) |
| sl50_tp50 | -64% (1345, 17%) | -19% (1891, 7%) | -48% (13, 8%) | -24% (69, 41%) |
| no_stop_tp100 | -63% (1345, 15%) | -19% (1891, 6%) | -43% (13, 8%) | -23% (69, 41%) |

Verdict: NOT ENOUGH DATA (need 30+ closed filter=1 trades and a CI above zero before believing anything).

Pools seen: 50492. Outcomes:

- missed_window: 33610
- low_liquidity: 8186
- proven_liquidity_gone: 3823
- no_momentum: 1951
- research_failed: 1354
- proven_low_volume: 727
- simulated failed buy: 622
- proven_price_collapsed_or_parabolic: 85
- proven: 74
- proven_no_uptrend: 31
- research_passed: 16
- dip: 13

Warning: 417 judged pools had an unreadable mint/freeze value. Check mint_raw / freeze_raw in candidates.csv; the parsing may need fixing.
