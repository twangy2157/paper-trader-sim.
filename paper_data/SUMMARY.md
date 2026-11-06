# Paper trader summary

SIMULATION ONLY. No real trades.

Updated 2026-11-06T02:21:30Z. Bankroll cash (research-selected trades): 649.6403049524637. Open positions: 30. Pools on watchlist: 71.

| group | n | win | avg | CI | P&L $ |
|---|---|---|---|---|---|
| research-picked | 8 | 25% | -31.0% | -68 to 8 | -250 |
| momentum, not picked | 754 | 14% | -58.1% | -62 to -54 | -43859 |
| all momentum | 762 | 14% | -57.8% | -62 to -54 | -44109 |
| control | 913 | 7% | -19.1% | -22 to -17 | -17509 |
| dip buy | 8 | 12% | -36.3% | -72 to 3 | -290 |
| proven pools | 40 | 45% | -15.2% | -31 to 0 | -612 |

What-if exit rules on the SAME trades. Cells: avg return (trades, win rate).

| exit rule | momentum | control | dip | proven |
|---|---|---|---|---|
| base_sl30_tp100 | -58% (741, 14%) | -19% (913, 7%) | -36% (8, 12%) | -15% (40, 45%) |
| wide_sl50_tp100 | -58% (741, 16%) | -20% (913, 7%) | -40% (8, 12%) | -15% (40, 45%) |
| sl30_tp50 | -60% (741, 18%) | -20% (913, 8%) | -40% (8, 12%) | -18% (40, 45%) |
| sl50_tp50 | -59% (741, 20%) | -20% (913, 8%) | -44% (8, 12%) | -18% (40, 45%) |
| no_stop_tp100 | -58% (741, 17%) | -20% (913, 7%) | -36% (8, 12%) | -15% (40, 45%) |

Verdict: NOT ENOUGH DATA (need 30+ closed filter=1 trades and a CI above zero before believing anything).

Pools seen: 27124. Outcomes:

- missed_window: 17665
- low_liquidity: 4974
- proven_liquidity_gone: 2025
- no_momentum: 968
- research_failed: 772
- simulated failed buy: 320
- proven_low_volume: 269
- proven_price_collapsed_or_parabolic: 52
- proven: 40
- proven_no_uptrend: 22
- research_passed: 9
- dip: 8

Warning: 208 judged pools had an unreadable mint/freeze value. Check mint_raw / freeze_raw in candidates.csv; the parsing may need fixing.
