# Paper trader summary

SIMULATION ONLY. No real trades.

Updated 2026-11-14T14:18:32Z. Bankroll cash (research-selected trades): 456.400154541351. Open positions: 11. Pools on watchlist: 111.

| group | n | win | avg | CI | P&L $ |
|---|---|---|---|---|---|
| research-picked | 16 | 25% | -33.9% | -64 to -3 | -544 |
| momentum, not picked | 2329 | 12% | -65.0% | -67 to -63 | -151644 |
| all momentum | 2345 | 12% | -64.8% | -67 to -62 | -152187 |
| control | 3071 | 6% | -18.4% | -20 to -17 | -56842 |
| dip buy | 32 | 28% | -15.4% | -37 to 5 | -493 |
| proven pools | 107 | 35% | -33.0% | -43 to -23 | -3544 |

What-if exit rules on the SAME trades. Cells: avg return (trades, win rate).

| exit rule | momentum | control | dip | proven |
|---|---|---|---|---|
| base_sl30_tp100 | -65% (2324, 12%) | -18% (3071, 6%) | -15% (32, 28%) | -33% (107, 35%) |
| wide_sl50_tp100 | -65% (2324, 13%) | -19% (3071, 6%) | -18% (32, 31%) | -34% (107, 35%) |
| sl30_tp50 | -66% (2324, 15%) | -19% (3071, 7%) | -20% (32, 31%) | -33% (107, 36%) |
| sl50_tp50 | -66% (2324, 16%) | -19% (3071, 7%) | -23% (32, 34%) | -34% (107, 36%) |
| no_stop_tp100 | -65% (2324, 14%) | -19% (3071, 6%) | -16% (32, 31%) | -35% (107, 35%) |

Verdict: NOT ENOUGH DATA (need 30+ closed filter=1 trades and a CI above zero before believing anything).

Pools seen: 81203. Outcomes:

- missed_window: 53214
- low_liquidity: 13361
- proven_liquidity_gone: 6717
- no_momentum: 3118
- research_failed: 2335
- proven_low_volume: 1120
- simulated failed buy: 1000
- proven_price_collapsed_or_parabolic: 131
- proven: 109
- proven_no_uptrend: 50
- dip: 32
- research_passed: 16

Warning: 646 judged pools had an unreadable mint/freeze value. Check mint_raw / freeze_raw in candidates.csv; the parsing may need fixing.
