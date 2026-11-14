# Paper trader summary

SIMULATION ONLY. No real trades.

Updated 2026-11-14T03:12:54Z. Bankroll cash (research-selected trades): 456.400154541351. Open positions: 8. Pools on watchlist: 56.

| group | n | win | avg | CI | P&L $ |
|---|---|---|---|---|---|
| research-picked | 16 | 25% | -33.9% | -64 to -3 | -544 |
| momentum, not picked | 2235 | 12% | -64.6% | -67 to -62 | -144630 |
| all momentum | 2251 | 12% | -64.4% | -67 to -62 | -145173 |
| control | 2981 | 6% | -18.3% | -20 to -17 | -54867 |
| dip buy | 32 | 28% | -15.4% | -37 to 5 | -493 |
| proven pools | 107 | 35% | -33.0% | -43 to -23 | -3544 |

What-if exit rules on the SAME trades. Cells: avg return (trades, win rate).

| exit rule | momentum | control | dip | proven |
|---|---|---|---|---|
| base_sl30_tp100 | -65% (2230, 12%) | -18% (2981, 6%) | -15% (32, 28%) | -33% (107, 35%) |
| wide_sl50_tp100 | -65% (2230, 14%) | -19% (2981, 6%) | -18% (32, 31%) | -34% (107, 35%) |
| sl30_tp50 | -66% (2230, 15%) | -19% (2981, 7%) | -20% (32, 31%) | -33% (107, 36%) |
| sl50_tp50 | -66% (2230, 16%) | -19% (2981, 7%) | -23% (32, 34%) | -34% (107, 36%) |
| no_stop_tp100 | -65% (2230, 14%) | -19% (2981, 6%) | -16% (32, 31%) | -35% (107, 35%) |

Verdict: NOT ENOUGH DATA (need 30+ closed filter=1 trades and a CI above zero before believing anything).

Pools seen: 78439. Outcomes:

- missed_window: 51512
- low_liquidity: 12844
- proven_liquidity_gone: 6417
- no_momentum: 3028
- research_failed: 2240
- proven_low_volume: 1097
- simulated failed buy: 972
- proven_price_collapsed_or_parabolic: 127
- proven: 107
- proven_no_uptrend: 47
- dip: 32
- research_passed: 16

Warning: 630 judged pools had an unreadable mint/freeze value. Check mint_raw / freeze_raw in candidates.csv; the parsing may need fixing.
