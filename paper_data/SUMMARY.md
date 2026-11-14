# Paper trader summary

SIMULATION ONLY. No real trades.

Updated 2026-11-14T16:16:30Z. Bankroll cash (research-selected trades): 456.400154541351. Open positions: 16. Pools on watchlist: 69.

| group | n | win | avg | CI | P&L $ |
|---|---|---|---|---|---|
| research-picked | 16 | 25% | -33.9% | -64 to -3 | -544 |
| momentum, not picked | 2346 | 12% | -65.2% | -67 to -63 | -153103 |
| all momentum | 2362 | 12% | -65.0% | -67 to -63 | -153647 |
| control | 3084 | 6% | -18.5% | -20 to -17 | -57217 |
| dip buy | 32 | 28% | -15.4% | -37 to 5 | -493 |
| proven pools | 108 | 34% | -33.6% | -44 to -24 | -3644 |

What-if exit rules on the SAME trades. Cells: avg return (trades, win rate).

| exit rule | momentum | control | dip | proven |
|---|---|---|---|---|
| base_sl30_tp100 | -65% (2341, 12%) | -18% (3084, 6%) | -15% (32, 28%) | -34% (108, 34%) |
| wide_sl50_tp100 | -65% (2341, 13%) | -19% (3084, 6%) | -18% (32, 31%) | -35% (108, 34%) |
| sl30_tp50 | -66% (2341, 15%) | -19% (3084, 7%) | -20% (32, 31%) | -34% (108, 35%) |
| sl50_tp50 | -66% (2341, 16%) | -19% (3084, 7%) | -23% (32, 34%) | -35% (108, 35%) |
| no_stop_tp100 | -65% (2341, 14%) | -19% (3084, 6%) | -16% (32, 31%) | -36% (108, 34%) |

Verdict: NOT ENOUGH DATA (need 30+ closed filter=1 trades and a CI above zero before believing anything).

Pools seen: 81909. Outcomes:

- missed_window: 53724
- low_liquidity: 13462
- proven_liquidity_gone: 6769
- no_momentum: 3135
- research_failed: 2354
- proven_low_volume: 1124
- simulated failed buy: 1002
- proven_price_collapsed_or_parabolic: 131
- proven: 109
- proven_no_uptrend: 51
- dip: 32
- research_passed: 16

Warning: 646 judged pools had an unreadable mint/freeze value. Check mint_raw / freeze_raw in candidates.csv; the parsing may need fixing.
