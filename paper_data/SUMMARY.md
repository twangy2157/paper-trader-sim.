# Paper trader summary

SIMULATION ONLY. No real trades.

Updated 2026-11-05T00:05:38Z. Bankroll cash (research-selected trades): 816.8065461812329. Open positions: 14. Pools on watchlist: 27.

| group | n | win | avg | CI | P&L $ |
|---|---|---|---|---|---|
| research-picked | 5 | 20% | -36.3% | - | -183 |
| momentum, not picked | 552 | 16% | -53.8% | -59 to -49 | -29740 |
| all momentum | 557 | 16% | -53.6% | -59 to -48 | -29923 |
| control | 684 | 7% | -19.2% | -22 to -16 | -13171 |
| dip buy | 4 | 25% | -13.1% | - | -52 |
| proven pools | 31 | 42% | -17.5% | -35 to -1 | -545 |

What-if exit rules on the SAME trades. Cells: avg return (trades, win rate).

| exit rule | momentum | control | dip | proven |
|---|---|---|---|---|
| base_sl30_tp100 | -54% (536, 16%) | -19% (684, 7%) | -13% (4, 25%) | -18% (31, 42%) |
| wide_sl50_tp100 | -54% (536, 18%) | -20% (684, 8%) | -13% (4, 25%) | -18% (31, 42%) |
| sl30_tp50 | -55% (536, 20%) | -20% (684, 8%) | -22% (4, 25%) | -19% (31, 42%) |
| sl50_tp50 | -55% (536, 22%) | -20% (684, 9%) | -22% (4, 25%) | -19% (31, 42%) |
| no_stop_tp100 | -53% (536, 19%) | -20% (684, 8%) | -13% (4, 25%) | -18% (31, 42%) |

Verdict: NOT ENOUGH DATA (need 30+ closed filter=1 trades and a CI above zero before believing anything).

Pools seen: 20399. Outcomes:

- missed_window: 13435
- low_liquidity: 3772
- proven_liquidity_gone: 1369
- no_momentum: 735
- research_failed: 558
- simulated failed buy: 229
- proven_low_volume: 196
- proven_price_collapsed_or_parabolic: 44
- proven: 32
- proven_no_uptrend: 20
- research_passed: 5
- dip: 4

Warning: 153 judged pools had an unreadable mint/freeze value. Check mint_raw / freeze_raw in candidates.csv; the parsing may need fixing.
