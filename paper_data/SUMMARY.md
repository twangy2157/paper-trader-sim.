# Paper trader summary

SIMULATION ONLY. No real trades.

Updated 2026-11-03T11:32:38Z. Bankroll cash (research-selected trades): 898.0. Open positions: 30. Pools on watchlist: 51.

| group | n | win | avg | CI | P&L $ |
|---|---|---|---|---|---|
| research-picked | 1 | 0% | -101.0% | - | -102 |
| momentum, not picked | 285 | 15% | -53.3% | -61 to -46 | -15205 |
| all momentum | 286 | 15% | -53.4% | -60 to -46 | -15307 |
| control | 326 | 8% | -16.4% | -21 to -12 | -5372 |
| dip buy | 1 | 100% | 57.9% | - | 58 |
| proven pools | 11 | 36% | -41.8% | -73 to -11 | -461 |

What-if exit rules on the SAME trades. Cells: avg return (trades, win rate).

| exit rule | momentum | control | dip | proven |
|---|---|---|---|---|
| base_sl30_tp100 | -55% (265, 16%) | -16% (326, 8%) | 58% (1, 100%) | -42% (11, 36%) |
| wide_sl50_tp100 | -55% (265, 17%) | -17% (326, 8%) | 58% (1, 100%) | -42% (11, 36%) |
| sl30_tp50 | -56% (265, 20%) | -18% (326, 8%) | 24% (1, 100%) | -42% (11, 36%) |
| sl50_tp50 | -56% (265, 22%) | -17% (326, 9%) | 24% (1, 100%) | -42% (11, 36%) |
| no_stop_tp100 | -55% (265, 18%) | -17% (326, 8%) | 58% (1, 100%) | -42% (11, 36%) |

Verdict: NOT ENOUGH DATA (need 30+ closed filter=1 trades and a CI above zero before believing anything).

Pools seen: 10764. Outcomes:

- missed_window: 7108
- low_liquidity: 2258
- proven_liquidity_gone: 484
- no_momentum: 381
- research_failed: 300
- simulated failed buy: 111
- proven_low_volume: 83
- proven: 14
- proven_price_collapsed_or_parabolic: 13
- proven_no_uptrend: 9
- dip: 2
- research_passed: 1

Warning: 71 judged pools had an unreadable mint/freeze value. Check mint_raw / freeze_raw in candidates.csv; the parsing may need fixing.
