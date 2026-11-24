# Paper trader summary

SIMULATION ONLY. No real trades.

Updated 2026-11-24T03:26:43Z. Bankroll cash (research-selected trades): 563.74568815387. Open positions: 20. Pools on watchlist: 51.

| group | n | win | avg | CI | P&L $ |
|---|---|---|---|---|---|
| research-picked | 20 | 35% | -21.7% | -51 to 10 | -436 |
| momentum, not picked | 3619 | 12% | -65.9% | -68 to -64 | -238774 |
| all momentum | 3639 | 12% | -65.6% | -68 to -64 | -239210 |
| control | 4383 | 6% | -19.3% | -20 to -18 | -84875 |
| dip buy | 47 | 28% | -12.8% | -30 to 4 | -606 |
| proven pools | 129 | 33% | -31.0% | -40 to -22 | -4017 |

What-if exit rules on the SAME trades. Cells: avg return (trades, win rate).

| exit rule | momentum | control | dip | proven |
|---|---|---|---|---|
| base_sl30_tp100 | -66% (3618, 12%) | -19% (4383, 6%) | -13% (47, 28%) | -31% (129, 33%) |
| wide_sl50_tp100 | -66% (3618, 13%) | -20% (4383, 6%) | -13% (47, 32%) | -32% (129, 33%) |
| sl30_tp50 | -67% (3618, 14%) | -19% (4383, 7%) | -17% (47, 34%) | -31% (129, 33%) |
| sl50_tp50 | -67% (3618, 15%) | -20% (4383, 8%) | -18% (47, 38%) | -32% (129, 33%) |
| no_stop_tp100 | -65% (3618, 14%) | -20% (4383, 7%) | -12% (47, 32%) | -33% (129, 33%) |

Verdict: NOT ENOUGH DATA (need 30+ closed filter=1 trades and a CI above zero before believing anything).

Pools seen: 118707. Outcomes:

- missed_window: 76765
- low_liquidity: 20253
- proven_liquidity_gone: 10198
- no_momentum: 4439
- research_failed: 3626
- proven_low_volume: 1502
- simulated failed buy: 1498
- proven_price_collapsed_or_parabolic: 165
- proven: 130
- proven_no_uptrend: 64
- dip: 47
- research_passed: 20

Warning: 932 judged pools had an unreadable mint/freeze value. Check mint_raw / freeze_raw in candidates.csv; the parsing may need fixing.
