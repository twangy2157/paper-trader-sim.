# Paper trader summary

SIMULATION ONLY. No real trades.

Updated 2026-11-05T12:30:41Z. Bankroll cash (research-selected trades): 749.6403049524637. Open positions: 19. Pools on watchlist: 43.

| group | n | win | avg | CI | P&L $ |
|---|---|---|---|---|---|
| research-picked | 8 | 25% | -31.0% | -68 to 8 | -250 |
| momentum, not picked | 649 | 15% | -55.4% | -60 to -50 | -36001 |
| all momentum | 657 | 15% | -55.1% | -60 to -50 | -36252 |
| control | 782 | 7% | -18.7% | -21 to -16 | -14676 |
| dip buy | 6 | 17% | -25.8% | -68 to 15 | -155 |
| proven pools | 38 | 42% | -17.9% | -34 to -2 | -681 |

What-if exit rules on the SAME trades. Cells: avg return (trades, win rate).

| exit rule | momentum | control | dip | proven |
|---|---|---|---|---|
| base_sl30_tp100 | -56% (636, 15%) | -19% (782, 7%) | -26% (6, 17%) | -18% (38, 42%) |
| wide_sl50_tp100 | -56% (636, 17%) | -19% (782, 8%) | -26% (6, 17%) | -18% (38, 42%) |
| sl30_tp50 | -57% (636, 19%) | -19% (782, 8%) | -31% (6, 17%) | -20% (38, 42%) |
| sl50_tp50 | -56% (636, 21%) | -19% (782, 9%) | -31% (6, 17%) | -20% (38, 42%) |
| no_stop_tp100 | -55% (636, 18%) | -19% (782, 8%) | -26% (6, 17%) | -18% (38, 42%) |

Verdict: NOT ENOUGH DATA (need 30+ closed filter=1 trades and a CI above zero before believing anything).

Pools seen: 23223. Outcomes:

- missed_window: 15140
- low_liquidity: 4303
- proven_liquidity_gone: 1671
- no_momentum: 836
- research_failed: 657
- simulated failed buy: 264
- proven_low_volume: 231
- proven_price_collapsed_or_parabolic: 48
- proven: 38
- proven_no_uptrend: 20
- research_passed: 8
- dip: 7

Warning: 172 judged pools had an unreadable mint/freeze value. Check mint_raw / freeze_raw in candidates.csv; the parsing may need fixing.
