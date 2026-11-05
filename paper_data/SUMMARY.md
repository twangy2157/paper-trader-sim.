# Paper trader summary

SIMULATION ONLY. No real trades.

Updated 2026-11-05T02:11:08Z. Bankroll cash (research-selected trades): 816.8065461812329. Open positions: 27. Pools on watchlist: 76.

| group | n | win | avg | CI | P&L $ |
|---|---|---|---|---|---|
| research-picked | 5 | 20% | -36.3% | - | -183 |
| momentum, not picked | 567 | 15% | -54.5% | -60 to -50 | -30962 |
| all momentum | 572 | 15% | -54.4% | -59 to -49 | -31145 |
| control | 693 | 7% | -19.2% | -22 to -16 | -13395 |
| dip buy | 4 | 25% | -13.1% | - | -52 |
| proven pools | 32 | 44% | -16.9% | -34 to -1 | -542 |

What-if exit rules on the SAME trades. Cells: avg return (trades, win rate).

| exit rule | momentum | control | dip | proven |
|---|---|---|---|---|
| base_sl30_tp100 | -55% (551, 16%) | -19% (693, 7%) | -13% (4, 25%) | -17% (32, 44%) |
| wide_sl50_tp100 | -55% (551, 18%) | -20% (693, 8%) | -13% (4, 25%) | -17% (32, 44%) |
| sl30_tp50 | -56% (551, 20%) | -20% (693, 8%) | -22% (4, 25%) | -18% (32, 44%) |
| sl50_tp50 | -56% (551, 22%) | -20% (693, 9%) | -22% (4, 25%) | -18% (32, 44%) |
| no_stop_tp100 | -54% (551, 19%) | -20% (693, 8%) | -13% (4, 25%) | -17% (32, 44%) |

Verdict: NOT ENOUGH DATA (need 30+ closed filter=1 trades and a CI above zero before believing anything).

Pools seen: 20781. Outcomes:

- missed_window: 13646
- low_liquidity: 3855
- proven_liquidity_gone: 1405
- no_momentum: 749
- research_failed: 582
- simulated failed buy: 231
- proven_low_volume: 208
- proven_price_collapsed_or_parabolic: 44
- proven: 32
- proven_no_uptrend: 20
- research_passed: 5
- dip: 4

Warning: 156 judged pools had an unreadable mint/freeze value. Check mint_raw / freeze_raw in candidates.csv; the parsing may need fixing.
