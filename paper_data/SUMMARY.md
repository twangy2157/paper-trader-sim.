# Paper trader summary

SIMULATION ONLY. No real trades.

Updated 2026-11-05T17:21:29Z. Bankroll cash (research-selected trades): 749.6403049524637. Open positions: 32. Pools on watchlist: 43.

| group | n | win | avg | CI | P&L $ |
|---|---|---|---|---|---|
| research-picked | 8 | 25% | -31.0% | -68 to 8 | -250 |
| momentum, not picked | 687 | 15% | -56.3% | -61 to -52 | -38732 |
| all momentum | 695 | 15% | -56.0% | -61 to -51 | -38982 |
| control | 824 | 7% | -19.1% | -22 to -16 | -15791 |
| dip buy | 7 | 14% | -27.3% | -65 to 10 | -191 |
| proven pools | 38 | 42% | -17.9% | -34 to -2 | -681 |

What-if exit rules on the SAME trades. Cells: avg return (trades, win rate).

| exit rule | momentum | control | dip | proven |
|---|---|---|---|---|
| base_sl30_tp100 | -57% (674, 15%) | -19% (824, 7%) | -27% (7, 14%) | -18% (38, 42%) |
| wide_sl50_tp100 | -56% (674, 17%) | -19% (824, 8%) | -32% (7, 14%) | -18% (38, 42%) |
| sl30_tp50 | -58% (674, 19%) | -19% (824, 8%) | -32% (7, 14%) | -20% (38, 42%) |
| sl50_tp50 | -57% (674, 21%) | -20% (824, 9%) | -36% (7, 14%) | -20% (38, 42%) |
| no_stop_tp100 | -56% (674, 18%) | -20% (824, 8%) | -27% (7, 14%) | -18% (38, 42%) |

Verdict: NOT ENOUGH DATA (need 30+ closed filter=1 trades and a CI above zero before believing anything).

Pools seen: 24625. Outcomes:

- missed_window: 16073
- low_liquidity: 4527
- proven_liquidity_gone: 1790
- no_momentum: 889
- research_failed: 698
- simulated failed buy: 281
- proven_low_volume: 243
- proven_price_collapsed_or_parabolic: 49
- proven: 38
- proven_no_uptrend: 22
- research_passed: 8
- dip: 7

Warning: 184 judged pools had an unreadable mint/freeze value. Check mint_raw / freeze_raw in candidates.csv; the parsing may need fixing.
