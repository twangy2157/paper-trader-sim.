# Paper trader summary

SIMULATION ONLY. No real trades.

Updated 2026-11-20T02:39:11Z. Bankroll cash (research-selected trades): 564.24568815387. Open positions: 17. Pools on watchlist: 22.

| group | n | win | avg | CI | P&L $ |
|---|---|---|---|---|---|
| research-picked | 20 | 35% | -21.7% | -51 to 10 | -436 |
| momentum, not picked | 3221 | 11% | -67.0% | -69 to -65 | -216067 |
| all momentum | 3241 | 11% | -66.7% | -69 to -65 | -216502 |
| control | 3945 | 6% | -19.1% | -20 to -18 | -75883 |
| dip buy | 42 | 26% | -13.0% | -30 to 5 | -548 |
| proven pools | 123 | 33% | -31.5% | -41 to -22 | -3883 |

What-if exit rules on the SAME trades. Cells: avg return (trades, win rate).

| exit rule | momentum | control | dip | proven |
|---|---|---|---|---|
| base_sl30_tp100 | -67% (3220, 11%) | -19% (3945, 6%) | -13% (42, 26%) | -31% (123, 33%) |
| wide_sl50_tp100 | -67% (3220, 13%) | -19% (3945, 7%) | -16% (42, 29%) | -32% (123, 33%) |
| sl30_tp50 | -68% (3220, 14%) | -19% (3945, 7%) | -17% (42, 31%) | -32% (123, 34%) |
| sl50_tp50 | -68% (3220, 15%) | -20% (3945, 8%) | -18% (42, 36%) | -33% (123, 34%) |
| no_stop_tp100 | -67% (3220, 13%) | -20% (3945, 7%) | -15% (42, 29%) | -33% (123, 33%) |

Verdict: NOT ENOUGH DATA (need 30+ closed filter=1 trades and a CI above zero before believing anything).

Pools seen: 106848. Outcomes:

- missed_window: 69394
- low_liquidity: 17898
- proven_liquidity_gone: 9215
- no_momentum: 3999
- research_failed: 3228
- proven_low_volume: 1375
- simulated failed buy: 1334
- proven_price_collapsed_or_parabolic: 158
- proven: 123
- proven_no_uptrend: 62
- dip: 42
- research_passed: 20

Warning: 841 judged pools had an unreadable mint/freeze value. Check mint_raw / freeze_raw in candidates.csv; the parsing may need fixing.
