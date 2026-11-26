# Paper trader summary

SIMULATION ONLY. No real trades.

Updated 2026-11-26T08:56:38Z. Bankroll cash (research-selected trades): 611.9691884226207. Open positions: 31. Pools on watchlist: 51.

| group | n | win | avg | CI | P&L $ |
|---|---|---|---|---|---|
| research-picked | 23 | 35% | -16.7% | -44 to 11 | -388 |
| momentum, not picked | 3815 | 12% | -65.7% | -68 to -64 | -250954 |
| all momentum | 3838 | 12% | -65.4% | -67 to -63 | -251342 |
| control | 4595 | 6% | -19.4% | -20 to -18 | -89572 |
| dip buy | 47 | 28% | -12.8% | -30 to 4 | -606 |
| proven pools | 135 | 33% | -31.2% | -40 to -23 | -4223 |

What-if exit rules on the SAME trades. Cells: avg return (trades, win rate).

| exit rule | momentum | control | dip | proven |
|---|---|---|---|---|
| base_sl30_tp100 | -66% (3817, 12%) | -19% (4595, 6%) | -13% (47, 28%) | -31% (135, 33%) |
| wide_sl50_tp100 | -65% (3817, 13%) | -20% (4595, 6%) | -13% (47, 32%) | -32% (135, 33%) |
| sl30_tp50 | -67% (3817, 14%) | -19% (4595, 7%) | -17% (47, 34%) | -31% (135, 33%) |
| sl50_tp50 | -67% (3817, 15%) | -20% (4595, 8%) | -18% (47, 38%) | -32% (135, 33%) |
| no_stop_tp100 | -65% (3817, 14%) | -20% (4595, 7%) | -12% (47, 32%) | -33% (135, 33%) |

Verdict: NOT ENOUGH DATA (need 30+ closed filter=1 trades and a CI above zero before believing anything).

Pools seen: 123614. Outcomes:

- missed_window: 79753
- low_liquidity: 21194
- proven_liquidity_gone: 10604
- no_momentum: 4656
- research_failed: 3829
- simulated failed buy: 1571
- proven_low_volume: 1567
- proven_price_collapsed_or_parabolic: 168
- proven: 135
- proven_no_uptrend: 67
- dip: 47
- research_passed: 23

Warning: 974 judged pools had an unreadable mint/freeze value. Check mint_raw / freeze_raw in candidates.csv; the parsing may need fixing.
