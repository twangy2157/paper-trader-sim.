# Paper trader summary

SIMULATION ONLY. No real trades.

Updated 2026-11-25T00:20:10Z. Bankroll cash (research-selected trades): 452.209713614385. Open positions: 21. Pools on watchlist: 67.

| group | n | win | avg | CI | P&L $ |
|---|---|---|---|---|---|
| research-picked | 22 | 32% | -20.2% | -49 to 7 | -448 |
| momentum, not picked | 3702 | 12% | -65.7% | -68 to -64 | -243664 |
| all momentum | 3724 | 12% | -65.5% | -67 to -64 | -244111 |
| control | 4471 | 6% | -19.3% | -20 to -18 | -86686 |
| dip buy | 47 | 28% | -12.8% | -30 to 4 | -606 |
| proven pools | 133 | 33% | -30.1% | -38 to -21 | -4022 |

What-if exit rules on the SAME trades. Cells: avg return (trades, win rate).

| exit rule | momentum | control | dip | proven |
|---|---|---|---|---|
| base_sl30_tp100 | -66% (3703, 12%) | -19% (4471, 6%) | -13% (47, 28%) | -30% (133, 33%) |
| wide_sl50_tp100 | -65% (3703, 13%) | -20% (4471, 7%) | -13% (47, 32%) | -31% (133, 33%) |
| sl30_tp50 | -67% (3703, 14%) | -19% (4471, 7%) | -17% (47, 34%) | -30% (133, 34%) |
| sl50_tp50 | -67% (3703, 15%) | -20% (4471, 8%) | -18% (47, 38%) | -31% (133, 34%) |
| no_stop_tp100 | -65% (3703, 14%) | -20% (4471, 7%) | -12% (47, 32%) | -32% (133, 33%) |

Verdict: NOT ENOUGH DATA (need 30+ closed filter=1 trades and a CI above zero before believing anything).

Pools seen: 121004. Outcomes:

- missed_window: 78127
- low_liquidity: 20766
- proven_liquidity_gone: 10375
- no_momentum: 4527
- research_failed: 3710
- simulated failed buy: 1535
- proven_low_volume: 1529
- proven_price_collapsed_or_parabolic: 167
- proven: 133
- proven_no_uptrend: 65
- dip: 47
- research_passed: 23

Warning: 952 judged pools had an unreadable mint/freeze value. Check mint_raw / freeze_raw in candidates.csv; the parsing may need fixing.
