# Paper trader summary

SIMULATION ONLY. No real trades.

Updated 2026-11-05T04:30:38Z. Bankroll cash (research-selected trades): 816.8065461812329. Open positions: 27. Pools on watchlist: 56.

| group | n | win | avg | CI | P&L $ |
|---|---|---|---|---|---|
| research-picked | 5 | 20% | -36.3% | - | -183 |
| momentum, not picked | 590 | 16% | -53.6% | -59 to -48 | -31672 |
| all momentum | 595 | 16% | -53.5% | -58 to -48 | -31855 |
| control | 714 | 7% | -19.1% | -22 to -16 | -13675 |
| dip buy | 4 | 25% | -13.1% | - | -52 |
| proven pools | 32 | 44% | -16.9% | -34 to -1 | -542 |

What-if exit rules on the SAME trades. Cells: avg return (trades, win rate).

| exit rule | momentum | control | dip | proven |
|---|---|---|---|---|
| base_sl30_tp100 | -54% (574, 16%) | -19% (714, 7%) | -13% (4, 25%) | -17% (32, 44%) |
| wide_sl50_tp100 | -54% (574, 18%) | -20% (714, 8%) | -13% (4, 25%) | -17% (32, 44%) |
| sl30_tp50 | -55% (574, 20%) | -20% (714, 8%) | -22% (4, 25%) | -18% (32, 44%) |
| sl50_tp50 | -55% (574, 22%) | -20% (714, 9%) | -22% (4, 25%) | -18% (32, 44%) |
| no_stop_tp100 | -53% (574, 19%) | -20% (714, 8%) | -13% (4, 25%) | -17% (32, 44%) |

Verdict: NOT ENOUGH DATA (need 30+ closed filter=1 trades and a CI above zero before believing anything).

Pools seen: 21362. Outcomes:

- missed_window: 14001
- low_liquidity: 3960
- proven_liquidity_gone: 1463
- no_momentum: 774
- research_failed: 599
- simulated failed buy: 241
- proven_low_volume: 215
- proven_price_collapsed_or_parabolic: 46
- proven: 34
- proven_no_uptrend: 20
- research_passed: 5
- dip: 4

Warning: 161 judged pools had an unreadable mint/freeze value. Check mint_raw / freeze_raw in candidates.csv; the parsing may need fixing.
