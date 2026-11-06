# Paper trader summary

SIMULATION ONLY. No real trades.

Updated 2026-11-06T13:27:56Z. Bankroll cash (research-selected trades): 743.1280659921765. Open positions: 19. Pools on watchlist: 57.

| group | n | win | avg | CI | P&L $ |
|---|---|---|---|---|---|
| research-picked | 10 | 30% | -25.5% | -65 to 19 | -257 |
| momentum, not picked | 853 | 14% | -59.6% | -64 to -55 | -50882 |
| all momentum | 863 | 14% | -59.2% | -63 to -55 | -51139 |
| control | 1014 | 7% | -20.0% | -22 to -18 | -20326 |
| dip buy | 9 | 11% | -43.3% | -77 to -6 | -390 |
| proven pools | 44 | 48% | -15.3% | -31 to -1 | -676 |

What-if exit rules on the SAME trades. Cells: avg return (trades, win rate).

| exit rule | momentum | control | dip | proven |
|---|---|---|---|---|
| base_sl30_tp100 | -60% (842, 14%) | -20% (1014, 7%) | -43% (9, 11%) | -15% (44, 48%) |
| wide_sl50_tp100 | -59% (842, 16%) | -20% (1014, 7%) | -47% (9, 11%) | -15% (44, 48%) |
| sl30_tp50 | -61% (842, 17%) | -20% (1014, 8%) | -47% (9, 11%) | -17% (44, 48%) |
| sl50_tp50 | -60% (842, 19%) | -21% (1014, 8%) | -50% (9, 11%) | -17% (44, 48%) |
| no_stop_tp100 | -59% (842, 17%) | -21% (1014, 7%) | -43% (9, 11%) | -15% (44, 48%) |

Verdict: NOT ENOUGH DATA (need 30+ closed filter=1 trades and a CI above zero before believing anything).

Pools seen: 29909. Outcomes:

- missed_window: 19453
- low_liquidity: 5432
- proven_liquidity_gone: 2305
- no_momentum: 1072
- research_failed: 858
- simulated failed buy: 358
- proven_low_volume: 292
- proven_price_collapsed_or_parabolic: 54
- proven: 44
- proven_no_uptrend: 22
- research_passed: 10
- dip: 9

Warning: 225 judged pools had an unreadable mint/freeze value. Check mint_raw / freeze_raw in candidates.csv; the parsing may need fixing.
