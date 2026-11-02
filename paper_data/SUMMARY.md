# Paper trader summary

SIMULATION ONLY. No real trades.

Updated 2026-11-02T22:24:11Z. Bankroll cash (research-selected trades): 898.5. Open positions: 17. Pools on watchlist: 58.

| group | n | win | avg | CI | P&L $ |
|---|---|---|---|---|---|
| research-picked | 1 | 0% | -101.0% | - | -102 |
| momentum, not picked | 192 | 15% | -52.6% | -61 to -44 | -10107 |
| all momentum | 193 | 15% | -52.8% | -62 to -44 | -10209 |
| control | 196 | 10% | -15.9% | -22 to -10 | -3126 |
| dip buy | 0 | - | - | - | 0 |
| proven pools | 1 | 0% | -100.0% | - | -100 |

What-if exit rules on the SAME trades. Cells: avg return (trades, win rate).

| exit rule | momentum | control | dip | proven |
|---|---|---|---|---|
| base_sl30_tp100 | -55% (172, 16%) | -16% (196, 10%) | - | -100% (1, 0%) |
| wide_sl50_tp100 | -55% (172, 17%) | -16% (196, 10%) | - | -100% (1, 0%) |
| sl30_tp50 | -56% (172, 19%) | -18% (196, 10%) | - | -100% (1, 0%) |
| sl50_tp50 | -55% (172, 22%) | -17% (196, 11%) | - | -100% (1, 0%) |
| no_stop_tp100 | -55% (172, 17%) | -17% (196, 10%) | - | -100% (1, 0%) |

Verdict: NOT ENOUGH DATA (need 30+ closed filter=1 trades and a CI above zero before believing anything).

Pools seen: 7438. Outcomes:

- missed_window: 4937
- low_liquidity: 1754
- no_momentum: 248
- research_failed: 199
- proven_liquidity_gone: 190
- simulated failed buy: 70
- proven_low_volume: 28
- proven_no_uptrend: 4
- proven_price_collapsed_or_parabolic: 4
- proven: 3
- research_passed: 1

Warning: 48 judged pools had an unreadable mint/freeze value. Check mint_raw / freeze_raw in candidates.csv; the parsing may need fixing.
