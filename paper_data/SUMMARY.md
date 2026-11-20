# Paper trader summary

SIMULATION ONLY. No real trades.

Updated 2026-11-20T06:11:11Z. Bankroll cash (research-selected trades): 564.24568815387. Open positions: 14. Pools on watchlist: 53.

| group | n | win | avg | CI | P&L $ |
|---|---|---|---|---|---|
| research-picked | 20 | 35% | -21.7% | -51 to 10 | -436 |
| momentum, not picked | 3249 | 11% | -67.0% | -69 to -65 | -217865 |
| all momentum | 3269 | 11% | -66.7% | -69 to -65 | -218301 |
| control | 3974 | 6% | -19.2% | -20 to -18 | -76725 |
| dip buy | 43 | 26% | -13.5% | -30 to 3 | -583 |
| proven pools | 125 | 33% | -31.0% | -40 to -21 | -3889 |

What-if exit rules on the SAME trades. Cells: avg return (trades, win rate).

| exit rule | momentum | control | dip | proven |
|---|---|---|---|---|
| base_sl30_tp100 | -67% (3248, 12%) | -19% (3974, 6%) | -14% (43, 26%) | -31% (125, 33%) |
| wide_sl50_tp100 | -67% (3248, 13%) | -19% (3974, 7%) | -13% (43, 30%) | -32% (125, 33%) |
| sl30_tp50 | -68% (3248, 14%) | -19% (3974, 7%) | -16% (43, 33%) | -31% (125, 34%) |
| sl50_tp50 | -68% (3248, 15%) | -20% (3974, 8%) | -17% (43, 37%) | -32% (125, 34%) |
| no_stop_tp100 | -66% (3248, 13%) | -20% (3974, 7%) | -12% (43, 30%) | -33% (125, 33%) |

Verdict: NOT ENOUGH DATA (need 30+ closed filter=1 trades and a CI above zero before believing anything).

Pools seen: 107767. Outcomes:

- missed_window: 69949
- low_liquidity: 18078
- proven_liquidity_gone: 9320
- no_momentum: 4024
- research_failed: 3256
- proven_low_volume: 1382
- simulated failed buy: 1349
- proven_price_collapsed_or_parabolic: 158
- proven: 126
- proven_no_uptrend: 62
- dip: 43
- research_passed: 20

Warning: 849 judged pools had an unreadable mint/freeze value. Check mint_raw / freeze_raw in candidates.csv; the parsing may need fixing.
