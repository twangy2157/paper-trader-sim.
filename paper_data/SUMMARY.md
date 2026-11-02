# Paper trader summary

SIMULATION ONLY. No real trades.

Updated 2026-11-02T20:58:12Z. Bankroll cash (research-selected trades): 898.5. Open positions: 25. Pools on watchlist: 70.

| group | n | win | avg | CI | P&L $ |
|---|---|---|---|---|---|
| research-picked | 1 | 0% | -101.0% | - | -102 |
| momentum, not picked | 185 | 15% | -51.5% | -60 to -43 | -9547 |
| all momentum | 186 | 15% | -51.8% | -61 to -42 | -9649 |
| control | 171 | 11% | -16.4% | -23 to -11 | -2826 |
| dip buy | 0 | - | - | - | 0 |
| proven pools | 1 | 0% | -100.0% | - | -100 |

What-if exit rules on the SAME trades. Cells: avg return (trades, win rate).

| exit rule | momentum | control | dip | proven |
|---|---|---|---|---|
| base_sl30_tp100 | -54% (165, 16%) | -16% (171, 11%) | - | -100% (1, 0%) |
| wide_sl50_tp100 | -54% (165, 18%) | -17% (171, 11%) | - | -100% (1, 0%) |
| sl30_tp50 | -56% (165, 19%) | -18% (171, 12%) | - | -100% (1, 0%) |
| sl50_tp50 | -55% (165, 22%) | -18% (171, 12%) | - | -100% (1, 0%) |
| no_stop_tp100 | -54% (165, 18%) | -17% (171, 11%) | - | -100% (1, 0%) |

Verdict: NOT ENOUGH DATA (need 30+ closed filter=1 trades and a CI above zero before believing anything).

Pools seen: 6912. Outcomes:

- missed_window: 4545
- low_liquidity: 1697
- no_momentum: 234
- research_failed: 189
- proven_liquidity_gone: 153
- simulated failed buy: 66
- proven_low_volume: 19
- proven: 3
- proven_price_collapsed_or_parabolic: 3
- proven_no_uptrend: 2
- research_passed: 1

Warning: 43 judged pools had an unreadable mint/freeze value. Check mint_raw / freeze_raw in candidates.csv; the parsing may need fixing.
