# Paper trader summary

SIMULATION ONLY. No real trades.

Updated 2026-11-05T22:12:09Z. Bankroll cash (research-selected trades): 749.6403049524637. Open positions: 18. Pools on watchlist: 78.

| group | n | win | avg | CI | P&L $ |
|---|---|---|---|---|---|
| research-picked | 8 | 25% | -31.0% | -68 to 8 | -250 |
| momentum, not picked | 731 | 14% | -57.7% | -62 to -53 | -42265 |
| all momentum | 739 | 14% | -57.4% | -62 to -53 | -42515 |
| control | 873 | 7% | -19.2% | -22 to -17 | -16847 |
| dip buy | 7 | 14% | -27.3% | -65 to 10 | -191 |
| proven pools | 40 | 45% | -15.2% | -31 to 0 | -612 |

What-if exit rules on the SAME trades. Cells: avg return (trades, win rate).

| exit rule | momentum | control | dip | proven |
|---|---|---|---|---|
| base_sl30_tp100 | -58% (718, 14%) | -19% (873, 7%) | -27% (7, 14%) | -15% (40, 45%) |
| wide_sl50_tp100 | -58% (718, 16%) | -20% (873, 7%) | -32% (7, 14%) | -15% (40, 45%) |
| sl30_tp50 | -59% (718, 18%) | -20% (873, 8%) | -32% (7, 14%) | -18% (40, 45%) |
| sl50_tp50 | -59% (718, 20%) | -20% (873, 9%) | -36% (7, 14%) | -18% (40, 45%) |
| no_stop_tp100 | -57% (718, 17%) | -20% (873, 8%) | -27% (7, 14%) | -15% (40, 45%) |

Verdict: NOT ENOUGH DATA (need 30+ closed filter=1 trades and a CI above zero before believing anything).

Pools seen: 25960. Outcomes:

- missed_window: 16954
- low_liquidity: 4747
- proven_liquidity_gone: 1914
- no_momentum: 926
- research_failed: 740
- simulated failed buy: 293
- proven_low_volume: 259
- proven_price_collapsed_or_parabolic: 50
- proven: 40
- proven_no_uptrend: 22
- research_passed: 8
- dip: 7

Warning: 189 judged pools had an unreadable mint/freeze value. Check mint_raw / freeze_raw in candidates.csv; the parsing may need fixing.
