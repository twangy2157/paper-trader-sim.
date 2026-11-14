# Paper trader summary

SIMULATION ONLY. No real trades.

Updated 2026-11-14T23:07:11Z. Bankroll cash (research-selected trades): 456.400154541351. Open positions: 12. Pools on watchlist: 51.

| group | n | win | avg | CI | P&L $ |
|---|---|---|---|---|---|
| research-picked | 16 | 25% | -33.9% | -64 to -3 | -544 |
| momentum, not picked | 2398 | 12% | -65.3% | -68 to -63 | -156892 |
| all momentum | 2414 | 12% | -65.1% | -67 to -63 | -157436 |
| control | 3127 | 6% | -18.6% | -20 to -17 | -58457 |
| dip buy | 32 | 28% | -15.4% | -37 to 5 | -493 |
| proven pools | 109 | 34% | -34.3% | -44 to -24 | -3744 |

What-if exit rules on the SAME trades. Cells: avg return (trades, win rate).

| exit rule | momentum | control | dip | proven |
|---|---|---|---|---|
| base_sl30_tp100 | -65% (2393, 12%) | -19% (3127, 6%) | -15% (32, 28%) | -34% (109, 34%) |
| wide_sl50_tp100 | -65% (2393, 13%) | -19% (3127, 6%) | -18% (32, 31%) | -36% (109, 34%) |
| sl30_tp50 | -66% (2393, 15%) | -19% (3127, 7%) | -20% (32, 31%) | -34% (109, 35%) |
| sl50_tp50 | -66% (2393, 16%) | -19% (3127, 7%) | -23% (32, 34%) | -36% (109, 35%) |
| no_stop_tp100 | -65% (2393, 14%) | -19% (3127, 6%) | -16% (32, 31%) | -36% (109, 34%) |

Verdict: NOT ENOUGH DATA (need 30+ closed filter=1 trades and a CI above zero before believing anything).

Pools seen: 84138. Outcomes:

- missed_window: 55279
- low_liquidity: 13821
- proven_liquidity_gone: 6956
- no_momentum: 3177
- research_failed: 2404
- proven_low_volume: 1132
- simulated failed buy: 1027
- proven_price_collapsed_or_parabolic: 134
- proven: 109
- proven_no_uptrend: 51
- dip: 32
- research_passed: 16

Warning: 652 judged pools had an unreadable mint/freeze value. Check mint_raw / freeze_raw in candidates.csv; the parsing may need fixing.
