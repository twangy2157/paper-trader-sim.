# Paper trader summary

SIMULATION ONLY. No real trades.

Updated 2026-11-25T01:22:09Z. Bankroll cash (research-selected trades): 611.9691884226207. Open positions: 16. Pools on watchlist: 41.

| group | n | win | avg | CI | P&L $ |
|---|---|---|---|---|---|
| research-picked | 23 | 35% | -16.7% | -44 to 11 | -388 |
| momentum, not picked | 3710 | 12% | -65.7% | -68 to -64 | -244073 |
| all momentum | 3733 | 12% | -65.4% | -67 to -64 | -244461 |
| control | 4483 | 6% | -19.3% | -20 to -18 | -87122 |
| dip buy | 47 | 28% | -12.8% | -30 to 4 | -606 |
| proven pools | 133 | 33% | -30.1% | -38 to -21 | -4022 |

What-if exit rules on the SAME trades. Cells: avg return (trades, win rate).

| exit rule | momentum | control | dip | proven |
|---|---|---|---|---|
| base_sl30_tp100 | -66% (3712, 12%) | -19% (4483, 6%) | -13% (47, 28%) | -30% (133, 33%) |
| wide_sl50_tp100 | -65% (3712, 13%) | -20% (4483, 6%) | -13% (47, 32%) | -31% (133, 33%) |
| sl30_tp50 | -67% (3712, 14%) | -19% (4483, 7%) | -17% (47, 34%) | -30% (133, 34%) |
| sl50_tp50 | -67% (3712, 15%) | -20% (4483, 8%) | -18% (47, 38%) | -31% (133, 34%) |
| no_stop_tp100 | -65% (3712, 14%) | -20% (4483, 7%) | -12% (47, 32%) | -32% (133, 33%) |

Verdict: NOT ENOUGH DATA (need 30+ closed filter=1 trades and a CI above zero before believing anything).

Pools seen: 121256. Outcomes:

- missed_window: 78281
- low_liquidity: 20808
- proven_liquidity_gone: 10407
- no_momentum: 4539
- research_failed: 3714
- simulated failed buy: 1536
- proven_low_volume: 1536
- proven_price_collapsed_or_parabolic: 167
- proven: 133
- proven_no_uptrend: 65
- dip: 47
- research_passed: 23

Warning: 952 judged pools had an unreadable mint/freeze value. Check mint_raw / freeze_raw in candidates.csv; the parsing may need fixing.
