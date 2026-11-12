# Paper trader summary

SIMULATION ONLY. No real trades.

Updated 2026-11-12T19:01:43Z. Bankroll cash (research-selected trades): 456.400154541351. Open positions: 12. Pools on watchlist: 40.

| group | n | win | avg | CI | P&L $ |
|---|---|---|---|---|---|
| research-picked | 16 | 25% | -33.9% | -64 to -3 | -544 |
| momentum, not picked | 1980 | 12% | -64.9% | -67 to -62 | -128695 |
| all momentum | 1996 | 12% | -64.7% | -67 to -62 | -129239 |
| control | 2752 | 6% | -17.9% | -19 to -17 | -49467 |
| dip buy | 27 | 26% | -19.9% | -44 to 4 | -539 |
| proven pools | 94 | 35% | -29.8% | -41 to -20 | -2808 |

What-if exit rules on the SAME trades. Cells: avg return (trades, win rate).

| exit rule | momentum | control | dip | proven |
|---|---|---|---|---|
| base_sl30_tp100 | -65% (1975, 12%) | -18% (2752, 6%) | -20% (27, 26%) | -30% (94, 35%) |
| wide_sl50_tp100 | -65% (1975, 13%) | -18% (2752, 6%) | -23% (27, 30%) | -31% (94, 35%) |
| sl30_tp50 | -66% (1975, 15%) | -18% (2752, 6%) | -25% (27, 30%) | -31% (94, 35%) |
| sl50_tp50 | -66% (1975, 16%) | -18% (2752, 7%) | -28% (27, 33%) | -32% (94, 35%) |
| no_stop_tp100 | -65% (1975, 14%) | -18% (2752, 6%) | -21% (27, 30%) | -32% (94, 35%) |

Verdict: NOT ENOUGH DATA (need 30+ closed filter=1 trades and a CI above zero before believing anything).

Pools seen: 70101. Outcomes:

- missed_window: 46218
- low_liquidity: 11301
- proven_liquidity_gone: 5570
- no_momentum: 2801
- research_failed: 1984
- proven_low_volume: 1047
- simulated failed buy: 878
- proven_price_collapsed_or_parabolic: 120
- proven: 97
- proven_no_uptrend: 42
- dip: 27
- research_passed: 16

Warning: 579 judged pools had an unreadable mint/freeze value. Check mint_raw / freeze_raw in candidates.csv; the parsing may need fixing.
