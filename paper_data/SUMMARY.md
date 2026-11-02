# Paper trader summary

SIMULATION ONLY. No real trades.

Updated 2026-11-02T17:23:32Z. Bankroll cash (research-selected trades): 898.5. Open positions: 21. Pools on watchlist: 65.

| group | n | win | avg | CI | P&L $ |
|---|---|---|---|---|---|
| research-picked | 1 | 0% | -101.0% | - | -102 |
| momentum, not picked | 160 | 15% | -51.9% | -61 to -42 | -8324 |
| all momentum | 161 | 15% | -52.2% | -61 to -43 | -8426 |
| control | 140 | 11% | -16.0% | -23 to -9 | -2246 |
| dip buy | 0 | - | - | - | 0 |
| proven pools | 0 | - | - | - | 0 |

What-if exit rules on the SAME trades. Cells: avg return (trades, win rate).

| exit rule | momentum | control | dip | proven |
|---|---|---|---|---|
| base_sl30_tp100 | -55% (140, 16%) | -16% (140, 11%) | - | - |
| wide_sl50_tp100 | -55% (140, 18%) | -17% (140, 11%) | - | - |
| sl30_tp50 | -56% (140, 20%) | -18% (140, 11%) | - | - |
| sl50_tp50 | -55% (140, 22%) | -18% (140, 12%) | - | - |
| no_stop_tp100 | -55% (140, 19%) | -17% (140, 11%) | - | - |

Verdict: NOT ENOUGH DATA (need 30+ closed filter=1 trades and a CI above zero before believing anything).

Pools seen: 5889. Outcomes:

- missed_window: 3875
- low_liquidity: 1519
- no_momentum: 191
- research_failed: 173
- proven_liquidity_gone: 70
- simulated failed buy: 53
- proven_low_volume: 6
- research_passed: 1
- proven: 1

Warning: 34 judged pools had an unreadable mint/freeze value. Check mint_raw / freeze_raw in candidates.csv; the parsing may need fixing.
