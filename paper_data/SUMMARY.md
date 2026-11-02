# Paper trader summary

SIMULATION ONLY. No real trades.

Updated 2026-11-02T23:07:09Z. Bankroll cash (research-selected trades): 898.5. Open positions: 16. Pools on watchlist: 41.

| group | n | win | avg | CI | P&L $ |
|---|---|---|---|---|---|
| research-picked | 1 | 0% | -101.0% | - | -102 |
| momentum, not picked | 196 | 15% | -52.0% | -60 to -43 | -10217 |
| all momentum | 197 | 15% | -52.3% | -61 to -43 | -10318 |
| control | 203 | 9% | -16.0% | -21 to -11 | -3268 |
| dip buy | 0 | - | - | - | 0 |
| proven pools | 1 | 0% | -100.0% | - | -100 |

What-if exit rules on the SAME trades. Cells: avg return (trades, win rate).

| exit rule | momentum | control | dip | proven |
|---|---|---|---|---|
| base_sl30_tp100 | -54% (176, 16%) | -16% (203, 9%) | - | -100% (1, 0%) |
| wide_sl50_tp100 | -55% (176, 17%) | -17% (203, 9%) | - | -100% (1, 0%) |
| sl30_tp50 | -56% (176, 19%) | -18% (203, 10%) | - | -100% (1, 0%) |
| sl50_tp50 | -55% (176, 22%) | -18% (203, 10%) | - | -100% (1, 0%) |
| no_stop_tp100 | -54% (176, 18%) | -17% (203, 9%) | - | -100% (1, 0%) |

Verdict: NOT ENOUGH DATA (need 30+ closed filter=1 trades and a CI above zero before believing anything).

Pools seen: 7601. Outcomes:

- missed_window: 5059
- low_liquidity: 1772
- no_momentum: 256
- research_failed: 201
- proven_liquidity_gone: 198
- simulated failed buy: 70
- proven_low_volume: 32
- proven_no_uptrend: 5
- proven_price_collapsed_or_parabolic: 4
- proven: 3
- research_passed: 1

Warning: 48 judged pools had an unreadable mint/freeze value. Check mint_raw / freeze_raw in candidates.csv; the parsing may need fixing.
