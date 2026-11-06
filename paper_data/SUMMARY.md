# Paper trader summary

SIMULATION ONLY. No real trades.

Updated 2026-11-06T21:29:33Z. Bankroll cash (research-selected trades): 706.1731051473196. Open positions: 28. Pools on watchlist: 76.

| group | n | win | avg | CI | P&L $ |
|---|---|---|---|---|---|
| research-picked | 11 | 27% | -26.5% | -63 to 13 | -294 |
| momentum, not picked | 874 | 13% | -60.3% | -64 to -56 | -52744 |
| all momentum | 885 | 13% | -59.8% | -64 to -56 | -53038 |
| control | 1082 | 6% | -19.7% | -22 to -17 | -21374 |
| dip buy | 9 | 11% | -43.3% | -77 to -6 | -391 |
| proven pools | 45 | 47% | -15.0% | -30 to -1 | -678 |

What-if exit rules on the SAME trades. Cells: avg return (trades, win rate).

| exit rule | momentum | control | dip | proven |
|---|---|---|---|---|
| base_sl30_tp100 | -60% (864, 14%) | -20% (1082, 6%) | -43% (9, 11%) | -15% (45, 47%) |
| wide_sl50_tp100 | -60% (864, 15%) | -20% (1082, 7%) | -47% (9, 11%) | -15% (45, 47%) |
| sl30_tp50 | -62% (864, 16%) | -20% (1082, 7%) | -47% (9, 11%) | -17% (45, 47%) |
| sl50_tp50 | -61% (864, 19%) | -20% (1082, 8%) | -50% (9, 11%) | -17% (45, 47%) |
| no_stop_tp100 | -60% (864, 16%) | -21% (1082, 7%) | -43% (9, 11%) | -15% (45, 47%) |

Verdict: NOT ENOUGH DATA (need 30+ closed filter=1 trades and a CI above zero before believing anything).

Pools seen: 30950. Outcomes:

- missed_window: 20098
- low_liquidity: 5636
- proven_liquidity_gone: 2365
- no_momentum: 1145
- research_failed: 882
- simulated failed buy: 376
- proven_low_volume: 305
- proven_price_collapsed_or_parabolic: 55
- proven: 46
- proven_no_uptrend: 22
- research_passed: 11
- dip: 9

Warning: 239 judged pools had an unreadable mint/freeze value. Check mint_raw / freeze_raw in candidates.csv; the parsing may need fixing.
