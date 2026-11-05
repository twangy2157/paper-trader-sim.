# Paper trader summary

SIMULATION ONLY. No real trades.

Updated 2026-11-05T18:40:21Z. Bankroll cash (research-selected trades): 749.6403049524637. Open positions: 20. Pools on watchlist: 36.

| group | n | win | avg | CI | P&L $ |
|---|---|---|---|---|---|
| research-picked | 8 | 25% | -31.0% | -68 to 8 | -250 |
| momentum, not picked | 700 | 14% | -56.5% | -61 to -52 | -39578 |
| all momentum | 708 | 15% | -56.2% | -61 to -51 | -39829 |
| control | 847 | 7% | -19.2% | -22 to -17 | -16321 |
| dip buy | 7 | 14% | -27.3% | -65 to 10 | -191 |
| proven pools | 38 | 42% | -17.9% | -34 to -2 | -681 |

What-if exit rules on the SAME trades. Cells: avg return (trades, win rate).

| exit rule | momentum | control | dip | proven |
|---|---|---|---|---|
| base_sl30_tp100 | -57% (687, 15%) | -19% (847, 7%) | -27% (7, 14%) | -18% (38, 42%) |
| wide_sl50_tp100 | -57% (687, 17%) | -20% (847, 7%) | -32% (7, 14%) | -18% (38, 42%) |
| sl30_tp50 | -58% (687, 18%) | -19% (847, 8%) | -32% (7, 14%) | -20% (38, 42%) |
| sl50_tp50 | -57% (687, 21%) | -20% (847, 9%) | -36% (7, 14%) | -20% (38, 42%) |
| no_stop_tp100 | -56% (687, 18%) | -20% (847, 8%) | -27% (7, 14%) | -18% (38, 42%) |

Verdict: NOT ENOUGH DATA (need 30+ closed filter=1 trades and a CI above zero before believing anything).

Pools seen: 24982. Outcomes:

- missed_window: 16321
- low_liquidity: 4573
- proven_liquidity_gone: 1823
- no_momentum: 900
- research_failed: 709
- simulated failed buy: 282
- proven_low_volume: 248
- proven_price_collapsed_or_parabolic: 49
- proven: 40
- proven_no_uptrend: 22
- research_passed: 8
- dip: 7

Warning: 185 judged pools had an unreadable mint/freeze value. Check mint_raw / freeze_raw in candidates.csv; the parsing may need fixing.
