# Paper trader summary

SIMULATION ONLY. No real trades.

Updated 2026-11-06T14:11:11Z. Bankroll cash (research-selected trades): 743.1280659921765. Open positions: 18. Pools on watchlist: 55.

| group | n | win | avg | CI | P&L $ |
|---|---|---|---|---|---|
| research-picked | 10 | 30% | -25.5% | -65 to 19 | -257 |
| momentum, not picked | 856 | 14% | -59.6% | -64 to -55 | -51090 |
| all momentum | 866 | 14% | -59.2% | -63 to -55 | -51347 |
| control | 1024 | 7% | -19.8% | -22 to -18 | -20390 |
| dip buy | 9 | 11% | -43.3% | -77 to -6 | -390 |
| proven pools | 44 | 48% | -15.3% | -31 to -1 | -676 |

What-if exit rules on the SAME trades. Cells: avg return (trades, win rate).

| exit rule | momentum | control | dip | proven |
|---|---|---|---|---|
| base_sl30_tp100 | -60% (845, 14%) | -20% (1024, 7%) | -43% (9, 11%) | -15% (44, 48%) |
| wide_sl50_tp100 | -59% (845, 16%) | -20% (1024, 7%) | -47% (9, 11%) | -15% (44, 48%) |
| sl30_tp50 | -61% (845, 17%) | -20% (1024, 8%) | -47% (9, 11%) | -17% (44, 48%) |
| sl50_tp50 | -60% (845, 19%) | -21% (1024, 8%) | -50% (9, 11%) | -17% (44, 48%) |
| no_stop_tp100 | -59% (845, 17%) | -21% (1024, 7%) | -43% (9, 11%) | -15% (44, 48%) |

Verdict: NOT ENOUGH DATA (need 30+ closed filter=1 trades and a CI above zero before believing anything).

Pools seen: 30080. Outcomes:

- missed_window: 19552
- low_liquidity: 5467
- proven_liquidity_gone: 2327
- no_momentum: 1077
- research_failed: 864
- simulated failed buy: 358
- proven_low_volume: 295
- proven_price_collapsed_or_parabolic: 54
- proven: 45
- proven_no_uptrend: 22
- research_passed: 10
- dip: 9

Warning: 226 judged pools had an unreadable mint/freeze value. Check mint_raw / freeze_raw in candidates.csv; the parsing may need fixing.
