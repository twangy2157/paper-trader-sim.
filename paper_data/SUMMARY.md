# Paper trader summary

SIMULATION ONLY. No real trades.

Updated 2026-11-05T14:43:41Z. Bankroll cash (research-selected trades): 749.6403049524637. Open positions: 19. Pools on watchlist: 49.

| group | n | win | avg | CI | P&L $ |
|---|---|---|---|---|---|
| research-picked | 8 | 25% | -31.0% | -68 to 8 | -250 |
| momentum, not picked | 664 | 15% | -55.5% | -60 to -51 | -36942 |
| all momentum | 672 | 15% | -55.3% | -60 to -51 | -37193 |
| control | 800 | 7% | -18.6% | -21 to -16 | -14986 |
| dip buy | 7 | 14% | -27.3% | -65 to 10 | -191 |
| proven pools | 38 | 42% | -17.9% | -34 to -2 | -681 |

What-if exit rules on the SAME trades. Cells: avg return (trades, win rate).

| exit rule | momentum | control | dip | proven |
|---|---|---|---|---|
| base_sl30_tp100 | -56% (651, 15%) | -19% (800, 7%) | -27% (7, 14%) | -18% (38, 42%) |
| wide_sl50_tp100 | -55% (651, 17%) | -19% (800, 8%) | -32% (7, 14%) | -18% (38, 42%) |
| sl30_tp50 | -57% (651, 19%) | -19% (800, 8%) | -32% (7, 14%) | -20% (38, 42%) |
| sl50_tp50 | -56% (651, 21%) | -19% (800, 9%) | -36% (7, 14%) | -20% (38, 42%) |
| no_stop_tp100 | -55% (651, 18%) | -19% (800, 8%) | -27% (7, 14%) | -18% (38, 42%) |

Verdict: NOT ENOUGH DATA (need 30+ closed filter=1 trades and a CI above zero before believing anything).

Pools seen: 23856. Outcomes:

- missed_window: 15560
- low_liquidity: 4411
- proven_liquidity_gone: 1729
- no_momentum: 852
- research_failed: 675
- simulated failed buy: 269
- proven_low_volume: 237
- proven_price_collapsed_or_parabolic: 48
- proven: 38
- proven_no_uptrend: 22
- research_passed: 8
- dip: 7

Warning: 175 judged pools had an unreadable mint/freeze value. Check mint_raw / freeze_raw in candidates.csv; the parsing may need fixing.
