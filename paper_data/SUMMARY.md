# Paper trader summary

SIMULATION ONLY. No real trades.

Updated 2026-11-06T00:30:42Z. Bankroll cash (research-selected trades): 749.6403049524637. Open positions: 21. Pools on watchlist: 59.

| group | n | win | avg | CI | P&L $ |
|---|---|---|---|---|---|
| research-picked | 8 | 25% | -31.0% | -68 to 8 | -250 |
| momentum, not picked | 746 | 14% | -58.0% | -62 to -54 | -43365 |
| all momentum | 754 | 14% | -57.8% | -62 to -53 | -43616 |
| control | 895 | 7% | -19.0% | -21 to -17 | -17072 |
| dip buy | 7 | 14% | -27.3% | -65 to 10 | -191 |
| proven pools | 40 | 45% | -15.2% | -31 to 0 | -612 |

What-if exit rules on the SAME trades. Cells: avg return (trades, win rate).

| exit rule | momentum | control | dip | proven |
|---|---|---|---|---|
| base_sl30_tp100 | -58% (733, 14%) | -19% (895, 7%) | -27% (7, 14%) | -15% (40, 45%) |
| wide_sl50_tp100 | -58% (733, 16%) | -19% (895, 7%) | -32% (7, 14%) | -15% (40, 45%) |
| sl30_tp50 | -59% (733, 18%) | -19% (895, 8%) | -32% (7, 14%) | -18% (40, 45%) |
| sl50_tp50 | -59% (733, 20%) | -20% (895, 9%) | -36% (7, 14%) | -18% (40, 45%) |
| no_stop_tp100 | -58% (733, 17%) | -20% (895, 8%) | -27% (7, 14%) | -15% (40, 45%) |

Verdict: NOT ENOUGH DATA (need 30+ closed filter=1 trades and a CI above zero before believing anything).

Pools seen: 26644. Outcomes:

- missed_window: 17390
- low_liquidity: 4871
- proven_liquidity_gone: 1977
- no_momentum: 954
- research_failed: 752
- simulated failed buy: 309
- proven_low_volume: 263
- proven_price_collapsed_or_parabolic: 51
- proven: 40
- proven_no_uptrend: 22
- research_passed: 8
- dip: 7

Warning: 200 judged pools had an unreadable mint/freeze value. Check mint_raw / freeze_raw in candidates.csv; the parsing may need fixing.
