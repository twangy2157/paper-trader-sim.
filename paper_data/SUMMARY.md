# Paper trader summary

SIMULATION ONLY. No real trades.

Updated 2026-11-02T14:56:44Z. Bankroll cash (research-selected trades): 898.5. Open positions: 19. Pools on watchlist: 87.

| group | n | win | avg | CI | P&L $ |
|---|---|---|---|---|---|
| research-picked | 1 | 0% | -101.0% | - | -102 |
| momentum, not picked | 137 | 15% | -50.1% | -60 to -39 | -6869 |
| all momentum | 138 | 14% | -50.4% | -60 to -40 | -6970 |
| control | 119 | 11% | -15.2% | -22 to -8 | -1815 |
| dip buy | 0 | - | - | - | 0 |
| proven pools | 0 | - | - | - | 0 |

What-if exit rules on the SAME trades. Cells: avg return (trades, win rate).

| exit rule | momentum | control | dip | proven |
|---|---|---|---|---|
| base_sl30_tp100 | -53% (117, 16%) | -15% (119, 11%) | - | - |
| wide_sl50_tp100 | -54% (117, 18%) | -16% (119, 11%) | - | - |
| sl30_tp50 | -54% (117, 20%) | -17% (119, 12%) | - | - |
| sl50_tp50 | -54% (117, 22%) | -17% (119, 13%) | - | - |
| no_stop_tp100 | -54% (117, 18%) | -16% (119, 11%) | - | - |

Verdict: NOT ENOUGH DATA (need 30+ closed filter=1 trades and a CI above zero before believing anything).

Pools seen: 5123. Outcomes:

- missed_window: 3355
- low_liquidity: 1403
- no_momentum: 172
- research_failed: 147
- simulated failed buy: 44
- research_passed: 1
- proven_liquidity_gone: 1

Warning: 28 judged pools had an unreadable mint/freeze value. Check mint_raw / freeze_raw in candidates.csv; the parsing may need fixing.
