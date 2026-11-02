# Paper trader summary

SIMULATION ONLY. No real trades.

Updated 2026-11-02T21:29:44Z. Bankroll cash (research-selected trades): 898.5. Open positions: 25. Pools on watchlist: 105.

| group | n | win | avg | CI | P&L $ |
|---|---|---|---|---|---|
| research-picked | 1 | 0% | -101.0% | - | -102 |
| momentum, not picked | 187 | 15% | -52.0% | -61 to -43 | -9748 |
| all momentum | 188 | 15% | -52.3% | -61 to -43 | -9849 |
| control | 181 | 10% | -16.5% | -23 to -10 | -3010 |
| dip buy | 0 | - | - | - | 0 |
| proven pools | 1 | 0% | -100.0% | - | -100 |

What-if exit rules on the SAME trades. Cells: avg return (trades, win rate).

| exit rule | momentum | control | dip | proven |
|---|---|---|---|---|
| base_sl30_tp100 | -54% (167, 16%) | -17% (181, 10%) | - | -100% (1, 0%) |
| wide_sl50_tp100 | -55% (167, 17%) | -17% (181, 10%) | - | -100% (1, 0%) |
| sl30_tp50 | -56% (167, 19%) | -18% (181, 11%) | - | -100% (1, 0%) |
| sl50_tp50 | -55% (167, 22%) | -18% (181, 12%) | - | -100% (1, 0%) |
| no_stop_tp100 | -54% (167, 18%) | -17% (181, 10%) | - | -100% (1, 0%) |

Verdict: NOT ENOUGH DATA (need 30+ closed filter=1 trades and a CI above zero before believing anything).

Pools seen: 7099. Outcomes:

- missed_window: 4686
- low_liquidity: 1712
- no_momentum: 242
- research_failed: 193
- proven_liquidity_gone: 167
- simulated failed buy: 68
- proven_low_volume: 21
- proven: 3
- proven_no_uptrend: 3
- proven_price_collapsed_or_parabolic: 3
- research_passed: 1

Warning: 45 judged pools had an unreadable mint/freeze value. Check mint_raw / freeze_raw in candidates.csv; the parsing may need fixing.
