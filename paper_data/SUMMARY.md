# Paper trader summary

SIMULATION ONLY. No real trades.

Updated 2026-11-26T01:54:29Z. Bankroll cash (research-selected trades): 611.9691884226207. Open positions: 39. Pools on watchlist: 22.

| group | n | win | avg | CI | P&L $ |
|---|---|---|---|---|---|
| research-picked | 23 | 35% | -16.7% | -44 to 11 | -388 |
| momentum, not picked | 3792 | 12% | -65.5% | -67 to -64 | -248895 |
| all momentum | 3815 | 12% | -65.2% | -67 to -63 | -249284 |
| control | 4565 | 6% | -19.5% | -21 to -18 | -89204 |
| dip buy | 47 | 28% | -12.8% | -30 to 4 | -606 |
| proven pools | 135 | 33% | -31.2% | -40 to -23 | -4222 |

What-if exit rules on the SAME trades. Cells: avg return (trades, win rate).

| exit rule | momentum | control | dip | proven |
|---|---|---|---|---|
| base_sl30_tp100 | -65% (3794, 12%) | -19% (4565, 6%) | -13% (47, 28%) | -31% (135, 33%) |
| wide_sl50_tp100 | -65% (3794, 13%) | -20% (4565, 6%) | -13% (47, 32%) | -32% (135, 33%) |
| sl30_tp50 | -67% (3794, 14%) | -20% (4565, 7%) | -17% (47, 34%) | -31% (135, 33%) |
| sl50_tp50 | -67% (3794, 15%) | -20% (4565, 8%) | -18% (47, 38%) | -32% (135, 33%) |
| no_stop_tp100 | -65% (3794, 14%) | -20% (4565, 7%) | -12% (47, 32%) | -33% (135, 33%) |

Verdict: NOT ENOUGH DATA (need 30+ closed filter=1 trades and a CI above zero before believing anything).

Pools seen: 123112. Outcomes:

- missed_window: 79461
- low_liquidity: 21075
- proven_liquidity_gone: 10574
- no_momentum: 4632
- research_failed: 3808
- simulated failed buy: 1561
- proven_low_volume: 1561
- proven_price_collapsed_or_parabolic: 168
- proven: 135
- proven_no_uptrend: 67
- dip: 47
- research_passed: 23

Warning: 966 judged pools had an unreadable mint/freeze value. Check mint_raw / freeze_raw in candidates.csv; the parsing may need fixing.
