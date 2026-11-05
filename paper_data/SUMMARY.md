# Paper trader summary

SIMULATION ONLY. No real trades.

Updated 2026-11-05T15:03:57Z. Bankroll cash (research-selected trades): 749.6403049524637. Open positions: 21. Pools on watchlist: 57.

| group | n | win | avg | CI | P&L $ |
|---|---|---|---|---|---|
| research-picked | 8 | 25% | -31.0% | -68 to 8 | -250 |
| momentum, not picked | 667 | 15% | -55.7% | -61 to -51 | -37242 |
| all momentum | 675 | 15% | -55.5% | -60 to -51 | -37493 |
| control | 804 | 7% | -18.7% | -21 to -16 | -15109 |
| dip buy | 7 | 14% | -27.3% | -65 to 10 | -191 |
| proven pools | 38 | 42% | -17.9% | -34 to -2 | -681 |

What-if exit rules on the SAME trades. Cells: avg return (trades, win rate).

| exit rule | momentum | control | dip | proven |
|---|---|---|---|---|
| base_sl30_tp100 | -56% (654, 15%) | -19% (804, 7%) | -27% (7, 14%) | -18% (38, 42%) |
| wide_sl50_tp100 | -56% (654, 17%) | -19% (804, 8%) | -32% (7, 14%) | -18% (38, 42%) |
| sl30_tp50 | -57% (654, 19%) | -19% (804, 8%) | -32% (7, 14%) | -20% (38, 42%) |
| sl50_tp50 | -57% (654, 21%) | -19% (804, 9%) | -36% (7, 14%) | -20% (38, 42%) |
| no_stop_tp100 | -55% (654, 18%) | -19% (804, 8%) | -27% (7, 14%) | -18% (38, 42%) |

Verdict: NOT ENOUGH DATA (need 30+ closed filter=1 trades and a CI above zero before believing anything).

Pools seen: 23984. Outcomes:

- missed_window: 15656
- low_liquidity: 4429
- proven_liquidity_gone: 1731
- no_momentum: 857
- research_failed: 679
- simulated failed buy: 270
- proven_low_volume: 239
- proven_price_collapsed_or_parabolic: 48
- proven: 38
- proven_no_uptrend: 22
- research_passed: 8
- dip: 7

Warning: 176 judged pools had an unreadable mint/freeze value. Check mint_raw / freeze_raw in candidates.csv; the parsing may need fixing.
