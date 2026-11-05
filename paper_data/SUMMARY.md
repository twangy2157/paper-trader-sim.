# Paper trader summary

SIMULATION ONLY. No real trades.

Updated 2026-11-05T05:03:32Z. Bankroll cash (research-selected trades): 816.8065461812329. Open positions: 26. Pools on watchlist: 29.

| group | n | win | avg | CI | P&L $ |
|---|---|---|---|---|---|
| research-picked | 5 | 20% | -36.3% | - | -183 |
| momentum, not picked | 596 | 16% | -53.8% | -59 to -49 | -32112 |
| all momentum | 601 | 16% | -53.6% | -59 to -49 | -32295 |
| control | 720 | 7% | -19.0% | -22 to -16 | -13733 |
| dip buy | 4 | 25% | -13.1% | - | -52 |
| proven pools | 32 | 44% | -16.9% | -34 to -1 | -542 |

What-if exit rules on the SAME trades. Cells: avg return (trades, win rate).

| exit rule | momentum | control | dip | proven |
|---|---|---|---|---|
| base_sl30_tp100 | -54% (580, 16%) | -19% (720, 7%) | -13% (4, 25%) | -17% (32, 44%) |
| wide_sl50_tp100 | -54% (580, 18%) | -20% (720, 8%) | -13% (4, 25%) | -17% (32, 44%) |
| sl30_tp50 | -56% (580, 20%) | -19% (720, 8%) | -22% (4, 25%) | -18% (32, 44%) |
| sl50_tp50 | -55% (580, 22%) | -20% (720, 9%) | -22% (4, 25%) | -18% (32, 44%) |
| no_stop_tp100 | -53% (580, 19%) | -20% (720, 8%) | -13% (4, 25%) | -17% (32, 44%) |

Verdict: NOT ENOUGH DATA (need 30+ closed filter=1 trades and a CI above zero before believing anything).

Pools seen: 21520. Outcomes:

- missed_window: 14111
- low_liquidity: 3980
- proven_liquidity_gone: 1476
- no_momentum: 782
- research_failed: 601
- simulated failed buy: 242
- proven_low_volume: 218
- proven_price_collapsed_or_parabolic: 46
- proven: 35
- proven_no_uptrend: 20
- research_passed: 5
- dip: 4

Warning: 162 judged pools had an unreadable mint/freeze value. Check mint_raw / freeze_raw in candidates.csv; the parsing may need fixing.
