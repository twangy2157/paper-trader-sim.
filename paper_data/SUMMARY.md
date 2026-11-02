# Paper trader summary

SIMULATION ONLY. No real trades.

Updated 2026-11-02T17:02:56Z. Bankroll cash (research-selected trades): 898.5. Open positions: 19. Pools on watchlist: 58.

| group | n | win | avg | CI | P&L $ |
|---|---|---|---|---|---|
| research-picked | 1 | 0% | -101.0% | - | -102 |
| momentum, not picked | 157 | 15% | -51.6% | -61 to -42 | -8119 |
| all momentum | 158 | 15% | -51.9% | -61 to -42 | -8220 |
| control | 136 | 11% | -15.6% | -23 to -9 | -2126 |
| dip buy | 0 | - | - | - | 0 |
| proven pools | 0 | - | - | - | 0 |

What-if exit rules on the SAME trades. Cells: avg return (trades, win rate).

| exit rule | momentum | control | dip | proven |
|---|---|---|---|---|
| base_sl30_tp100 | -54% (137, 17%) | -16% (136, 11%) | - | - |
| wide_sl50_tp100 | -55% (137, 18%) | -16% (136, 11%) | - | - |
| sl30_tp50 | -55% (137, 20%) | -18% (136, 12%) | - | - |
| sl50_tp50 | -55% (137, 23%) | -18% (136, 12%) | - | - |
| no_stop_tp100 | -54% (137, 19%) | -17% (136, 11%) | - | - |

Verdict: NOT ENOUGH DATA (need 30+ closed filter=1 trades and a CI above zero before believing anything).

Pools seen: 5791. Outcomes:

- missed_window: 3812
- low_liquidity: 1506
- no_momentum: 186
- research_failed: 170
- proven_liquidity_gone: 59
- simulated failed buy: 51
- proven_low_volume: 6
- research_passed: 1

Warning: 32 judged pools had an unreadable mint/freeze value. Check mint_raw / freeze_raw in candidates.csv; the parsing may need fixing.
