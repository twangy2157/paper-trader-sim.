# Paper trader summary

SIMULATION ONLY. No real trades.

Updated 2026-11-08T00:18:10Z. Bankroll cash (research-selected trades): 399.4001435479087. Open positions: 24. Pools on watchlist: 75.

| group | n | win | avg | CI | P&L $ |
|---|---|---|---|---|---|
| research-picked | 14 | 21% | -35.6% | -66 to -4 | -501 |
| momentum, not picked | 1066 | 13% | -61.6% | -65 to -58 | -65722 |
| all momentum | 1080 | 13% | -61.2% | -65 to -58 | -66223 |
| control | 1413 | 6% | -19.7% | -22 to -18 | -27933 |
| dip buy | 11 | 9% | -40.6% | -69 to -11 | -447 |
| proven pools | 55 | 47% | -14.9% | -27 to -2 | -826 |

What-if exit rules on the SAME trades. Cells: avg return (trades, win rate).

| exit rule | momentum | control | dip | proven |
|---|---|---|---|---|
| base_sl30_tp100 | -62% (1059, 13%) | -20% (1413, 6%) | -41% (11, 9%) | -15% (55, 47%) |
| wide_sl50_tp100 | -62% (1059, 15%) | -20% (1413, 6%) | -48% (11, 9%) | -15% (55, 47%) |
| sl30_tp50 | -63% (1059, 16%) | -20% (1413, 7%) | -44% (11, 9%) | -17% (55, 47%) |
| sl50_tp50 | -62% (1059, 18%) | -20% (1413, 7%) | -52% (11, 9%) | -17% (55, 47%) |
| no_stop_tp100 | -61% (1059, 16%) | -20% (1413, 6%) | -45% (11, 9%) | -15% (55, 47%) |

Verdict: NOT ENOUGH DATA (need 30+ closed filter=1 trades and a CI above zero before believing anything).

Pools seen: 38506. Outcomes:

- missed_window: 25136
- low_liquidity: 6751
- proven_liquidity_gone: 2977
- no_momentum: 1472
- research_failed: 1074
- simulated failed buy: 468
- proven_low_volume: 458
- proven_price_collapsed_or_parabolic: 65
- proven: 55
- proven_no_uptrend: 24
- research_passed: 15
- dip: 11

Warning: 296 judged pools had an unreadable mint/freeze value. Check mint_raw / freeze_raw in candidates.csv; the parsing may need fixing.
