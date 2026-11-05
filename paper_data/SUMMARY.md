# Paper trader summary

SIMULATION ONLY. No real trades.

Updated 2026-11-05T23:58:40Z. Bankroll cash (research-selected trades): 749.6403049524637. Open positions: 23. Pools on watchlist: 57.

| group | n | win | avg | CI | P&L $ |
|---|---|---|---|---|---|
| research-picked | 8 | 25% | -31.0% | -68 to 8 | -250 |
| momentum, not picked | 743 | 14% | -57.9% | -62 to -54 | -43064 |
| all momentum | 751 | 14% | -57.6% | -62 to -53 | -43315 |
| control | 888 | 7% | -19.0% | -21 to -17 | -16926 |
| dip buy | 7 | 14% | -27.3% | -65 to 10 | -191 |
| proven pools | 40 | 45% | -15.2% | -31 to 0 | -612 |

What-if exit rules on the SAME trades. Cells: avg return (trades, win rate).

| exit rule | momentum | control | dip | proven |
|---|---|---|---|---|
| base_sl30_tp100 | -58% (730, 15%) | -19% (888, 7%) | -27% (7, 14%) | -15% (40, 45%) |
| wide_sl50_tp100 | -58% (730, 16%) | -19% (888, 8%) | -32% (7, 14%) | -15% (40, 45%) |
| sl30_tp50 | -59% (730, 18%) | -19% (888, 8%) | -32% (7, 14%) | -18% (40, 45%) |
| sl50_tp50 | -59% (730, 20%) | -20% (888, 9%) | -36% (7, 14%) | -18% (40, 45%) |
| no_stop_tp100 | -57% (730, 17%) | -20% (888, 8%) | -27% (7, 14%) | -15% (40, 45%) |

Verdict: NOT ENOUGH DATA (need 30+ closed filter=1 trades and a CI above zero before believing anything).

Pools seen: 26516. Outcomes:

- missed_window: 17316
- low_liquidity: 4845
- proven_liquidity_gone: 1960
- no_momentum: 947
- research_failed: 751
- simulated failed buy: 307
- proven_low_volume: 263
- proven_price_collapsed_or_parabolic: 50
- proven: 40
- proven_no_uptrend: 22
- research_passed: 8
- dip: 7

Warning: 199 judged pools had an unreadable mint/freeze value. Check mint_raw / freeze_raw in candidates.csv; the parsing may need fixing.
