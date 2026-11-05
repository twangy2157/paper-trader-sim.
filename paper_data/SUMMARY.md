# Paper trader summary

SIMULATION ONLY. No real trades.

Updated 2026-11-05T17:00:58Z. Bankroll cash (research-selected trades): 749.6403049524637. Open positions: 22. Pools on watchlist: 56.

| group | n | win | avg | CI | P&L $ |
|---|---|---|---|---|---|
| research-picked | 8 | 25% | -31.0% | -68 to 8 | -250 |
| momentum, not picked | 686 | 14% | -56.4% | -61 to -52 | -38775 |
| all momentum | 694 | 15% | -56.1% | -61 to -52 | -39025 |
| control | 821 | 7% | -18.8% | -21 to -16 | -15497 |
| dip buy | 7 | 14% | -27.3% | -65 to 10 | -191 |
| proven pools | 38 | 42% | -17.9% | -34 to -2 | -681 |

What-if exit rules on the SAME trades. Cells: avg return (trades, win rate).

| exit rule | momentum | control | dip | proven |
|---|---|---|---|---|
| base_sl30_tp100 | -57% (673, 15%) | -19% (821, 7%) | -27% (7, 14%) | -18% (38, 42%) |
| wide_sl50_tp100 | -56% (673, 17%) | -19% (821, 8%) | -32% (7, 14%) | -18% (38, 42%) |
| sl30_tp50 | -58% (673, 18%) | -19% (821, 8%) | -32% (7, 14%) | -20% (38, 42%) |
| sl50_tp50 | -57% (673, 21%) | -19% (821, 9%) | -36% (7, 14%) | -20% (38, 42%) |
| no_stop_tp100 | -56% (673, 18%) | -19% (821, 8%) | -27% (7, 14%) | -18% (38, 42%) |

Verdict: NOT ENOUGH DATA (need 30+ closed filter=1 trades and a CI above zero before believing anything).

Pools seen: 24536. Outcomes:

- missed_window: 16019
- low_liquidity: 4511
- proven_liquidity_gone: 1787
- no_momentum: 882
- research_failed: 691
- simulated failed buy: 280
- proven_low_volume: 243
- proven_price_collapsed_or_parabolic: 48
- proven: 38
- proven_no_uptrend: 22
- research_passed: 8
- dip: 7

Warning: 183 judged pools had an unreadable mint/freeze value. Check mint_raw / freeze_raw in candidates.csv; the parsing may need fixing.
