# Paper trader summary

SIMULATION ONLY. No real trades.

Updated 2026-11-15T16:17:41Z. Bankroll cash (research-selected trades): 456.400154541351. Open positions: 35. Pools on watchlist: 63.

| group | n | win | avg | CI | P&L $ |
|---|---|---|---|---|---|
| research-picked | 16 | 25% | -33.9% | -64 to -3 | -544 |
| momentum, not picked | 2549 | 12% | -65.9% | -68 to -64 | -168142 |
| all momentum | 2565 | 12% | -65.7% | -68 to -63 | -168686 |
| control | 3255 | 6% | -18.8% | -20 to -18 | -61411 |
| dip buy | 34 | 29% | -11.9% | -32 to 8 | -406 |
| proven pools | 112 | 34% | -33.2% | -43 to -23 | -3725 |

What-if exit rules on the SAME trades. Cells: avg return (trades, win rate).

| exit rule | momentum | control | dip | proven |
|---|---|---|---|---|
| base_sl30_tp100 | -66% (2544, 12%) | -19% (3255, 6%) | -12% (34, 29%) | -33% (112, 34%) |
| wide_sl50_tp100 | -66% (2544, 13%) | -19% (3255, 6%) | -15% (34, 32%) | -34% (112, 34%) |
| sl30_tp50 | -67% (2544, 14%) | -19% (3255, 7%) | -18% (34, 32%) | -33% (112, 35%) |
| sl50_tp50 | -67% (2544, 16%) | -19% (3255, 7%) | -21% (34, 35%) | -34% (112, 35%) |
| no_stop_tp100 | -66% (2544, 14%) | -19% (3255, 6%) | -13% (34, 32%) | -35% (112, 34%) |

Verdict: NOT ENOUGH DATA (need 30+ closed filter=1 trades and a CI above zero before believing anything).

Pools seen: 88589. Outcomes:

- missed_window: 58158
- low_liquidity: 14529
- proven_liquidity_gone: 7401
- no_momentum: 3324
- research_failed: 2559
- proven_low_volume: 1169
- simulated failed buy: 1095
- proven_price_collapsed_or_parabolic: 137
- proven: 112
- proven_no_uptrend: 55
- dip: 34
- research_passed: 16

Warning: 695 judged pools had an unreadable mint/freeze value. Check mint_raw / freeze_raw in candidates.csv; the parsing may need fixing.
