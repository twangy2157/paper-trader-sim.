# Paper trader summary

SIMULATION ONLY. No real trades.

Updated 2026-11-06T01:17:40Z. Bankroll cash (research-selected trades): 749.6403049524637. Open positions: 13. Pools on watchlist: 98.

| group | n | win | avg | CI | P&L $ |
|---|---|---|---|---|---|
| research-picked | 8 | 25% | -31.0% | -68 to 8 | -250 |
| momentum, not picked | 751 | 14% | -58.0% | -62 to -53 | -43625 |
| all momentum | 759 | 14% | -57.7% | -62 to -53 | -43875 |
| control | 904 | 7% | -19.1% | -22 to -17 | -17360 |
| dip buy | 7 | 14% | -27.3% | -65 to 10 | -191 |
| proven pools | 40 | 45% | -15.2% | -31 to 0 | -612 |

What-if exit rules on the SAME trades. Cells: avg return (trades, win rate).

| exit rule | momentum | control | dip | proven |
|---|---|---|---|---|
| base_sl30_tp100 | -58% (738, 14%) | -19% (904, 7%) | -27% (7, 14%) | -15% (40, 45%) |
| wide_sl50_tp100 | -58% (738, 16%) | -20% (904, 7%) | -32% (7, 14%) | -15% (40, 45%) |
| sl30_tp50 | -59% (738, 18%) | -20% (904, 8%) | -32% (7, 14%) | -18% (40, 45%) |
| sl50_tp50 | -59% (738, 20%) | -20% (904, 9%) | -36% (7, 14%) | -18% (40, 45%) |
| no_stop_tp100 | -58% (738, 17%) | -20% (904, 8%) | -27% (7, 14%) | -15% (40, 45%) |

Verdict: NOT ENOUGH DATA (need 30+ closed filter=1 trades and a CI above zero before believing anything).

Pools seen: 26744. Outcomes:

- missed_window: 17457
- low_liquidity: 4880
- proven_liquidity_gone: 1989
- no_momentum: 957
- research_failed: 754
- simulated failed buy: 313
- proven_low_volume: 265
- proven_price_collapsed_or_parabolic: 51
- proven: 40
- proven_no_uptrend: 22
- research_passed: 8
- dip: 8

Warning: 202 judged pools had an unreadable mint/freeze value. Check mint_raw / freeze_raw in candidates.csv; the parsing may need fixing.
