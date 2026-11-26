# Paper trader summary

SIMULATION ONLY. No real trades.

Updated 2026-11-26T23:35:45Z. Bankroll cash (research-selected trades): 511.46918842262073. Open positions: 14. Pools on watchlist: 45.

| group | n | win | avg | CI | P&L $ |
|---|---|---|---|---|---|
| research-picked | 23 | 35% | -16.7% | -44 to 11 | -389 |
| momentum, not picked | 3884 | 12% | -65.6% | -68 to -64 | -255328 |
| all momentum | 3907 | 12% | -65.4% | -67 to -64 | -255716 |
| control | 4665 | 6% | -19.4% | -20 to -18 | -90933 |
| dip buy | 47 | 28% | -12.8% | -30 to 4 | -606 |
| proven pools | 135 | 33% | -31.2% | -40 to -23 | -4223 |

What-if exit rules on the SAME trades. Cells: avg return (trades, win rate).

| exit rule | momentum | control | dip | proven |
|---|---|---|---|---|
| base_sl30_tp100 | -66% (3886, 12%) | -19% (4665, 6%) | -13% (47, 28%) | -31% (135, 33%) |
| wide_sl50_tp100 | -65% (3886, 13%) | -20% (4665, 6%) | -13% (47, 32%) | -32% (135, 33%) |
| sl30_tp50 | -67% (3886, 14%) | -20% (4665, 7%) | -17% (47, 34%) | -31% (135, 33%) |
| sl50_tp50 | -67% (3886, 15%) | -20% (4665, 8%) | -18% (47, 38%) | -32% (135, 33%) |
| no_stop_tp100 | -65% (3886, 14%) | -20% (4665, 7%) | -12% (47, 32%) | -33% (135, 33%) |

Verdict: NOT ENOUGH DATA (need 30+ closed filter=1 trades and a CI above zero before believing anything).

Pools seen: 124993. Outcomes:

- missed_window: 80492
- low_liquidity: 21550
- proven_liquidity_gone: 10712
- no_momentum: 4716
- research_failed: 3890
- simulated failed buy: 1602
- proven_low_volume: 1587
- proven_price_collapsed_or_parabolic: 169
- proven: 135
- proven_no_uptrend: 69
- dip: 47
- research_passed: 24

Warning: 989 judged pools had an unreadable mint/freeze value. Check mint_raw / freeze_raw in candidates.csv; the parsing may need fixing.
