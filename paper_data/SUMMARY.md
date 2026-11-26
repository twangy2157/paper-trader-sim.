# Paper trader summary

SIMULATION ONLY. No real trades.

Updated 2026-11-26T12:38:40Z. Bankroll cash (research-selected trades): 611.9691884226207. Open positions: 20. Pools on watchlist: 44.

| group | n | win | avg | CI | P&L $ |
|---|---|---|---|---|---|
| research-picked | 23 | 35% | -16.7% | -44 to 11 | -388 |
| momentum, not picked | 3855 | 12% | -65.6% | -67 to -64 | -253357 |
| all momentum | 3878 | 12% | -65.3% | -67 to -63 | -253745 |
| control | 4636 | 6% | -19.4% | -20 to -18 | -90286 |
| dip buy | 47 | 28% | -12.8% | -30 to 4 | -606 |
| proven pools | 135 | 33% | -31.2% | -40 to -23 | -4223 |

What-if exit rules on the SAME trades. Cells: avg return (trades, win rate).

| exit rule | momentum | control | dip | proven |
|---|---|---|---|---|
| base_sl30_tp100 | -65% (3857, 12%) | -19% (4636, 6%) | -13% (47, 28%) | -31% (135, 33%) |
| wide_sl50_tp100 | -65% (3857, 13%) | -20% (4636, 6%) | -13% (47, 32%) | -32% (135, 33%) |
| sl30_tp50 | -67% (3857, 14%) | -19% (4636, 7%) | -17% (47, 34%) | -31% (135, 33%) |
| sl50_tp50 | -67% (3857, 15%) | -20% (4636, 7%) | -18% (47, 38%) | -32% (135, 33%) |
| no_stop_tp100 | -65% (3857, 14%) | -20% (4636, 7%) | -12% (47, 32%) | -33% (135, 33%) |

Verdict: NOT ENOUGH DATA (need 30+ closed filter=1 trades and a CI above zero before believing anything).

Pools seen: 124307. Outcomes:

- missed_window: 80130
- low_liquidity: 21339
- proven_liquidity_gone: 10672
- no_momentum: 4689
- research_failed: 3866
- simulated failed buy: 1584
- proven_low_volume: 1584
- proven_price_collapsed_or_parabolic: 169
- proven: 135
- proven_no_uptrend: 69
- dip: 47
- research_passed: 23

Warning: 978 judged pools had an unreadable mint/freeze value. Check mint_raw / freeze_raw in candidates.csv; the parsing may need fixing.
