# Paper trader summary

SIMULATION ONLY. No real trades.

Updated 2026-11-12T15:51:56Z. Bankroll cash (research-selected trades): 456.400154541351. Open positions: 21. Pools on watchlist: 53.

| group | n | win | avg | CI | P&L $ |
|---|---|---|---|---|---|
| research-picked | 16 | 25% | -33.9% | -64 to -3 | -544 |
| momentum, not picked | 1949 | 12% | -64.6% | -67 to -62 | -126104 |
| all momentum | 1965 | 12% | -64.4% | -67 to -62 | -126648 |
| control | 2728 | 6% | -18.1% | -19 to -17 | -49504 |
| dip buy | 27 | 26% | -19.9% | -44 to 4 | -539 |
| proven pools | 92 | 35% | -29.8% | -41 to -19 | -2749 |

What-if exit rules on the SAME trades. Cells: avg return (trades, win rate).

| exit rule | momentum | control | dip | proven |
|---|---|---|---|---|
| base_sl30_tp100 | -65% (1944, 12%) | -18% (2728, 6%) | -20% (27, 26%) | -30% (92, 35%) |
| wide_sl50_tp100 | -65% (1944, 13%) | -18% (2728, 6%) | -23% (27, 30%) | -31% (92, 35%) |
| sl30_tp50 | -66% (1944, 15%) | -18% (2728, 6%) | -25% (27, 30%) | -31% (92, 35%) |
| sl50_tp50 | -66% (1944, 16%) | -19% (2728, 7%) | -28% (27, 33%) | -32% (92, 35%) |
| no_stop_tp100 | -65% (1944, 14%) | -19% (2728, 6%) | -21% (27, 30%) | -32% (92, 35%) |

Verdict: NOT ENOUGH DATA (need 30+ closed filter=1 trades and a CI above zero before believing anything).

Pools seen: 69316. Outcomes:

- missed_window: 45727
- low_liquidity: 11156
- proven_liquidity_gone: 5487
- no_momentum: 2779
- research_failed: 1962
- proven_low_volume: 1042
- simulated failed buy: 868
- proven_price_collapsed_or_parabolic: 119
- proven: 93
- proven_no_uptrend: 40
- dip: 27
- research_passed: 16

Warning: 573 judged pools had an unreadable mint/freeze value. Check mint_raw / freeze_raw in candidates.csv; the parsing may need fixing.
