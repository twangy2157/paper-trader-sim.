# Paper trader summary

SIMULATION ONLY. No real trades.

Updated 2026-11-06T20:03:44Z. Bankroll cash (research-selected trades): 643.1280659921765. Open positions: 45. Pools on watchlist: 63.

| group | n | win | avg | CI | P&L $ |
|---|---|---|---|---|---|
| research-picked | 10 | 30% | -25.5% | -65 to 19 | -257 |
| momentum, not picked | 865 | 13% | -59.9% | -64 to -56 | -51871 |
| all momentum | 875 | 14% | -59.5% | -64 to -55 | -52128 |
| control | 1041 | 7% | -20.0% | -22 to -18 | -20871 |
| dip buy | 9 | 11% | -43.3% | -77 to -6 | -391 |
| proven pools | 45 | 47% | -15.0% | -30 to -1 | -678 |

What-if exit rules on the SAME trades. Cells: avg return (trades, win rate).

| exit rule | momentum | control | dip | proven |
|---|---|---|---|---|
| base_sl30_tp100 | -60% (854, 14%) | -20% (1041, 7%) | -43% (9, 11%) | -15% (45, 47%) |
| wide_sl50_tp100 | -60% (854, 16%) | -20% (1041, 7%) | -47% (9, 11%) | -15% (45, 47%) |
| sl30_tp50 | -61% (854, 17%) | -20% (1041, 7%) | -47% (9, 11%) | -17% (45, 47%) |
| sl50_tp50 | -61% (854, 19%) | -21% (1041, 8%) | -50% (9, 11%) | -17% (45, 47%) |
| no_stop_tp100 | -59% (854, 17%) | -21% (1041, 7%) | -43% (9, 11%) | -15% (45, 47%) |

Verdict: NOT ENOUGH DATA (need 30+ closed filter=1 trades and a CI above zero before believing anything).

Pools seen: 30547. Outcomes:

- missed_window: 19840
- low_liquidity: 5556
- proven_liquidity_gone: 2351
- no_momentum: 1120
- research_failed: 873
- simulated failed buy: 370
- proven_low_volume: 295
- proven_price_collapsed_or_parabolic: 54
- proven: 46
- proven_no_uptrend: 22
- research_passed: 11
- dip: 9

Warning: 237 judged pools had an unreadable mint/freeze value. Check mint_raw / freeze_raw in candidates.csv; the parsing may need fixing.
