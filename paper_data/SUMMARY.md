# Paper trader summary

SIMULATION ONLY. No real trades.

Updated 2026-11-06T20:36:32Z. Bankroll cash (research-selected trades): 643.1280659921765. Open positions: 44. Pools on watchlist: 60.

| group | n | win | avg | CI | P&L $ |
|---|---|---|---|---|---|
| research-picked | 10 | 30% | -25.5% | -65 to 19 | -257 |
| momentum, not picked | 867 | 13% | -59.9% | -64 to -56 | -52043 |
| all momentum | 877 | 14% | -59.5% | -63 to -56 | -52300 |
| control | 1056 | 7% | -19.9% | -22 to -18 | -21103 |
| dip buy | 9 | 11% | -43.3% | -77 to -6 | -391 |
| proven pools | 45 | 47% | -15.0% | -30 to -1 | -678 |

What-if exit rules on the SAME trades. Cells: avg return (trades, win rate).

| exit rule | momentum | control | dip | proven |
|---|---|---|---|---|
| base_sl30_tp100 | -60% (856, 14%) | -20% (1056, 7%) | -43% (9, 11%) | -15% (45, 47%) |
| wide_sl50_tp100 | -60% (856, 16%) | -20% (1056, 7%) | -47% (9, 11%) | -15% (45, 47%) |
| sl30_tp50 | -61% (856, 17%) | -20% (1056, 7%) | -47% (9, 11%) | -17% (45, 47%) |
| sl50_tp50 | -61% (856, 19%) | -21% (1056, 8%) | -50% (9, 11%) | -17% (45, 47%) |
| no_stop_tp100 | -59% (856, 16%) | -21% (1056, 7%) | -43% (9, 11%) | -15% (45, 47%) |

Verdict: NOT ENOUGH DATA (need 30+ closed filter=1 trades and a CI above zero before believing anything).

Pools seen: 30683. Outcomes:

- missed_window: 19923
- low_liquidity: 5591
- proven_liquidity_gone: 2351
- no_momentum: 1130
- research_failed: 879
- simulated failed buy: 372
- proven_low_volume: 295
- proven_price_collapsed_or_parabolic: 54
- proven: 46
- proven_no_uptrend: 22
- research_passed: 11
- dip: 9

Warning: 237 judged pools had an unreadable mint/freeze value. Check mint_raw / freeze_raw in candidates.csv; the parsing may need fixing.
