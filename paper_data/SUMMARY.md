# Paper trader summary

SIMULATION ONLY. No real trades.

Updated 2026-11-04T06:31:11Z. Bankroll cash (research-selected trades): 860.0946161788225. Open positions: 19. Pools on watchlist: 51.

| group | n | win | avg | CI | P&L $ |
|---|---|---|---|---|---|
| research-picked | 2 | 0% | -69.5% | - | -140 |
| momentum, not picked | 427 | 15% | -54.0% | -60 to -48 | -23093 |
| all momentum | 429 | 15% | -54.1% | -60 to -48 | -23233 |
| control | 509 | 8% | -16.7% | -20 to -13 | -8573 |
| dip buy | 4 | 25% | -13.1% | - | -52 |
| proven pools | 19 | 32% | -30.3% | -54 to -10 | -577 |

What-if exit rules on the SAME trades. Cells: avg return (trades, win rate).

| exit rule | momentum | control | dip | proven |
|---|---|---|---|---|
| base_sl30_tp100 | -55% (408, 16%) | -17% (509, 8%) | -13% (4, 25%) | -30% (19, 32%) |
| wide_sl50_tp100 | -55% (408, 17%) | -17% (509, 8%) | -13% (4, 25%) | -30% (19, 32%) |
| sl30_tp50 | -57% (408, 19%) | -17% (509, 9%) | -22% (4, 25%) | -30% (19, 32%) |
| sl50_tp50 | -56% (408, 21%) | -17% (509, 9%) | -22% (4, 25%) | -30% (19, 32%) |
| no_stop_tp100 | -55% (408, 18%) | -18% (509, 8%) | -13% (4, 25%) | -30% (19, 32%) |

Verdict: NOT ENOUGH DATA (need 30+ closed filter=1 trades and a CI above zero before believing anything).

Pools seen: 16124. Outcomes:

- missed_window: 10710
- low_liquidity: 3070
- proven_liquidity_gone: 958
- no_momentum: 560
- research_failed: 437
- simulated failed buy: 176
- proven_low_volume: 150
- proven_price_collapsed_or_parabolic: 25
- proven: 21
- proven_no_uptrend: 11
- dip: 4
- research_passed: 2

Warning: 122 judged pools had an unreadable mint/freeze value. Check mint_raw / freeze_raw in candidates.csv; the parsing may need fixing.
