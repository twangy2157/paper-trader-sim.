# Paper trader summary

SIMULATION ONLY. No real trades.

Updated 2026-11-09T13:13:11Z. Bankroll cash (research-selected trades): 456.400154541351. Open positions: 16. Pools on watchlist: 48.

| group | n | win | avg | CI | P&L $ |
|---|---|---|---|---|---|
| research-picked | 16 | 25% | -33.9% | -64 to -3 | -544 |
| momentum, not picked | 1321 | 13% | -63.2% | -66 to -60 | -83601 |
| all momentum | 1337 | 13% | -62.8% | -66 to -60 | -84144 |
| control | 1848 | 5% | -18.8% | -20 to -17 | -34874 |
| dip buy | 13 | 8% | -38.7% | -63 to -14 | -504 |
| proven pools | 64 | 44% | -19.2% | -32 to -7 | -1233 |

What-if exit rules on the SAME trades. Cells: avg return (trades, win rate).

| exit rule | momentum | control | dip | proven |
|---|---|---|---|---|
| base_sl30_tp100 | -63% (1316, 13%) | -19% (1848, 5%) | -39% (13, 8%) | -19% (64, 44%) |
| wide_sl50_tp100 | -63% (1316, 15%) | -19% (1848, 6%) | -45% (13, 8%) | -19% (64, 44%) |
| sl30_tp50 | -64% (1316, 16%) | -19% (1848, 6%) | -41% (13, 8%) | -21% (64, 44%) |
| sl50_tp50 | -64% (1316, 18%) | -19% (1848, 6%) | -48% (13, 8%) | -21% (64, 44%) |
| no_stop_tp100 | -63% (1316, 15%) | -19% (1848, 6%) | -43% (13, 8%) | -19% (64, 44%) |

Verdict: NOT ENOUGH DATA (need 30+ closed filter=1 trades and a CI above zero before believing anything).

Pools seen: 49237. Outcomes:

- missed_window: 32690
- low_liquidity: 8063
- proven_liquidity_gone: 3743
- no_momentum: 1899
- research_failed: 1329
- proven_low_volume: 709
- simulated failed buy: 598
- proven_price_collapsed_or_parabolic: 83
- proven: 65
- proven_no_uptrend: 29
- research_passed: 16
- dip: 13

Warning: 398 judged pools had an unreadable mint/freeze value. Check mint_raw / freeze_raw in candidates.csv; the parsing may need fixing.
