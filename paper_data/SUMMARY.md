# Paper trader summary

SIMULATION ONLY. No real trades.

Updated 2026-11-14T16:26:54Z. Bankroll cash (research-selected trades): 456.400154541351. Open positions: 14. Pools on watchlist: 55.

| group | n | win | avg | CI | P&L $ |
|---|---|---|---|---|---|
| research-picked | 16 | 25% | -33.9% | -64 to -3 | -544 |
| momentum, not picked | 2347 | 12% | -65.2% | -68 to -63 | -153204 |
| all momentum | 2363 | 12% | -65.0% | -67 to -63 | -153747 |
| control | 3086 | 6% | -18.5% | -20 to -17 | -57328 |
| dip buy | 32 | 28% | -15.4% | -37 to 5 | -493 |
| proven pools | 108 | 34% | -33.6% | -44 to -24 | -3644 |

What-if exit rules on the SAME trades. Cells: avg return (trades, win rate).

| exit rule | momentum | control | dip | proven |
|---|---|---|---|---|
| base_sl30_tp100 | -65% (2342, 12%) | -18% (3086, 6%) | -15% (32, 28%) | -34% (108, 34%) |
| wide_sl50_tp100 | -65% (2342, 13%) | -19% (3086, 6%) | -18% (32, 31%) | -35% (108, 34%) |
| sl30_tp50 | -66% (2342, 15%) | -19% (3086, 7%) | -20% (32, 31%) | -34% (108, 35%) |
| sl50_tp50 | -66% (2342, 16%) | -19% (3086, 7%) | -23% (32, 34%) | -35% (108, 35%) |
| no_stop_tp100 | -65% (2342, 14%) | -19% (3086, 6%) | -16% (32, 31%) | -36% (108, 34%) |

Verdict: NOT ENOUGH DATA (need 30+ closed filter=1 trades and a CI above zero before believing anything).

Pools seen: 81962. Outcomes:

- missed_window: 53758
- low_liquidity: 13472
- proven_liquidity_gone: 6776
- no_momentum: 3135
- research_failed: 2355
- proven_low_volume: 1124
- simulated failed buy: 1003
- proven_price_collapsed_or_parabolic: 131
- proven: 109
- proven_no_uptrend: 51
- dip: 32
- research_passed: 16

Warning: 646 judged pools had an unreadable mint/freeze value. Check mint_raw / freeze_raw in candidates.csv; the parsing may need fixing.
