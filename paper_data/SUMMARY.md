# Paper trader summary

SIMULATION ONLY. No real trades.

Updated 2026-11-05T04:41:44Z. Bankroll cash (research-selected trades): 816.8065461812329. Open positions: 30. Pools on watchlist: 65.

| group | n | win | avg | CI | P&L $ |
|---|---|---|---|---|---|
| research-picked | 5 | 20% | -36.3% | - | -183 |
| momentum, not picked | 592 | 16% | -53.8% | -59 to -49 | -31872 |
| all momentum | 597 | 16% | -53.6% | -59 to -48 | -32055 |
| control | 715 | 7% | -19.0% | -22 to -16 | -13681 |
| dip buy | 4 | 25% | -13.1% | - | -52 |
| proven pools | 32 | 44% | -16.9% | -34 to -1 | -542 |

What-if exit rules on the SAME trades. Cells: avg return (trades, win rate).

| exit rule | momentum | control | dip | proven |
|---|---|---|---|---|
| base_sl30_tp100 | -54% (576, 16%) | -19% (715, 7%) | -13% (4, 25%) | -17% (32, 44%) |
| wide_sl50_tp100 | -54% (576, 18%) | -20% (715, 8%) | -13% (4, 25%) | -17% (32, 44%) |
| sl30_tp50 | -56% (576, 20%) | -19% (715, 8%) | -22% (4, 25%) | -18% (32, 44%) |
| sl50_tp50 | -55% (576, 22%) | -20% (715, 9%) | -22% (4, 25%) | -18% (32, 44%) |
| no_stop_tp100 | -53% (576, 19%) | -20% (715, 8%) | -13% (4, 25%) | -17% (32, 44%) |

Verdict: NOT ENOUGH DATA (need 30+ closed filter=1 trades and a CI above zero before believing anything).

Pools seen: 21412. Outcomes:

- missed_window: 14032
- low_liquidity: 3967
- proven_liquidity_gone: 1468
- no_momentum: 779
- research_failed: 599
- simulated failed buy: 241
- proven_low_volume: 216
- proven_price_collapsed_or_parabolic: 46
- proven: 35
- proven_no_uptrend: 20
- research_passed: 5
- dip: 4

Warning: 161 judged pools had an unreadable mint/freeze value. Check mint_raw / freeze_raw in candidates.csv; the parsing may need fixing.
