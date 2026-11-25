# Paper trader summary

SIMULATION ONLY. No real trades.

Updated 2026-11-25T01:11:54Z. Bankroll cash (research-selected trades): 452.209713614385. Open positions: 18. Pools on watchlist: 51.

| group | n | win | avg | CI | P&L $ |
|---|---|---|---|---|---|
| research-picked | 22 | 32% | -20.2% | -49 to 7 | -448 |
| momentum, not picked | 3709 | 12% | -65.7% | -68 to -64 | -243975 |
| all momentum | 3731 | 12% | -65.4% | -67 to -64 | -244422 |
| control | 4481 | 6% | -19.3% | -20 to -18 | -87103 |
| dip buy | 47 | 28% | -12.8% | -30 to 4 | -606 |
| proven pools | 133 | 33% | -30.1% | -38 to -21 | -4022 |

What-if exit rules on the SAME trades. Cells: avg return (trades, win rate).

| exit rule | momentum | control | dip | proven |
|---|---|---|---|---|
| base_sl30_tp100 | -66% (3710, 12%) | -19% (4481, 6%) | -13% (47, 28%) | -30% (133, 33%) |
| wide_sl50_tp100 | -65% (3710, 13%) | -20% (4481, 6%) | -13% (47, 32%) | -31% (133, 33%) |
| sl30_tp50 | -67% (3710, 14%) | -19% (4481, 7%) | -17% (47, 34%) | -30% (133, 34%) |
| sl50_tp50 | -67% (3710, 15%) | -20% (4481, 8%) | -18% (47, 38%) | -31% (133, 34%) |
| no_stop_tp100 | -65% (3710, 14%) | -20% (4481, 7%) | -12% (47, 32%) | -32% (133, 33%) |

Verdict: NOT ENOUGH DATA (need 30+ closed filter=1 trades and a CI above zero before believing anything).

Pools seen: 121209. Outcomes:

- missed_window: 78250
- low_liquidity: 20800
- proven_liquidity_gone: 10401
- no_momentum: 4538
- research_failed: 3713
- simulated failed buy: 1536
- proven_low_volume: 1536
- proven_price_collapsed_or_parabolic: 167
- proven: 133
- proven_no_uptrend: 65
- dip: 47
- research_passed: 23

Warning: 952 judged pools had an unreadable mint/freeze value. Check mint_raw / freeze_raw in candidates.csv; the parsing may need fixing.
