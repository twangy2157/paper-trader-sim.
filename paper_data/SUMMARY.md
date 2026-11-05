# Paper trader summary

SIMULATION ONLY. No real trades.

Updated 2026-11-05T12:40:57Z. Bankroll cash (research-selected trades): 749.6403049524637. Open positions: 19. Pools on watchlist: 35.

| group | n | win | avg | CI | P&L $ |
|---|---|---|---|---|---|
| research-picked | 8 | 25% | -31.0% | -68 to 8 | -250 |
| momentum, not picked | 650 | 15% | -55.5% | -60 to -51 | -36102 |
| all momentum | 658 | 15% | -55.2% | -60 to -50 | -36352 |
| control | 783 | 7% | -18.7% | -21 to -16 | -14684 |
| dip buy | 6 | 17% | -25.8% | -68 to 15 | -155 |
| proven pools | 38 | 42% | -17.9% | -34 to -2 | -681 |

What-if exit rules on the SAME trades. Cells: avg return (trades, win rate).

| exit rule | momentum | control | dip | proven |
|---|---|---|---|---|
| base_sl30_tp100 | -56% (637, 15%) | -19% (783, 7%) | -26% (6, 17%) | -18% (38, 42%) |
| wide_sl50_tp100 | -56% (637, 17%) | -19% (783, 8%) | -26% (6, 17%) | -18% (38, 42%) |
| sl30_tp50 | -57% (637, 19%) | -19% (783, 8%) | -31% (6, 17%) | -20% (38, 42%) |
| sl50_tp50 | -57% (637, 21%) | -19% (783, 9%) | -31% (6, 17%) | -20% (38, 42%) |
| no_stop_tp100 | -55% (637, 18%) | -19% (783, 8%) | -26% (6, 17%) | -18% (38, 42%) |

Verdict: NOT ENOUGH DATA (need 30+ closed filter=1 trades and a CI above zero before believing anything).

Pools seen: 23268. Outcomes:

- missed_window: 15167
- low_liquidity: 4311
- proven_liquidity_gone: 1678
- no_momentum: 836
- research_failed: 659
- simulated failed buy: 265
- proven_low_volume: 231
- proven_price_collapsed_or_parabolic: 48
- proven: 38
- proven_no_uptrend: 20
- research_passed: 8
- dip: 7

Warning: 172 judged pools had an unreadable mint/freeze value. Check mint_raw / freeze_raw in candidates.csv; the parsing may need fixing.
