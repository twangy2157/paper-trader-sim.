# Paper trader summary

SIMULATION ONLY. No real trades.

Updated 2026-11-09T18:03:09Z. Bankroll cash (research-selected trades): 456.400154541351. Open positions: 34. Pools on watchlist: 60.

| group | n | win | avg | CI | P&L $ |
|---|---|---|---|---|---|
| research-picked | 16 | 25% | -33.9% | -64 to -3 | -544 |
| momentum, not picked | 1354 | 13% | -63.5% | -66 to -60 | -86113 |
| all momentum | 1370 | 13% | -63.2% | -66 to -60 | -86656 |
| control | 1908 | 5% | -18.7% | -20 to -17 | -35801 |
| dip buy | 13 | 8% | -38.7% | -63 to -14 | -504 |
| proven pools | 74 | 38% | -26.0% | -38 to -14 | -1931 |

What-if exit rules on the SAME trades. Cells: avg return (trades, win rate).

| exit rule | momentum | control | dip | proven |
|---|---|---|---|---|
| base_sl30_tp100 | -64% (1349, 13%) | -19% (1908, 5%) | -39% (13, 8%) | -26% (74, 38%) |
| wide_sl50_tp100 | -63% (1349, 14%) | -19% (1908, 6%) | -45% (13, 8%) | -26% (74, 38%) |
| sl30_tp50 | -64% (1349, 16%) | -19% (1908, 6%) | -41% (13, 8%) | -27% (74, 38%) |
| sl50_tp50 | -64% (1349, 17%) | -19% (1908, 6%) | -48% (13, 8%) | -28% (74, 38%) |
| no_stop_tp100 | -63% (1349, 15%) | -19% (1908, 6%) | -43% (13, 8%) | -27% (74, 38%) |

Verdict: NOT ENOUGH DATA (need 30+ closed filter=1 trades and a CI above zero before believing anything).

Pools seen: 50828. Outcomes:

- missed_window: 33851
- low_liquidity: 8218
- proven_liquidity_gone: 3837
- no_momentum: 1980
- research_failed: 1360
- proven_low_volume: 737
- simulated failed buy: 625
- proven_price_collapsed_or_parabolic: 86
- proven: 74
- proven_no_uptrend: 31
- research_passed: 16
- dip: 13

Warning: 420 judged pools had an unreadable mint/freeze value. Check mint_raw / freeze_raw in candidates.csv; the parsing may need fixing.
