# Paper trader summary

SIMULATION ONLY. No real trades.

Updated 2026-11-06T20:46:42Z. Bankroll cash (research-selected trades): 643.1280659921765. Open positions: 43. Pools on watchlist: 62.

| group | n | win | avg | CI | P&L $ |
|---|---|---|---|---|---|
| research-picked | 10 | 30% | -25.5% | -65 to 19 | -257 |
| momentum, not picked | 871 | 13% | -60.1% | -64 to -56 | -52443 |
| all momentum | 881 | 14% | -59.7% | -64 to -56 | -52700 |
| control | 1058 | 7% | -19.9% | -22 to -18 | -21115 |
| dip buy | 9 | 11% | -43.3% | -77 to -6 | -391 |
| proven pools | 45 | 47% | -15.0% | -30 to -1 | -678 |

What-if exit rules on the SAME trades. Cells: avg return (trades, win rate).

| exit rule | momentum | control | dip | proven |
|---|---|---|---|---|
| base_sl30_tp100 | -60% (860, 14%) | -20% (1058, 7%) | -43% (9, 11%) | -15% (45, 47%) |
| wide_sl50_tp100 | -60% (860, 15%) | -20% (1058, 7%) | -47% (9, 11%) | -15% (45, 47%) |
| sl30_tp50 | -62% (860, 17%) | -20% (1058, 7%) | -47% (9, 11%) | -17% (45, 47%) |
| sl50_tp50 | -61% (860, 19%) | -21% (1058, 8%) | -50% (9, 11%) | -17% (45, 47%) |
| no_stop_tp100 | -60% (860, 16%) | -21% (1058, 7%) | -43% (9, 11%) | -15% (45, 47%) |

Verdict: NOT ENOUGH DATA (need 30+ closed filter=1 trades and a CI above zero before believing anything).

Pools seen: 30722. Outcomes:

- missed_window: 19945
- low_liquidity: 5601
- proven_liquidity_gone: 2351
- no_momentum: 1134
- research_failed: 880
- simulated failed buy: 374
- proven_low_volume: 295
- proven_price_collapsed_or_parabolic: 54
- proven: 46
- proven_no_uptrend: 22
- research_passed: 11
- dip: 9

Warning: 238 judged pools had an unreadable mint/freeze value. Check mint_raw / freeze_raw in candidates.csv; the parsing may need fixing.
