# Paper trader summary

SIMULATION ONLY. No real trades.

Updated 2026-11-24T14:49:30Z. Bankroll cash (research-selected trades): 454.67293770671824. Open positions: 12. Pools on watchlist: 79.

| group | n | win | avg | CI | P&L $ |
|---|---|---|---|---|---|
| research-picked | 21 | 33% | -21.1% | -50 to 9 | -445 |
| momentum, not picked | 3685 | 12% | -65.8% | -68 to -64 | -242658 |
| all momentum | 3706 | 12% | -65.5% | -67 to -64 | -243103 |
| control | 4449 | 6% | -19.3% | -20 to -18 | -86400 |
| dip buy | 47 | 28% | -12.8% | -30 to 4 | -606 |
| proven pools | 132 | 33% | -30.1% | -39 to -21 | -3989 |

What-if exit rules on the SAME trades. Cells: avg return (trades, win rate).

| exit rule | momentum | control | dip | proven |
|---|---|---|---|---|
| base_sl30_tp100 | -66% (3685, 12%) | -19% (4449, 6%) | -13% (47, 28%) | -30% (132, 33%) |
| wide_sl50_tp100 | -65% (3685, 13%) | -20% (4449, 6%) | -13% (47, 32%) | -31% (132, 33%) |
| sl30_tp50 | -67% (3685, 14%) | -19% (4449, 7%) | -17% (47, 34%) | -30% (132, 34%) |
| sl50_tp50 | -67% (3685, 15%) | -20% (4449, 8%) | -18% (47, 38%) | -31% (132, 34%) |
| no_stop_tp100 | -65% (3685, 14%) | -20% (4449, 7%) | -12% (47, 32%) | -32% (132, 33%) |

Verdict: NOT ENOUGH DATA (need 30+ closed filter=1 trades and a CI above zero before believing anything).

Pools seen: 120458. Outcomes:

- missed_window: 77831
- low_liquidity: 20599
- proven_liquidity_gone: 10360
- no_momentum: 4501
- research_failed: 3687
- proven_low_volume: 1526
- simulated failed buy: 1520
- proven_price_collapsed_or_parabolic: 167
- proven: 133
- proven_no_uptrend: 65
- dip: 47
- research_passed: 22

Warning: 945 judged pools had an unreadable mint/freeze value. Check mint_raw / freeze_raw in candidates.csv; the parsing may need fixing.
