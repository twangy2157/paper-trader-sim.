# Paper trader summary

SIMULATION ONLY. No real trades.

Updated 2026-11-05T15:25:41Z. Bankroll cash (research-selected trades): 749.6403049524637. Open positions: 20. Pools on watchlist: 66.

| group | n | win | avg | CI | P&L $ |
|---|---|---|---|---|---|
| research-picked | 8 | 25% | -31.0% | -68 to 8 | -250 |
| momentum, not picked | 670 | 15% | -55.9% | -60 to -51 | -37544 |
| all momentum | 678 | 15% | -55.7% | -60 to -51 | -37794 |
| control | 807 | 7% | -18.7% | -21 to -16 | -15162 |
| dip buy | 7 | 14% | -27.3% | -65 to 10 | -191 |
| proven pools | 38 | 42% | -17.9% | -34 to -2 | -681 |

What-if exit rules on the SAME trades. Cells: avg return (trades, win rate).

| exit rule | momentum | control | dip | proven |
|---|---|---|---|---|
| base_sl30_tp100 | -56% (657, 15%) | -19% (807, 7%) | -27% (7, 14%) | -18% (38, 42%) |
| wide_sl50_tp100 | -56% (657, 17%) | -19% (807, 8%) | -32% (7, 14%) | -18% (38, 42%) |
| sl30_tp50 | -57% (657, 19%) | -19% (807, 8%) | -32% (7, 14%) | -20% (38, 42%) |
| sl50_tp50 | -57% (657, 21%) | -19% (807, 9%) | -36% (7, 14%) | -20% (38, 42%) |
| no_stop_tp100 | -55% (657, 18%) | -19% (807, 8%) | -27% (7, 14%) | -18% (38, 42%) |

Verdict: NOT ENOUGH DATA (need 30+ closed filter=1 trades and a CI above zero before believing anything).

Pools seen: 24090. Outcomes:

- missed_window: 15727
- low_liquidity: 4445
- proven_liquidity_gone: 1738
- no_momentum: 859
- research_failed: 682
- simulated failed buy: 277
- proven_low_volume: 239
- proven_price_collapsed_or_parabolic: 48
- proven: 38
- proven_no_uptrend: 22
- research_passed: 8
- dip: 7

Warning: 180 judged pools had an unreadable mint/freeze value. Check mint_raw / freeze_raw in candidates.csv; the parsing may need fixing.
