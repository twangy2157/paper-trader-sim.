# Paper trader summary

SIMULATION ONLY. No real trades.

Updated 2026-11-25T08:55:31Z. Bankroll cash (research-selected trades): 611.9691884226207. Open positions: 27. Pools on watchlist: 36.

| group | n | win | avg | CI | P&L $ |
|---|---|---|---|---|---|
| research-picked | 23 | 35% | -16.7% | -44 to 11 | -388 |
| momentum, not picked | 3743 | 12% | -65.6% | -67 to -64 | -245948 |
| all momentum | 3766 | 12% | -65.3% | -67 to -63 | -246336 |
| control | 4514 | 6% | -19.4% | -20 to -18 | -87850 |
| dip buy | 47 | 28% | -12.8% | -30 to 4 | -606 |
| proven pools | 134 | 33% | -30.7% | -39 to -22 | -4122 |

What-if exit rules on the SAME trades. Cells: avg return (trades, win rate).

| exit rule | momentum | control | dip | proven |
|---|---|---|---|---|
| base_sl30_tp100 | -65% (3745, 12%) | -19% (4514, 6%) | -13% (47, 28%) | -31% (134, 33%) |
| wide_sl50_tp100 | -65% (3745, 13%) | -20% (4514, 6%) | -13% (47, 32%) | -32% (134, 33%) |
| sl30_tp50 | -67% (3745, 14%) | -19% (4514, 7%) | -17% (47, 34%) | -31% (134, 34%) |
| sl50_tp50 | -67% (3745, 15%) | -20% (4514, 8%) | -18% (47, 38%) | -32% (134, 34%) |
| no_stop_tp100 | -65% (3745, 14%) | -20% (4514, 7%) | -12% (47, 32%) | -32% (134, 33%) |

Verdict: NOT ENOUGH DATA (need 30+ closed filter=1 trades and a CI above zero before believing anything).

Pools seen: 121981. Outcomes:

- missed_window: 78705
- low_liquidity: 20919
- proven_liquidity_gone: 10499
- no_momentum: 4570
- research_failed: 3758
- proven_low_volume: 1546
- simulated failed buy: 1545
- proven_price_collapsed_or_parabolic: 168
- proven: 134
- proven_no_uptrend: 67
- dip: 47
- research_passed: 23

Warning: 957 judged pools had an unreadable mint/freeze value. Check mint_raw / freeze_raw in candidates.csv; the parsing may need fixing.
