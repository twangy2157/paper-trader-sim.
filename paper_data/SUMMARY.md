# Paper trader summary

SIMULATION ONLY. No real trades.

Updated 2026-11-06T14:22:40Z. Bankroll cash (research-selected trades): 743.1280659921765. Open positions: 16. Pools on watchlist: 53.

| group | n | win | avg | CI | P&L $ |
|---|---|---|---|---|---|
| research-picked | 10 | 30% | -25.5% | -65 to 19 | -257 |
| momentum, not picked | 858 | 14% | -59.7% | -64 to -56 | -51290 |
| all momentum | 868 | 14% | -59.3% | -63 to -55 | -51547 |
| control | 1027 | 7% | -19.8% | -22 to -17 | -20415 |
| dip buy | 9 | 11% | -43.3% | -77 to -6 | -390 |
| proven pools | 44 | 48% | -15.3% | -31 to -1 | -676 |

What-if exit rules on the SAME trades. Cells: avg return (trades, win rate).

| exit rule | momentum | control | dip | proven |
|---|---|---|---|---|
| base_sl30_tp100 | -60% (847, 14%) | -20% (1027, 7%) | -43% (9, 11%) | -15% (44, 48%) |
| wide_sl50_tp100 | -60% (847, 16%) | -20% (1027, 7%) | -47% (9, 11%) | -15% (44, 48%) |
| sl30_tp50 | -61% (847, 17%) | -20% (1027, 8%) | -47% (9, 11%) | -17% (44, 48%) |
| sl50_tp50 | -61% (847, 19%) | -20% (1027, 8%) | -50% (9, 11%) | -17% (44, 48%) |
| no_stop_tp100 | -59% (847, 17%) | -21% (1027, 7%) | -43% (9, 11%) | -15% (44, 48%) |

Verdict: NOT ENOUGH DATA (need 30+ closed filter=1 trades and a CI above zero before believing anything).

Pools seen: 30138. Outcomes:

- missed_window: 19591
- low_liquidity: 5475
- proven_liquidity_gone: 2335
- no_momentum: 1080
- research_failed: 864
- simulated failed buy: 358
- proven_low_volume: 295
- proven_price_collapsed_or_parabolic: 54
- proven: 45
- proven_no_uptrend: 22
- research_passed: 10
- dip: 9

Warning: 226 judged pools had an unreadable mint/freeze value. Check mint_raw / freeze_raw in candidates.csv; the parsing may need fixing.
