# Paper trader summary

SIMULATION ONLY. No real trades.

Updated 2026-11-18T18:28:40Z. Bankroll cash (research-selected trades): 549.3536238229275. Open positions: 7. Pools on watchlist: 54.

| group | n | win | avg | CI | P&L $ |
|---|---|---|---|---|---|
| research-picked | 17 | 29% | -26.4% | -58 to 8 | -451 |
| momentum, not picked | 3084 | 11% | -66.6% | -69 to -65 | -205778 |
| all momentum | 3101 | 11% | -66.4% | -68 to -64 | -206228 |
| control | 3819 | 6% | -19.1% | -20 to -18 | -73128 |
| dip buy | 41 | 27% | -12.0% | -29 to 6 | -494 |
| proven pools | 120 | 33% | -32.6% | -42 to -23 | -3923 |

What-if exit rules on the SAME trades. Cells: avg return (trades, win rate).

| exit rule | momentum | control | dip | proven |
|---|---|---|---|---|
| base_sl30_tp100 | -67% (3080, 11%) | -19% (3819, 6%) | -12% (41, 27%) | -33% (120, 33%) |
| wide_sl50_tp100 | -66% (3080, 13%) | -19% (3819, 6%) | -15% (41, 29%) | -34% (120, 33%) |
| sl30_tp50 | -68% (3080, 14%) | -19% (3819, 7%) | -18% (41, 29%) | -33% (120, 34%) |
| sl50_tp50 | -67% (3080, 15%) | -19% (3819, 7%) | -19% (41, 34%) | -34% (120, 34%) |
| no_stop_tp100 | -66% (3080, 13%) | -20% (3819, 7%) | -13% (41, 29%) | -35% (120, 33%) |

Verdict: NOT ENOUGH DATA (need 30+ closed filter=1 trades and a CI above zero before believing anything).

Pools seen: 102630. Outcomes:

- missed_window: 66770
- low_liquidity: 17062
- proven_liquidity_gone: 8821
- no_momentum: 3866
- research_failed: 3088
- proven_low_volume: 1344
- simulated failed buy: 1288
- proven_price_collapsed_or_parabolic: 153
- proven: 120
- proven_no_uptrend: 60
- dip: 41
- research_passed: 17

Warning: 815 judged pools had an unreadable mint/freeze value. Check mint_raw / freeze_raw in candidates.csv; the parsing may need fixing.
