# Paper trader summary

SIMULATION ONLY. No real trades.

Updated 2026-11-05T17:31:41Z. Bankroll cash (research-selected trades): 749.6403049524637. Open positions: 26. Pools on watchlist: 39.

| group | n | win | avg | CI | P&L $ |
|---|---|---|---|---|---|
| research-picked | 8 | 25% | -31.0% | -68 to 8 | -250 |
| momentum, not picked | 687 | 15% | -56.3% | -61 to -52 | -38732 |
| all momentum | 695 | 15% | -56.0% | -61 to -51 | -38982 |
| control | 831 | 7% | -19.2% | -22 to -17 | -16055 |
| dip buy | 7 | 14% | -27.3% | -65 to 10 | -191 |
| proven pools | 38 | 42% | -17.9% | -34 to -2 | -681 |

What-if exit rules on the SAME trades. Cells: avg return (trades, win rate).

| exit rule | momentum | control | dip | proven |
|---|---|---|---|---|
| base_sl30_tp100 | -57% (674, 15%) | -19% (831, 7%) | -27% (7, 14%) | -18% (38, 42%) |
| wide_sl50_tp100 | -56% (674, 17%) | -20% (831, 7%) | -32% (7, 14%) | -18% (38, 42%) |
| sl30_tp50 | -58% (674, 19%) | -20% (831, 8%) | -32% (7, 14%) | -20% (38, 42%) |
| sl50_tp50 | -57% (674, 21%) | -20% (831, 9%) | -36% (7, 14%) | -20% (38, 42%) |
| no_stop_tp100 | -56% (674, 18%) | -20% (831, 8%) | -27% (7, 14%) | -18% (38, 42%) |

Verdict: NOT ENOUGH DATA (need 30+ closed filter=1 trades and a CI above zero before believing anything).

Pools seen: 24658. Outcomes:

- missed_window: 16097
- low_liquidity: 4530
- proven_liquidity_gone: 1794
- no_momentum: 889
- research_failed: 699
- simulated failed buy: 281
- proven_low_volume: 244
- proven_price_collapsed_or_parabolic: 49
- proven: 38
- proven_no_uptrend: 22
- research_passed: 8
- dip: 7

Warning: 184 judged pools had an unreadable mint/freeze value. Check mint_raw / freeze_raw in candidates.csv; the parsing may need fixing.
