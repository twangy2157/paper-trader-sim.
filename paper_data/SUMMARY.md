# Paper trader summary

SIMULATION ONLY. No real trades.

Updated 2026-11-05T03:34:56Z. Bankroll cash (research-selected trades): 816.8065461812329. Open positions: 16. Pools on watchlist: 41.

| group | n | win | avg | CI | P&L $ |
|---|---|---|---|---|---|
| research-picked | 5 | 20% | -36.3% | - | -183 |
| momentum, not picked | 583 | 16% | -54.1% | -59 to -49 | -31595 |
| all momentum | 588 | 16% | -54.0% | -59 to -49 | -31778 |
| control | 708 | 7% | -19.1% | -22 to -16 | -13595 |
| dip buy | 4 | 25% | -13.1% | - | -52 |
| proven pools | 32 | 44% | -16.9% | -34 to -1 | -542 |

What-if exit rules on the SAME trades. Cells: avg return (trades, win rate).

| exit rule | momentum | control | dip | proven |
|---|---|---|---|---|
| base_sl30_tp100 | -55% (567, 16%) | -19% (708, 7%) | -13% (4, 25%) | -17% (32, 44%) |
| wide_sl50_tp100 | -54% (567, 18%) | -20% (708, 7%) | -13% (4, 25%) | -17% (32, 44%) |
| sl30_tp50 | -56% (567, 20%) | -20% (708, 8%) | -22% (4, 25%) | -18% (32, 44%) |
| sl50_tp50 | -55% (567, 22%) | -20% (708, 9%) | -22% (4, 25%) | -18% (32, 44%) |
| no_stop_tp100 | -54% (567, 19%) | -20% (708, 8%) | -13% (4, 25%) | -17% (32, 44%) |

Verdict: NOT ENOUGH DATA (need 30+ closed filter=1 trades and a CI above zero before believing anything).

Pools seen: 21154. Outcomes:

- missed_window: 13890
- low_liquidity: 3924
- proven_liquidity_gone: 1434
- no_momentum: 758
- research_failed: 592
- simulated failed buy: 238
- proven_low_volume: 212
- proven_price_collapsed_or_parabolic: 44
- proven: 33
- proven_no_uptrend: 20
- research_passed: 5
- dip: 4

Warning: 159 judged pools had an unreadable mint/freeze value. Check mint_raw / freeze_raw in candidates.csv; the parsing may need fixing.
