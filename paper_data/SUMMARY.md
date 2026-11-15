# Paper trader summary

SIMULATION ONLY. No real trades.

Updated 2026-11-15T12:02:54Z. Bankroll cash (research-selected trades): 456.400154541351. Open positions: 18. Pools on watchlist: 36.

| group | n | win | avg | CI | P&L $ |
|---|---|---|---|---|---|
| research-picked | 16 | 25% | -33.9% | -64 to -3 | -544 |
| momentum, not picked | 2516 | 12% | -65.8% | -68 to -64 | -165710 |
| all momentum | 2532 | 12% | -65.6% | -68 to -63 | -166254 |
| control | 3215 | 6% | -18.7% | -20 to -18 | -60448 |
| dip buy | 33 | 30% | -12.1% | -32 to 8 | -402 |
| proven pools | 111 | 33% | -33.7% | -43 to -24 | -3752 |

What-if exit rules on the SAME trades. Cells: avg return (trades, win rate).

| exit rule | momentum | control | dip | proven |
|---|---|---|---|---|
| base_sl30_tp100 | -66% (2511, 12%) | -19% (3215, 6%) | -12% (33, 30%) | -34% (111, 33%) |
| wide_sl50_tp100 | -66% (2511, 13%) | -19% (3215, 6%) | -15% (33, 33%) | -35% (111, 33%) |
| sl30_tp50 | -67% (2511, 14%) | -19% (3215, 7%) | -18% (33, 33%) | -34% (111, 34%) |
| sl50_tp50 | -67% (2511, 16%) | -19% (3215, 7%) | -21% (33, 36%) | -35% (111, 34%) |
| no_stop_tp100 | -66% (2511, 14%) | -19% (3215, 6%) | -13% (33, 33%) | -36% (111, 33%) |

Verdict: NOT ENOUGH DATA (need 30+ closed filter=1 trades and a CI above zero before believing anything).

Pools seen: 87454. Outcomes:

- missed_window: 57422
- low_liquidity: 14367
- proven_liquidity_gone: 7296
- no_momentum: 3269
- research_failed: 2523
- proven_low_volume: 1155
- simulated failed buy: 1074
- proven_price_collapsed_or_parabolic: 135
- proven: 112
- proven_no_uptrend: 52
- dip: 33
- research_passed: 16

Warning: 680 judged pools had an unreadable mint/freeze value. Check mint_raw / freeze_raw in candidates.csv; the parsing may need fixing.
