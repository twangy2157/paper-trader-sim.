# Paper trader summary

SIMULATION ONLY. No real trades.

Updated 2026-11-06T18:57:52Z. Bankroll cash (research-selected trades): 743.1280659921765. Open positions: 14. Pools on watchlist: 48.

| group | n | win | avg | CI | P&L $ |
|---|---|---|---|---|---|
| research-picked | 10 | 30% | -25.5% | -65 to 19 | -257 |
| momentum, not picked | 862 | 13% | -59.8% | -64 to -56 | -51627 |
| all momentum | 872 | 14% | -59.4% | -64 to -56 | -51883 |
| control | 1029 | 7% | -19.8% | -22 to -17 | -20424 |
| dip buy | 9 | 11% | -43.3% | -77 to -6 | -390 |
| proven pools | 45 | 47% | -15.0% | -30 to -1 | -678 |

What-if exit rules on the SAME trades. Cells: avg return (trades, win rate).

| exit rule | momentum | control | dip | proven |
|---|---|---|---|---|
| base_sl30_tp100 | -60% (851, 14%) | -20% (1029, 7%) | -43% (9, 11%) | -15% (45, 47%) |
| wide_sl50_tp100 | -60% (851, 16%) | -20% (1029, 7%) | -47% (9, 11%) | -15% (45, 47%) |
| sl30_tp50 | -61% (851, 17%) | -20% (1029, 8%) | -47% (9, 11%) | -17% (45, 47%) |
| sl50_tp50 | -61% (851, 19%) | -20% (1029, 8%) | -50% (9, 11%) | -17% (45, 47%) |
| no_stop_tp100 | -59% (851, 16%) | -21% (1029, 7%) | -43% (9, 11%) | -15% (45, 47%) |

Verdict: NOT ENOUGH DATA (need 30+ closed filter=1 trades and a CI above zero before believing anything).

Pools seen: 30205. Outcomes:

- missed_window: 19644
- low_liquidity: 5478
- proven_liquidity_gone: 2340
- no_momentum: 1085
- research_failed: 864
- simulated failed buy: 359
- proven_low_volume: 295
- proven_price_collapsed_or_parabolic: 54
- proven: 45
- proven_no_uptrend: 22
- research_passed: 10
- dip: 9

Warning: 227 judged pools had an unreadable mint/freeze value. Check mint_raw / freeze_raw in candidates.csv; the parsing may need fixing.
