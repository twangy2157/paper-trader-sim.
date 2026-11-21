# Paper trader summary

SIMULATION ONLY. No real trades.

Updated 2026-11-21T04:49:12Z. Bankroll cash (research-selected trades): 563.74568815387. Open positions: 12. Pools on watchlist: 51.

| group | n | win | avg | CI | P&L $ |
|---|---|---|---|---|---|
| research-picked | 20 | 35% | -21.7% | -51 to 10 | -436 |
| momentum, not picked | 3341 | 12% | -66.5% | -68 to -65 | -222479 |
| all momentum | 3361 | 12% | -66.2% | -68 to -64 | -222916 |
| control | 4076 | 6% | -19.2% | -20 to -18 | -78543 |
| dip buy | 45 | 27% | -13.2% | -30 to 5 | -596 |
| proven pools | 126 | 33% | -30.7% | -39 to -21 | -3879 |

What-if exit rules on the SAME trades. Cells: avg return (trades, win rate).

| exit rule | momentum | control | dip | proven |
|---|---|---|---|---|
| base_sl30_tp100 | -66% (3340, 12%) | -19% (4076, 6%) | -13% (45, 27%) | -31% (126, 33%) |
| wide_sl50_tp100 | -66% (3340, 13%) | -19% (4076, 6%) | -13% (45, 31%) | -32% (126, 33%) |
| sl30_tp50 | -68% (3340, 14%) | -19% (4076, 7%) | -16% (45, 33%) | -31% (126, 34%) |
| sl50_tp50 | -68% (3340, 15%) | -20% (4076, 8%) | -18% (45, 38%) | -32% (126, 34%) |
| no_stop_tp100 | -66% (3340, 14%) | -20% (4076, 7%) | -12% (45, 31%) | -32% (126, 33%) |

Verdict: NOT ENOUGH DATA (need 30+ closed filter=1 trades and a CI above zero before believing anything).

Pools seen: 110452. Outcomes:

- missed_window: 71576
- low_liquidity: 18636
- proven_liquidity_gone: 9562
- no_momentum: 4126
- research_failed: 3345
- proven_low_volume: 1410
- simulated failed buy: 1383
- proven_price_collapsed_or_parabolic: 159
- proven: 127
- proven_no_uptrend: 62
- dip: 46
- research_passed: 20

Warning: 875 judged pools had an unreadable mint/freeze value. Check mint_raw / freeze_raw in candidates.csv; the parsing may need fixing.
