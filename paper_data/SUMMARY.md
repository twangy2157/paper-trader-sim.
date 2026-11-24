# Paper trader summary

SIMULATION ONLY. No real trades.

Updated 2026-11-24T14:06:33Z. Bankroll cash (research-selected trades): 454.67293770671824. Open positions: 24. Pools on watchlist: 44.

| group | n | win | avg | CI | P&L $ |
|---|---|---|---|---|---|
| research-picked | 21 | 33% | -21.1% | -50 to 9 | -445 |
| momentum, not picked | 3679 | 12% | -65.7% | -68 to -64 | -242149 |
| all momentum | 3700 | 12% | -65.5% | -67 to -64 | -242595 |
| control | 4435 | 6% | -19.3% | -20 to -18 | -86017 |
| dip buy | 47 | 28% | -12.8% | -30 to 4 | -606 |
| proven pools | 132 | 33% | -30.1% | -39 to -21 | -3989 |

What-if exit rules on the SAME trades. Cells: avg return (trades, win rate).

| exit rule | momentum | control | dip | proven |
|---|---|---|---|---|
| base_sl30_tp100 | -66% (3679, 12%) | -19% (4435, 6%) | -13% (47, 28%) | -30% (132, 33%) |
| wide_sl50_tp100 | -65% (3679, 13%) | -20% (4435, 6%) | -13% (47, 32%) | -31% (132, 33%) |
| sl30_tp50 | -67% (3679, 14%) | -19% (4435, 7%) | -17% (47, 34%) | -30% (132, 34%) |
| sl50_tp50 | -67% (3679, 15%) | -20% (4435, 8%) | -18% (47, 38%) | -31% (132, 34%) |
| no_stop_tp100 | -65% (3679, 14%) | -20% (4435, 7%) | -12% (47, 32%) | -32% (132, 33%) |

Verdict: NOT ENOUGH DATA (need 30+ closed filter=1 trades and a CI above zero before believing anything).

Pools seen: 120252. Outcomes:

- missed_window: 77689
- low_liquidity: 20573
- proven_liquidity_gone: 10337
- no_momentum: 4495
- research_failed: 3685
- proven_low_volume: 1522
- simulated failed buy: 1518
- proven_price_collapsed_or_parabolic: 166
- proven: 133
- proven_no_uptrend: 65
- dip: 47
- research_passed: 22

Warning: 944 judged pools had an unreadable mint/freeze value. Check mint_raw / freeze_raw in candidates.csv; the parsing may need fixing.
