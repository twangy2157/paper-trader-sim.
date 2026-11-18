# Paper trader summary

SIMULATION ONLY. No real trades.

Updated 2026-11-18T21:07:39Z. Bankroll cash (research-selected trades): 549.3536238229275. Open positions: 5. Pools on watchlist: 57.

| group | n | win | avg | CI | P&L $ |
|---|---|---|---|---|---|
| research-picked | 17 | 29% | -26.4% | -58 to 8 | -451 |
| momentum, not picked | 3104 | 11% | -66.8% | -69 to -65 | -207590 |
| all momentum | 3121 | 11% | -66.6% | -69 to -64 | -208041 |
| control | 3836 | 6% | -19.1% | -20 to -18 | -73450 |
| dip buy | 41 | 27% | -12.0% | -29 to 6 | -494 |
| proven pools | 120 | 33% | -32.6% | -42 to -23 | -3923 |

What-if exit rules on the SAME trades. Cells: avg return (trades, win rate).

| exit rule | momentum | control | dip | proven |
|---|---|---|---|---|
| base_sl30_tp100 | -67% (3100, 11%) | -19% (3836, 6%) | -12% (41, 27%) | -33% (120, 33%) |
| wide_sl50_tp100 | -66% (3100, 13%) | -19% (3836, 6%) | -15% (41, 29%) | -34% (120, 33%) |
| sl30_tp50 | -68% (3100, 14%) | -19% (3836, 7%) | -18% (41, 29%) | -33% (120, 34%) |
| sl50_tp50 | -68% (3100, 15%) | -19% (3836, 7%) | -19% (41, 34%) | -34% (120, 34%) |
| no_stop_tp100 | -66% (3100, 13%) | -20% (3836, 7%) | -13% (41, 29%) | -35% (120, 33%) |

Verdict: NOT ENOUGH DATA (need 30+ closed filter=1 trades and a CI above zero before believing anything).

Pools seen: 103360. Outcomes:

- missed_window: 67215
- low_liquidity: 17226
- proven_liquidity_gone: 8896
- no_momentum: 3881
- research_failed: 3107
- proven_low_volume: 1346
- simulated failed buy: 1296
- proven_price_collapsed_or_parabolic: 153
- proven: 121
- proven_no_uptrend: 61
- dip: 41
- research_passed: 17

Warning: 821 judged pools had an unreadable mint/freeze value. Check mint_raw / freeze_raw in candidates.csv; the parsing may need fixing.
