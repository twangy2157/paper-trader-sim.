# Paper trader summary

SIMULATION ONLY. No real trades.

Updated 2026-11-15T17:53:39Z. Bankroll cash (research-selected trades): 456.400154541351. Open positions: 12. Pools on watchlist: 56.

| group | n | win | avg | CI | P&L $ |
|---|---|---|---|---|---|
| research-picked | 16 | 25% | -33.9% | -64 to -3 | -544 |
| momentum, not picked | 2562 | 12% | -65.9% | -68 to -64 | -169102 |
| all momentum | 2578 | 12% | -65.7% | -68 to -63 | -169645 |
| control | 3288 | 6% | -18.7% | -20 to -17 | -61864 |
| dip buy | 34 | 29% | -11.9% | -32 to 8 | -406 |
| proven pools | 112 | 34% | -33.2% | -43 to -23 | -3725 |

What-if exit rules on the SAME trades. Cells: avg return (trades, win rate).

| exit rule | momentum | control | dip | proven |
|---|---|---|---|---|
| base_sl30_tp100 | -66% (2557, 12%) | -19% (3288, 6%) | -12% (34, 29%) | -33% (112, 34%) |
| wide_sl50_tp100 | -66% (2557, 13%) | -19% (3288, 6%) | -15% (34, 32%) | -34% (112, 34%) |
| sl30_tp50 | -67% (2557, 14%) | -19% (3288, 7%) | -18% (34, 32%) | -33% (112, 35%) |
| sl50_tp50 | -67% (2557, 16%) | -19% (3288, 7%) | -21% (34, 35%) | -34% (112, 35%) |
| no_stop_tp100 | -66% (2557, 14%) | -19% (3288, 6%) | -13% (34, 32%) | -35% (112, 34%) |

Verdict: NOT ENOUGH DATA (need 30+ closed filter=1 trades and a CI above zero before believing anything).

Pools seen: 89029. Outcomes:

- missed_window: 58463
- low_liquidity: 14590
- proven_liquidity_gone: 7432
- no_momentum: 3338
- research_failed: 2567
- proven_low_volume: 1182
- simulated failed buy: 1101
- proven_price_collapsed_or_parabolic: 137
- proven: 113
- proven_no_uptrend: 56
- dip: 34
- research_passed: 16

Warning: 700 judged pools had an unreadable mint/freeze value. Check mint_raw / freeze_raw in candidates.csv; the parsing may need fixing.
