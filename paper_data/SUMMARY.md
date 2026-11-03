# Paper trader summary

SIMULATION ONLY. No real trades.

Updated 2026-11-03T10:59:43Z. Bankroll cash (research-selected trades): 898.0. Open positions: 29. Pools on watchlist: 51.

| group | n | win | avg | CI | P&L $ |
|---|---|---|---|---|---|
| research-picked | 1 | 0% | -101.0% | - | -102 |
| momentum, not picked | 283 | 15% | -52.9% | -60 to -45 | -15004 |
| all momentum | 284 | 15% | -53.1% | -60 to -46 | -15106 |
| control | 319 | 8% | -16.5% | -21 to -13 | -5305 |
| dip buy | 1 | 100% | 57.9% | - | 58 |
| proven pools | 9 | 33% | -41.1% | -78 to -6 | -370 |

What-if exit rules on the SAME trades. Cells: avg return (trades, win rate).

| exit rule | momentum | control | dip | proven |
|---|---|---|---|---|
| base_sl30_tp100 | -54% (263, 16%) | -17% (319, 8%) | 58% (1, 100%) | -41% (9, 33%) |
| wide_sl50_tp100 | -55% (263, 17%) | -17% (319, 8%) | 58% (1, 100%) | -41% (9, 33%) |
| sl30_tp50 | -56% (263, 20%) | -18% (319, 8%) | 24% (1, 100%) | -41% (9, 33%) |
| sl50_tp50 | -55% (263, 22%) | -18% (319, 9%) | 24% (1, 100%) | -41% (9, 33%) |
| no_stop_tp100 | -55% (263, 18%) | -17% (319, 8%) | 58% (1, 100%) | -41% (9, 33%) |

Verdict: NOT ENOUGH DATA (need 30+ closed filter=1 trades and a CI above zero before believing anything).

Pools seen: 10629. Outcomes:

- missed_window: 7024
- low_liquidity: 2238
- proven_liquidity_gone: 469
- no_momentum: 378
- research_failed: 292
- simulated failed buy: 110
- proven_low_volume: 80
- proven: 13
- proven_price_collapsed_or_parabolic: 13
- proven_no_uptrend: 9
- dip: 2
- research_passed: 1

Warning: 71 judged pools had an unreadable mint/freeze value. Check mint_raw / freeze_raw in candidates.csv; the parsing may need fixing.
