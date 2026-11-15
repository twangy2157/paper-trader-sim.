# Paper trader summary

SIMULATION ONLY. No real trades.

Updated 2026-11-15T20:17:41Z. Bankroll cash (research-selected trades): 456.400154541351. Open positions: 14. Pools on watchlist: 66.

| group | n | win | avg | CI | P&L $ |
|---|---|---|---|---|---|
| research-picked | 16 | 25% | -33.9% | -64 to -3 | -544 |
| momentum, not picked | 2578 | 12% | -65.9% | -68 to -64 | -170167 |
| all momentum | 2594 | 12% | -65.7% | -68 to -64 | -170710 |
| control | 3306 | 6% | -18.6% | -20 to -17 | -61911 |
| dip buy | 34 | 29% | -11.9% | -32 to 8 | -406 |
| proven pools | 112 | 34% | -33.2% | -43 to -23 | -3725 |

What-if exit rules on the SAME trades. Cells: avg return (trades, win rate).

| exit rule | momentum | control | dip | proven |
|---|---|---|---|---|
| base_sl30_tp100 | -66% (2573, 12%) | -19% (3306, 6%) | -12% (34, 29%) | -33% (112, 34%) |
| wide_sl50_tp100 | -66% (2573, 13%) | -19% (3306, 6%) | -15% (34, 32%) | -34% (112, 34%) |
| sl30_tp50 | -67% (2573, 14%) | -19% (3306, 7%) | -18% (34, 32%) | -33% (112, 35%) |
| sl50_tp50 | -67% (2573, 16%) | -19% (3306, 7%) | -21% (34, 35%) | -34% (112, 35%) |
| no_stop_tp100 | -66% (2573, 14%) | -19% (3306, 6%) | -13% (34, 32%) | -35% (112, 34%) |

Verdict: NOT ENOUGH DATA (need 30+ closed filter=1 trades and a CI above zero before believing anything).

Pools seen: 89600. Outcomes:

- missed_window: 58814
- low_liquidity: 14694
- proven_liquidity_gone: 7487
- no_momentum: 3357
- research_failed: 2584
- proven_low_volume: 1197
- simulated failed buy: 1109
- proven_price_collapsed_or_parabolic: 138
- proven: 113
- proven_no_uptrend: 57
- dip: 34
- research_passed: 16

Warning: 707 judged pools had an unreadable mint/freeze value. Check mint_raw / freeze_raw in candidates.csv; the parsing may need fixing.
