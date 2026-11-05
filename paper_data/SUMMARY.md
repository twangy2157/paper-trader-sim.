# Paper trader summary

SIMULATION ONLY. No real trades.

Updated 2026-11-05T13:10:30Z. Bankroll cash (research-selected trades): 749.6403049524637. Open positions: 19. Pools on watchlist: 42.

| group | n | win | avg | CI | P&L $ |
|---|---|---|---|---|---|
| research-picked | 8 | 25% | -31.0% | -68 to 8 | -250 |
| momentum, not picked | 653 | 15% | -55.3% | -60 to -50 | -36171 |
| all momentum | 661 | 15% | -55.0% | -60 to -50 | -36421 |
| control | 786 | 7% | -18.7% | -21 to -16 | -14794 |
| dip buy | 6 | 17% | -25.8% | -68 to 15 | -155 |
| proven pools | 38 | 42% | -17.9% | -34 to -2 | -681 |

What-if exit rules on the SAME trades. Cells: avg return (trades, win rate).

| exit rule | momentum | control | dip | proven |
|---|---|---|---|---|
| base_sl30_tp100 | -56% (640, 15%) | -19% (786, 7%) | -26% (6, 17%) | -18% (38, 42%) |
| wide_sl50_tp100 | -56% (640, 17%) | -19% (786, 8%) | -26% (6, 17%) | -18% (38, 42%) |
| sl30_tp50 | -57% (640, 19%) | -19% (786, 8%) | -31% (6, 17%) | -20% (38, 42%) |
| sl50_tp50 | -56% (640, 21%) | -19% (786, 9%) | -31% (6, 17%) | -20% (38, 42%) |
| no_stop_tp100 | -55% (640, 18%) | -19% (786, 8%) | -26% (6, 17%) | -18% (38, 42%) |

Verdict: NOT ENOUGH DATA (need 30+ closed filter=1 trades and a CI above zero before believing anything).

Pools seen: 23357. Outcomes:

- missed_window: 15224
- low_liquidity: 4331
- proven_liquidity_gone: 1683
- no_momentum: 839
- research_failed: 662
- simulated failed buy: 266
- proven_low_volume: 231
- proven_price_collapsed_or_parabolic: 48
- proven: 38
- proven_no_uptrend: 20
- research_passed: 8
- dip: 7

Warning: 173 judged pools had an unreadable mint/freeze value. Check mint_raw / freeze_raw in candidates.csv; the parsing may need fixing.
