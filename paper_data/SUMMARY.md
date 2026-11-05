# Paper trader summary

SIMULATION ONLY. No real trades.

Updated 2026-11-05T15:47:10Z. Bankroll cash (research-selected trades): 749.6403049524637. Open positions: 19. Pools on watchlist: 78.

| group | n | win | avg | CI | P&L $ |
|---|---|---|---|---|---|
| research-picked | 8 | 25% | -31.0% | -68 to 8 | -250 |
| momentum, not picked | 675 | 15% | -56.2% | -61 to -52 | -37982 |
| all momentum | 683 | 15% | -55.9% | -60 to -51 | -38232 |
| control | 809 | 7% | -18.7% | -21 to -16 | -15180 |
| dip buy | 7 | 14% | -27.3% | -65 to 10 | -191 |
| proven pools | 38 | 42% | -17.9% | -34 to -2 | -681 |

What-if exit rules on the SAME trades. Cells: avg return (trades, win rate).

| exit rule | momentum | control | dip | proven |
|---|---|---|---|---|
| base_sl30_tp100 | -56% (662, 15%) | -19% (809, 7%) | -27% (7, 14%) | -18% (38, 42%) |
| wide_sl50_tp100 | -56% (662, 17%) | -19% (809, 8%) | -32% (7, 14%) | -18% (38, 42%) |
| sl30_tp50 | -58% (662, 19%) | -19% (809, 8%) | -32% (7, 14%) | -20% (38, 42%) |
| sl50_tp50 | -57% (662, 21%) | -19% (809, 9%) | -36% (7, 14%) | -20% (38, 42%) |
| no_stop_tp100 | -56% (662, 18%) | -19% (809, 8%) | -27% (7, 14%) | -18% (38, 42%) |

Verdict: NOT ENOUGH DATA (need 30+ closed filter=1 trades and a CI above zero before believing anything).

Pools seen: 24211. Outcomes:

- missed_window: 15815
- low_liquidity: 4460
- proven_liquidity_gone: 1749
- no_momentum: 862
- research_failed: 685
- simulated failed buy: 278
- proven_low_volume: 239
- proven_price_collapsed_or_parabolic: 48
- proven: 38
- proven_no_uptrend: 22
- research_passed: 8
- dip: 7

Warning: 181 judged pools had an unreadable mint/freeze value. Check mint_raw / freeze_raw in candidates.csv; the parsing may need fixing.
