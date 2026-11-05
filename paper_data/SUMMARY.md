# Paper trader summary

SIMULATION ONLY. No real trades.

Updated 2026-11-05T18:23:57Z. Bankroll cash (research-selected trades): 749.6403049524637. Open positions: 18. Pools on watchlist: 60.

| group | n | win | avg | CI | P&L $ |
|---|---|---|---|---|---|
| research-picked | 8 | 25% | -31.0% | -68 to 8 | -250 |
| momentum, not picked | 698 | 14% | -56.5% | -61 to -52 | -39474 |
| all momentum | 706 | 15% | -56.2% | -61 to -52 | -39725 |
| control | 844 | 7% | -19.2% | -22 to -17 | -16294 |
| dip buy | 7 | 14% | -27.3% | -65 to 10 | -191 |
| proven pools | 38 | 42% | -17.9% | -34 to -2 | -681 |

What-if exit rules on the SAME trades. Cells: avg return (trades, win rate).

| exit rule | momentum | control | dip | proven |
|---|---|---|---|---|
| base_sl30_tp100 | -57% (685, 15%) | -19% (844, 7%) | -27% (7, 14%) | -18% (38, 42%) |
| wide_sl50_tp100 | -57% (685, 17%) | -20% (844, 7%) | -32% (7, 14%) | -18% (38, 42%) |
| sl30_tp50 | -58% (685, 18%) | -20% (844, 8%) | -32% (7, 14%) | -20% (38, 42%) |
| sl50_tp50 | -57% (685, 21%) | -20% (844, 9%) | -36% (7, 14%) | -20% (38, 42%) |
| no_stop_tp100 | -56% (685, 18%) | -20% (844, 8%) | -27% (7, 14%) | -18% (38, 42%) |

Verdict: NOT ENOUGH DATA (need 30+ closed filter=1 trades and a CI above zero before believing anything).

Pools seen: 24903. Outcomes:

- missed_window: 16270
- low_liquidity: 4562
- proven_liquidity_gone: 1814
- no_momentum: 897
- research_failed: 705
- simulated failed buy: 282
- proven_low_volume: 247
- proven_price_collapsed_or_parabolic: 49
- proven: 40
- proven_no_uptrend: 22
- research_passed: 8
- dip: 7

Warning: 185 judged pools had an unreadable mint/freeze value. Check mint_raw / freeze_raw in candidates.csv; the parsing may need fixing.
