# Paper trader summary

SIMULATION ONLY. No real trades.

Updated 2026-11-18T05:48:28Z. Bankroll cash (research-selected trades): 549.3536238229275. Open positions: 27. Pools on watchlist: 53.

| group | n | win | avg | CI | P&L $ |
|---|---|---|---|---|---|
| research-picked | 17 | 29% | -26.4% | -58 to 8 | -451 |
| momentum, not picked | 3039 | 11% | -66.5% | -69 to -65 | -202439 |
| all momentum | 3056 | 11% | -66.3% | -68 to -64 | -202889 |
| control | 3773 | 6% | -19.2% | -20 to -18 | -72657 |
| dip buy | 40 | 25% | -14.5% | -31 to 3 | -583 |
| proven pools | 117 | 32% | -33.8% | -43 to -24 | -3969 |

What-if exit rules on the SAME trades. Cells: avg return (trades, win rate).

| exit rule | momentum | control | dip | proven |
|---|---|---|---|---|
| base_sl30_tp100 | -67% (3035, 12%) | -19% (3773, 6%) | -15% (40, 25%) | -34% (117, 32%) |
| wide_sl50_tp100 | -66% (3035, 13%) | -19% (3773, 6%) | -17% (40, 28%) | -35% (117, 32%) |
| sl30_tp50 | -68% (3035, 14%) | -19% (3773, 7%) | -19% (40, 28%) | -34% (117, 33%) |
| sl50_tp50 | -67% (3035, 15%) | -20% (3773, 7%) | -21% (40, 32%) | -35% (117, 33%) |
| no_stop_tp100 | -66% (3035, 13%) | -20% (3773, 6%) | -15% (40, 28%) | -36% (117, 32%) |

Verdict: NOT ENOUGH DATA (need 30+ closed filter=1 trades and a CI above zero before believing anything).

Pools seen: 101598. Outcomes:

- missed_window: 66079
- low_liquidity: 16883
- proven_liquidity_gone: 8757
- no_momentum: 3828
- research_failed: 3052
- proven_low_volume: 1336
- simulated failed buy: 1273
- proven_price_collapsed_or_parabolic: 153
- proven: 120
- proven_no_uptrend: 60
- dip: 40
- research_passed: 17

Warning: 802 judged pools had an unreadable mint/freeze value. Check mint_raw / freeze_raw in candidates.csv; the parsing may need fixing.
