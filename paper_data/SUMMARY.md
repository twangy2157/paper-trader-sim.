# Paper trader summary

SIMULATION ONLY. No real trades.

Updated 2026-11-21T03:56:31Z. Bankroll cash (research-selected trades): 563.74568815387. Open positions: 29. Pools on watchlist: 41.

| group | n | win | avg | CI | P&L $ |
|---|---|---|---|---|---|
| research-picked | 20 | 35% | -21.7% | -51 to 10 | -436 |
| momentum, not picked | 3330 | 12% | -66.6% | -68 to -65 | -221989 |
| all momentum | 3350 | 12% | -66.3% | -68 to -64 | -222425 |
| control | 4066 | 6% | -19.2% | -20 to -18 | -78363 |
| dip buy | 45 | 27% | -13.2% | -30 to 5 | -596 |
| proven pools | 126 | 33% | -30.7% | -39 to -21 | -3879 |

What-if exit rules on the SAME trades. Cells: avg return (trades, win rate).

| exit rule | momentum | control | dip | proven |
|---|---|---|---|---|
| base_sl30_tp100 | -66% (3329, 12%) | -19% (4066, 6%) | -13% (45, 27%) | -31% (126, 33%) |
| wide_sl50_tp100 | -66% (3329, 13%) | -19% (4066, 6%) | -13% (45, 31%) | -32% (126, 33%) |
| sl30_tp50 | -68% (3329, 14%) | -19% (4066, 7%) | -16% (45, 33%) | -31% (126, 34%) |
| sl50_tp50 | -68% (3329, 15%) | -20% (4066, 8%) | -18% (45, 38%) | -32% (126, 34%) |
| no_stop_tp100 | -66% (3329, 14%) | -20% (4066, 7%) | -12% (45, 31%) | -32% (126, 33%) |

Verdict: NOT ENOUGH DATA (need 30+ closed filter=1 trades and a CI above zero before believing anything).

Pools seen: 110192. Outcomes:

- missed_window: 71398
- low_liquidity: 18593
- proven_liquidity_gone: 9532
- no_momentum: 4124
- research_failed: 3344
- proven_low_volume: 1408
- simulated failed buy: 1380
- proven_price_collapsed_or_parabolic: 159
- proven: 127
- proven_no_uptrend: 62
- dip: 45
- research_passed: 20

Warning: 874 judged pools had an unreadable mint/freeze value. Check mint_raw / freeze_raw in candidates.csv; the parsing may need fixing.
