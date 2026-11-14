# Paper trader summary

SIMULATION ONLY. No real trades.

Updated 2026-11-14T10:46:31Z. Bankroll cash (research-selected trades): 456.400154541351. Open positions: 21. Pools on watchlist: 53.

| group | n | win | avg | CI | P&L $ |
|---|---|---|---|---|---|
| research-picked | 16 | 25% | -33.9% | -64 to -3 | -544 |
| momentum, not picked | 2295 | 12% | -64.9% | -67 to -62 | -149154 |
| all momentum | 2311 | 12% | -64.7% | -67 to -62 | -149698 |
| control | 3041 | 6% | -18.4% | -20 to -17 | -56253 |
| dip buy | 32 | 28% | -15.4% | -37 to 5 | -493 |
| proven pools | 107 | 35% | -33.0% | -43 to -23 | -3544 |

What-if exit rules on the SAME trades. Cells: avg return (trades, win rate).

| exit rule | momentum | control | dip | proven |
|---|---|---|---|---|
| base_sl30_tp100 | -65% (2290, 12%) | -18% (3041, 6%) | -15% (32, 28%) | -33% (107, 35%) |
| wide_sl50_tp100 | -65% (2290, 13%) | -19% (3041, 6%) | -18% (32, 31%) | -34% (107, 35%) |
| sl30_tp50 | -66% (2290, 15%) | -19% (3041, 7%) | -20% (32, 31%) | -33% (107, 36%) |
| sl50_tp50 | -66% (2290, 16%) | -19% (3041, 7%) | -23% (32, 34%) | -34% (107, 36%) |
| no_stop_tp100 | -65% (2290, 14%) | -19% (3041, 6%) | -16% (32, 31%) | -35% (107, 35%) |

Verdict: NOT ENOUGH DATA (need 30+ closed filter=1 trades and a CI above zero before believing anything).

Pools seen: 80270. Outcomes:

- missed_window: 52601
- low_liquidity: 13208
- proven_liquidity_gone: 6627
- no_momentum: 3095
- research_failed: 2306
- proven_low_volume: 1111
- simulated failed buy: 989
- proven_price_collapsed_or_parabolic: 130
- proven: 107
- proven_no_uptrend: 48
- dip: 32
- research_passed: 16

Warning: 640 judged pools had an unreadable mint/freeze value. Check mint_raw / freeze_raw in candidates.csv; the parsing may need fixing.
