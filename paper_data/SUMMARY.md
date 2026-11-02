# Paper trader summary

SIMULATION ONLY. No real trades.

Updated 2026-11-02T22:13:56Z. Bankroll cash (research-selected trades): 898.5. Open positions: 20. Pools on watchlist: 76.

| group | n | win | avg | CI | P&L $ |
|---|---|---|---|---|---|
| research-picked | 1 | 0% | -101.0% | - | -102 |
| momentum, not picked | 191 | 15% | -52.3% | -61 to -44 | -10007 |
| all momentum | 192 | 15% | -52.6% | -62 to -43 | -10109 |
| control | 192 | 10% | -16.0% | -22 to -10 | -3082 |
| dip buy | 0 | - | - | - | 0 |
| proven pools | 1 | 0% | -100.0% | - | -100 |

What-if exit rules on the SAME trades. Cells: avg return (trades, win rate).

| exit rule | momentum | control | dip | proven |
|---|---|---|---|---|
| base_sl30_tp100 | -54% (171, 16%) | -16% (192, 10%) | - | -100% (1, 0%) |
| wide_sl50_tp100 | -55% (171, 17%) | -17% (192, 10%) | - | -100% (1, 0%) |
| sl30_tp50 | -56% (171, 19%) | -18% (192, 10%) | - | -100% (1, 0%) |
| sl50_tp50 | -55% (171, 22%) | -18% (192, 11%) | - | -100% (1, 0%) |
| no_stop_tp100 | -55% (171, 18%) | -17% (192, 10%) | - | -100% (1, 0%) |

Verdict: NOT ENOUGH DATA (need 30+ closed filter=1 trades and a CI above zero before believing anything).

Pools seen: 7373. Outcomes:

- missed_window: 4887
- low_liquidity: 1747
- no_momentum: 248
- research_failed: 197
- proven_liquidity_gone: 186
- simulated failed buy: 70
- proven_low_volume: 26
- proven_no_uptrend: 4
- proven_price_collapsed_or_parabolic: 4
- proven: 3
- research_passed: 1

Warning: 48 judged pools had an unreadable mint/freeze value. Check mint_raw / freeze_raw in candidates.csv; the parsing may need fixing.
