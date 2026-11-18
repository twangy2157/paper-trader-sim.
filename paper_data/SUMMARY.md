# Paper trader summary

SIMULATION ONLY. No real trades.

Updated 2026-11-18T17:25:27Z. Bankroll cash (research-selected trades): 549.3536238229275. Open positions: 32. Pools on watchlist: 35.

| group | n | win | avg | CI | P&L $ |
|---|---|---|---|---|---|
| research-picked | 17 | 29% | -26.4% | -58 to 8 | -451 |
| momentum, not picked | 3067 | 11% | -66.6% | -69 to -65 | -204639 |
| all momentum | 3084 | 11% | -66.4% | -68 to -64 | -205090 |
| control | 3805 | 6% | -19.1% | -20 to -18 | -72914 |
| dip buy | 40 | 25% | -14.5% | -31 to 3 | -583 |
| proven pools | 120 | 33% | -32.6% | -42 to -23 | -3923 |

What-if exit rules on the SAME trades. Cells: avg return (trades, win rate).

| exit rule | momentum | control | dip | proven |
|---|---|---|---|---|
| base_sl30_tp100 | -67% (3063, 11%) | -19% (3805, 6%) | -15% (40, 25%) | -33% (120, 33%) |
| wide_sl50_tp100 | -66% (3063, 13%) | -19% (3805, 6%) | -17% (40, 28%) | -34% (120, 33%) |
| sl30_tp50 | -68% (3063, 14%) | -19% (3805, 7%) | -19% (40, 28%) | -33% (120, 34%) |
| sl50_tp50 | -67% (3063, 15%) | -19% (3805, 7%) | -21% (40, 32%) | -34% (120, 34%) |
| no_stop_tp100 | -66% (3063, 13%) | -20% (3805, 7%) | -15% (40, 28%) | -35% (120, 33%) |

Verdict: NOT ENOUGH DATA (need 30+ closed filter=1 trades and a CI above zero before believing anything).

Pools seen: 102274. Outcomes:

- missed_window: 66500
- low_liquidity: 17026
- proven_liquidity_gone: 8785
- no_momentum: 3863
- research_failed: 3084
- proven_low_volume: 1339
- simulated failed buy: 1286
- proven_price_collapsed_or_parabolic: 153
- proven: 120
- proven_no_uptrend: 60
- dip: 41
- research_passed: 17

Warning: 815 judged pools had an unreadable mint/freeze value. Check mint_raw / freeze_raw in candidates.csv; the parsing may need fixing.
