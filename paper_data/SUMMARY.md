# Paper trader summary

SIMULATION ONLY. No real trades.

Updated 2026-11-14T20:13:45Z. Bankroll cash (research-selected trades): 456.400154541351. Open positions: 14. Pools on watchlist: 70.

| group | n | win | avg | CI | P&L $ |
|---|---|---|---|---|---|
| research-picked | 16 | 25% | -33.9% | -64 to -3 | -544 |
| momentum, not picked | 2376 | 12% | -65.3% | -68 to -63 | -155384 |
| all momentum | 2392 | 12% | -65.1% | -67 to -63 | -155927 |
| control | 3111 | 6% | -18.5% | -20 to -17 | -57894 |
| dip buy | 32 | 28% | -15.4% | -37 to 5 | -493 |
| proven pools | 109 | 34% | -34.3% | -44 to -24 | -3744 |

What-if exit rules on the SAME trades. Cells: avg return (trades, win rate).

| exit rule | momentum | control | dip | proven |
|---|---|---|---|---|
| base_sl30_tp100 | -65% (2371, 12%) | -19% (3111, 6%) | -15% (32, 28%) | -34% (109, 34%) |
| wide_sl50_tp100 | -65% (2371, 13%) | -19% (3111, 6%) | -18% (32, 31%) | -36% (109, 34%) |
| sl30_tp50 | -66% (2371, 15%) | -19% (3111, 7%) | -20% (32, 31%) | -34% (109, 35%) |
| sl50_tp50 | -66% (2371, 16%) | -19% (3111, 7%) | -23% (32, 34%) | -36% (109, 35%) |
| no_stop_tp100 | -65% (2371, 14%) | -19% (3111, 6%) | -16% (32, 31%) | -36% (109, 34%) |

Verdict: NOT ENOUGH DATA (need 30+ closed filter=1 trades and a CI above zero before believing anything).

Pools seen: 83040. Outcomes:

- missed_window: 54478
- low_liquidity: 13650
- proven_liquidity_gone: 6876
- no_momentum: 3162
- research_failed: 2383
- proven_low_volume: 1130
- simulated failed buy: 1021
- proven_price_collapsed_or_parabolic: 132
- proven: 109
- proven_no_uptrend: 51
- dip: 32
- research_passed: 16

Warning: 650 judged pools had an unreadable mint/freeze value. Check mint_raw / freeze_raw in candidates.csv; the parsing may need fixing.
