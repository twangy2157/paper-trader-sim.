# Paper trader summary

SIMULATION ONLY. No real trades.

Updated 2026-11-05T17:52:12Z. Bankroll cash (research-selected trades): 749.6403049524637. Open positions: 26. Pools on watchlist: 75.

| group | n | win | avg | CI | P&L $ |
|---|---|---|---|---|---|
| research-picked | 8 | 25% | -31.0% | -68 to 8 | -250 |
| momentum, not picked | 690 | 15% | -56.3% | -61 to -51 | -38905 |
| all momentum | 698 | 15% | -56.0% | -60 to -51 | -39156 |
| control | 835 | 7% | -19.2% | -22 to -17 | -16082 |
| dip buy | 7 | 14% | -27.3% | -65 to 10 | -191 |
| proven pools | 38 | 42% | -17.9% | -34 to -2 | -681 |

What-if exit rules on the SAME trades. Cells: avg return (trades, win rate).

| exit rule | momentum | control | dip | proven |
|---|---|---|---|---|
| base_sl30_tp100 | -57% (677, 15%) | -19% (835, 7%) | -27% (7, 14%) | -18% (38, 42%) |
| wide_sl50_tp100 | -56% (677, 17%) | -20% (835, 7%) | -32% (7, 14%) | -18% (38, 42%) |
| sl30_tp50 | -58% (677, 19%) | -19% (835, 8%) | -32% (7, 14%) | -20% (38, 42%) |
| sl50_tp50 | -57% (677, 21%) | -20% (835, 9%) | -36% (7, 14%) | -20% (38, 42%) |
| no_stop_tp100 | -56% (677, 18%) | -20% (835, 8%) | -27% (7, 14%) | -18% (38, 42%) |

Verdict: NOT ENOUGH DATA (need 30+ closed filter=1 trades and a CI above zero before believing anything).

Pools seen: 24734. Outcomes:

- missed_window: 16139
- low_liquidity: 4546
- proven_liquidity_gone: 1803
- no_momentum: 892
- research_failed: 703
- simulated failed buy: 282
- proven_low_volume: 245
- proven_price_collapsed_or_parabolic: 49
- proven: 38
- proven_no_uptrend: 22
- research_passed: 8
- dip: 7

Warning: 185 judged pools had an unreadable mint/freeze value. Check mint_raw / freeze_raw in candidates.csv; the parsing may need fixing.
