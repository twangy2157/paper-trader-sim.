# Paper trader summary

SIMULATION ONLY. No real trades.

Updated 2026-11-22T10:33:11Z. Bankroll cash (research-selected trades): 563.74568815387. Open positions: 21. Pools on watchlist: 43.

| group | n | win | avg | CI | P&L $ |
|---|---|---|---|---|---|
| research-picked | 20 | 35% | -21.7% | -51 to 10 | -436 |
| momentum, not picked | 3475 | 12% | -66.2% | -68 to -64 | -230231 |
| all momentum | 3495 | 12% | -65.9% | -68 to -64 | -230667 |
| control | 4217 | 6% | -19.3% | -20 to -18 | -81614 |
| dip buy | 47 | 28% | -12.8% | -30 to 4 | -606 |
| proven pools | 129 | 33% | -31.0% | -40 to -22 | -4017 |

What-if exit rules on the SAME trades. Cells: avg return (trades, win rate).

| exit rule | momentum | control | dip | proven |
|---|---|---|---|---|
| base_sl30_tp100 | -66% (3474, 12%) | -19% (4217, 6%) | -13% (47, 28%) | -31% (129, 33%) |
| wide_sl50_tp100 | -66% (3474, 13%) | -20% (4217, 7%) | -13% (47, 32%) | -32% (129, 33%) |
| sl30_tp50 | -68% (3474, 14%) | -19% (4217, 7%) | -17% (47, 34%) | -31% (129, 33%) |
| sl50_tp50 | -67% (3474, 15%) | -20% (4217, 8%) | -18% (47, 38%) | -32% (129, 33%) |
| no_stop_tp100 | -66% (3474, 14%) | -20% (4217, 7%) | -12% (47, 32%) | -33% (129, 33%) |

Verdict: NOT ENOUGH DATA (need 30+ closed filter=1 trades and a CI above zero before believing anything).

Pools seen: 114801. Outcomes:

- missed_window: 74336
- low_liquidity: 19474
- proven_liquidity_gone: 9900
- no_momentum: 4265
- research_failed: 3492
- proven_low_volume: 1458
- simulated failed buy: 1453
- proven_price_collapsed_or_parabolic: 163
- proven: 129
- proven_no_uptrend: 64
- dip: 47
- research_passed: 20

Warning: 900 judged pools had an unreadable mint/freeze value. Check mint_raw / freeze_raw in candidates.csv; the parsing may need fixing.
