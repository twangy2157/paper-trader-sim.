# Paper trader summary

SIMULATION ONLY. No real trades.

Updated 2026-11-09T13:46:09Z. Bankroll cash (research-selected trades): 456.400154541351. Open positions: 20. Pools on watchlist: 72.

| group | n | win | avg | CI | P&L $ |
|---|---|---|---|---|---|
| research-picked | 16 | 25% | -33.9% | -64 to -3 | -544 |
| momentum, not picked | 1325 | 13% | -63.1% | -66 to -60 | -83759 |
| all momentum | 1341 | 13% | -62.8% | -66 to -60 | -84302 |
| control | 1851 | 5% | -18.7% | -20 to -17 | -34795 |
| dip buy | 13 | 8% | -38.7% | -63 to -14 | -504 |
| proven pools | 65 | 43% | -19.4% | -31 to -7 | -1266 |

What-if exit rules on the SAME trades. Cells: avg return (trades, win rate).

| exit rule | momentum | control | dip | proven |
|---|---|---|---|---|
| base_sl30_tp100 | -63% (1320, 13%) | -19% (1851, 5%) | -39% (13, 8%) | -19% (65, 43%) |
| wide_sl50_tp100 | -63% (1320, 15%) | -19% (1851, 6%) | -45% (13, 8%) | -20% (65, 43%) |
| sl30_tp50 | -64% (1320, 16%) | -19% (1851, 6%) | -41% (13, 8%) | -21% (65, 43%) |
| sl50_tp50 | -63% (1320, 18%) | -19% (1851, 6%) | -48% (13, 8%) | -21% (65, 43%) |
| no_stop_tp100 | -62% (1320, 15%) | -19% (1851, 6%) | -43% (13, 8%) | -20% (65, 43%) |

Verdict: NOT ENOUGH DATA (need 30+ closed filter=1 trades and a CI above zero before believing anything).

Pools seen: 49406. Outcomes:

- missed_window: 32805
- low_liquidity: 8095
- proven_liquidity_gone: 3748
- no_momentum: 1905
- research_failed: 1334
- proven_low_volume: 712
- simulated failed buy: 599
- proven_price_collapsed_or_parabolic: 83
- proven: 66
- proven_no_uptrend: 30
- research_passed: 16
- dip: 13

Warning: 399 judged pools had an unreadable mint/freeze value. Check mint_raw / freeze_raw in candidates.csv; the parsing may need fixing.
