# Paper trader summary

SIMULATION ONLY. No real trades.

Updated 2026-11-09T11:34:55Z. Bankroll cash (research-selected trades): 456.400154541351. Open positions: 25. Pools on watchlist: 41.

| group | n | win | avg | CI | P&L $ |
|---|---|---|---|---|---|
| research-picked | 16 | 25% | -33.9% | -64 to -3 | -544 |
| momentum, not picked | 1302 | 13% | -63.4% | -67 to -60 | -82633 |
| all momentum | 1318 | 13% | -63.0% | -66 to -60 | -83176 |
| control | 1827 | 5% | -18.7% | -20 to -17 | -34314 |
| dip buy | 13 | 8% | -38.7% | -63 to -14 | -504 |
| proven pools | 63 | 44% | -17.9% | -30 to -6 | -1132 |

What-if exit rules on the SAME trades. Cells: avg return (trades, win rate).

| exit rule | momentum | control | dip | proven |
|---|---|---|---|---|
| base_sl30_tp100 | -63% (1297, 13%) | -19% (1827, 5%) | -39% (13, 8%) | -18% (63, 44%) |
| wide_sl50_tp100 | -63% (1297, 14%) | -19% (1827, 6%) | -45% (13, 8%) | -18% (63, 44%) |
| sl30_tp50 | -64% (1297, 16%) | -19% (1827, 6%) | -41% (13, 8%) | -19% (63, 44%) |
| sl50_tp50 | -64% (1297, 18%) | -19% (1827, 6%) | -48% (13, 8%) | -19% (63, 44%) |
| no_stop_tp100 | -63% (1297, 15%) | -19% (1827, 6%) | -43% (13, 8%) | -18% (63, 44%) |

Verdict: NOT ENOUGH DATA (need 30+ closed filter=1 trades and a CI above zero before believing anything).

Pools seen: 48729. Outcomes:

- missed_window: 32317
- low_liquidity: 8020
- proven_liquidity_gone: 3701
- no_momentum: 1883
- research_failed: 1313
- proven_low_volume: 699
- simulated failed buy: 592
- proven_price_collapsed_or_parabolic: 82
- proven: 65
- proven_no_uptrend: 28
- research_passed: 16
- dip: 13

Warning: 392 judged pools had an unreadable mint/freeze value. Check mint_raw / freeze_raw in candidates.csv; the parsing may need fixing.
