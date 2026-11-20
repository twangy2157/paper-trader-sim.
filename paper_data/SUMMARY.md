# Paper trader summary

SIMULATION ONLY. No real trades.

Updated 2026-11-20T15:25:42Z. Bankroll cash (research-selected trades): 564.24568815387. Open positions: 13. Pools on watchlist: 21.

| group | n | win | avg | CI | P&L $ |
|---|---|---|---|---|---|
| research-picked | 20 | 35% | -21.7% | -51 to 10 | -436 |
| momentum, not picked | 3254 | 11% | -67.0% | -69 to -65 | -218265 |
| all momentum | 3274 | 11% | -66.7% | -69 to -65 | -218701 |
| control | 3976 | 6% | -19.2% | -20 to -18 | -76831 |
| dip buy | 43 | 26% | -13.5% | -30 to 3 | -583 |
| proven pools | 126 | 33% | -30.7% | -39 to -21 | -3879 |

What-if exit rules on the SAME trades. Cells: avg return (trades, win rate).

| exit rule | momentum | control | dip | proven |
|---|---|---|---|---|
| base_sl30_tp100 | -67% (3253, 11%) | -19% (3976, 6%) | -14% (43, 26%) | -31% (126, 33%) |
| wide_sl50_tp100 | -67% (3253, 13%) | -19% (3976, 7%) | -13% (43, 30%) | -32% (126, 33%) |
| sl30_tp50 | -68% (3253, 14%) | -19% (3976, 7%) | -16% (43, 33%) | -31% (126, 34%) |
| sl50_tp50 | -68% (3253, 15%) | -20% (3976, 8%) | -17% (43, 37%) | -32% (126, 34%) |
| no_stop_tp100 | -66% (3253, 13%) | -20% (3976, 7%) | -12% (43, 30%) | -32% (126, 33%) |

Verdict: NOT ENOUGH DATA (need 30+ closed filter=1 trades and a CI above zero before believing anything).

Pools seen: 107831. Outcomes:

- missed_window: 70002
- low_liquidity: 18081
- proven_liquidity_gone: 9320
- no_momentum: 4030
- research_failed: 3257
- proven_low_volume: 1382
- simulated failed buy: 1350
- proven_price_collapsed_or_parabolic: 158
- proven: 126
- proven_no_uptrend: 62
- dip: 43
- research_passed: 20

Warning: 849 judged pools had an unreadable mint/freeze value. Check mint_raw / freeze_raw in candidates.csv; the parsing may need fixing.
