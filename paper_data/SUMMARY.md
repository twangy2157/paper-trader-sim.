# Paper trader summary

SIMULATION ONLY. No real trades.

Updated 2026-11-27T09:06:55Z. Bankroll cash (research-selected trades): 513.2029228559132. Open positions: 37. Pools on watchlist: 42.

| group | n | win | avg | CI | P&L $ |
|---|---|---|---|---|---|
| research-picked | 24 | 33% | -20.1% | -46 to 6 | -487 |
| momentum, not picked | 3920 | 12% | -65.5% | -67 to -64 | -257017 |
| all momentum | 3944 | 12% | -65.2% | -67 to -63 | -257503 |
| control | 4707 | 6% | -19.4% | -20 to -18 | -91751 |
| dip buy | 47 | 28% | -12.8% | -30 to 4 | -606 |
| proven pools | 135 | 33% | -31.2% | -40 to -23 | -4223 |

What-if exit rules on the SAME trades. Cells: avg return (trades, win rate).

| exit rule | momentum | control | dip | proven |
|---|---|---|---|---|
| base_sl30_tp100 | -65% (3923, 12%) | -19% (4707, 6%) | -13% (47, 28%) | -31% (135, 33%) |
| wide_sl50_tp100 | -65% (3923, 13%) | -20% (4707, 6%) | -13% (47, 32%) | -32% (135, 33%) |
| sl30_tp50 | -67% (3923, 14%) | -20% (4707, 7%) | -17% (47, 34%) | -31% (135, 33%) |
| sl50_tp50 | -67% (3923, 15%) | -20% (4707, 7%) | -18% (47, 38%) | -32% (135, 33%) |
| no_stop_tp100 | -65% (3923, 14%) | -20% (4707, 7%) | -12% (47, 32%) | -33% (135, 33%) |

Verdict: NOT ENOUGH DATA (need 30+ closed filter=1 trades and a CI above zero before believing anything).

Pools seen: 126102. Outcomes:

- missed_window: 81146
- low_liquidity: 21780
- proven_liquidity_gone: 10803
- no_momentum: 4768
- research_failed: 3940
- simulated failed buy: 1616
- proven_low_volume: 1605
- proven_price_collapsed_or_parabolic: 169
- proven: 135
- proven_no_uptrend: 69
- dip: 47
- research_passed: 24

Warning: 998 judged pools had an unreadable mint/freeze value. Check mint_raw / freeze_raw in candidates.csv; the parsing may need fixing.
