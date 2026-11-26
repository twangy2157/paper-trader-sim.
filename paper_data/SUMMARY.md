# Paper trader summary

SIMULATION ONLY. No real trades.

Updated 2026-11-26T13:20:32Z. Bankroll cash (research-selected trades): 611.9691884226207. Open positions: 9. Pools on watchlist: 45.

| group | n | win | avg | CI | P&L $ |
|---|---|---|---|---|---|
| research-picked | 23 | 35% | -16.7% | -44 to 11 | -388 |
| momentum, not picked | 3864 | 12% | -65.6% | -68 to -64 | -253962 |
| all momentum | 3887 | 12% | -65.3% | -67 to -64 | -254350 |
| control | 4645 | 6% | -19.4% | -21 to -18 | -90591 |
| dip buy | 47 | 28% | -12.8% | -30 to 4 | -606 |
| proven pools | 135 | 33% | -31.2% | -40 to -23 | -4223 |

What-if exit rules on the SAME trades. Cells: avg return (trades, win rate).

| exit rule | momentum | control | dip | proven |
|---|---|---|---|---|
| base_sl30_tp100 | -65% (3866, 12%) | -19% (4645, 6%) | -13% (47, 28%) | -31% (135, 33%) |
| wide_sl50_tp100 | -65% (3866, 13%) | -20% (4645, 6%) | -13% (47, 32%) | -32% (135, 33%) |
| sl30_tp50 | -67% (3866, 14%) | -20% (4645, 7%) | -17% (47, 34%) | -31% (135, 33%) |
| sl50_tp50 | -67% (3866, 15%) | -20% (4645, 7%) | -18% (47, 38%) | -32% (135, 33%) |
| no_stop_tp100 | -65% (3866, 14%) | -20% (4645, 7%) | -12% (47, 32%) | -33% (135, 33%) |

Verdict: NOT ENOUGH DATA (need 30+ closed filter=1 trades and a CI above zero before believing anything).

Pools seen: 124461. Outcomes:

- missed_window: 80224
- low_liquidity: 21365
- proven_liquidity_gone: 10698
- no_momentum: 4692
- research_failed: 3870
- proven_low_volume: 1585
- simulated failed buy: 1584
- proven_price_collapsed_or_parabolic: 169
- proven: 135
- proven_no_uptrend: 69
- dip: 47
- research_passed: 23

Warning: 978 judged pools had an unreadable mint/freeze value. Check mint_raw / freeze_raw in candidates.csv; the parsing may need fixing.
