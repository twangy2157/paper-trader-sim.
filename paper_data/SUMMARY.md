# Paper trader summary

SIMULATION ONLY. No real trades.

Updated 2026-11-18T06:30:42Z. Bankroll cash (research-selected trades): 549.3536238229275. Open positions: 21. Pools on watchlist: 39.

| group | n | win | avg | CI | P&L $ |
|---|---|---|---|---|---|
| research-picked | 17 | 29% | -26.4% | -58 to 8 | -451 |
| momentum, not picked | 3048 | 11% | -66.6% | -69 to -64 | -203225 |
| all momentum | 3065 | 11% | -66.4% | -68 to -64 | -203676 |
| control | 3780 | 6% | -19.1% | -20 to -18 | -72606 |
| dip buy | 40 | 25% | -14.5% | -31 to 3 | -583 |
| proven pools | 119 | 34% | -32.8% | -42 to -23 | -3917 |

What-if exit rules on the SAME trades. Cells: avg return (trades, win rate).

| exit rule | momentum | control | dip | proven |
|---|---|---|---|---|
| base_sl30_tp100 | -67% (3044, 11%) | -19% (3780, 6%) | -15% (40, 25%) | -33% (119, 34%) |
| wide_sl50_tp100 | -66% (3044, 13%) | -19% (3780, 6%) | -17% (40, 28%) | -34% (119, 34%) |
| sl30_tp50 | -68% (3044, 14%) | -19% (3780, 7%) | -19% (40, 28%) | -33% (119, 34%) |
| sl50_tp50 | -67% (3044, 15%) | -20% (3780, 7%) | -21% (40, 32%) | -34% (119, 34%) |
| no_stop_tp100 | -66% (3044, 13%) | -20% (3780, 6%) | -15% (40, 28%) | -35% (119, 34%) |

Verdict: NOT ENOUGH DATA (need 30+ closed filter=1 trades and a CI above zero before believing anything).

Pools seen: 101774. Outcomes:

- missed_window: 66195
- low_liquidity: 16904
- proven_liquidity_gone: 8777
- no_momentum: 3835
- research_failed: 3057
- proven_low_volume: 1338
- simulated failed buy: 1278
- proven_price_collapsed_or_parabolic: 153
- proven: 120
- proven_no_uptrend: 60
- dip: 40
- research_passed: 17

Warning: 806 judged pools had an unreadable mint/freeze value. Check mint_raw / freeze_raw in candidates.csv; the parsing may need fixing.
