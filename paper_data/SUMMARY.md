# Paper trader summary

SIMULATION ONLY. No real trades.

Updated 2026-11-15T05:02:08Z. Bankroll cash (research-selected trades): 456.400154541351. Open positions: 18. Pools on watchlist: 49.

| group | n | win | avg | CI | P&L $ |
|---|---|---|---|---|---|
| research-picked | 16 | 25% | -33.9% | -64 to -3 | -544 |
| momentum, not picked | 2444 | 12% | -65.6% | -68 to -63 | -160626 |
| all momentum | 2460 | 12% | -65.4% | -68 to -63 | -161170 |
| control | 3166 | 6% | -18.8% | -20 to -18 | -59763 |
| dip buy | 33 | 30% | -12.1% | -32 to 8 | -402 |
| proven pools | 110 | 34% | -34.0% | -44 to -24 | -3747 |

What-if exit rules on the SAME trades. Cells: avg return (trades, win rate).

| exit rule | momentum | control | dip | proven |
|---|---|---|---|---|
| base_sl30_tp100 | -66% (2439, 12%) | -19% (3166, 6%) | -12% (33, 30%) | -34% (110, 34%) |
| wide_sl50_tp100 | -66% (2439, 13%) | -19% (3166, 6%) | -15% (33, 33%) | -35% (110, 34%) |
| sl30_tp50 | -67% (2439, 14%) | -19% (3166, 7%) | -18% (33, 33%) | -34% (110, 35%) |
| sl50_tp50 | -67% (2439, 16%) | -19% (3166, 7%) | -21% (33, 36%) | -35% (110, 35%) |
| no_stop_tp100 | -66% (2439, 14%) | -19% (3166, 6%) | -13% (33, 33%) | -36% (110, 34%) |

Verdict: NOT ENOUGH DATA (need 30+ closed filter=1 trades and a CI above zero before believing anything).

Pools seen: 85763. Outcomes:

- missed_window: 56371
- low_liquidity: 14083
- proven_liquidity_gone: 7100
- no_momentum: 3216
- research_failed: 2456
- proven_low_volume: 1143
- simulated failed buy: 1048
- proven_price_collapsed_or_parabolic: 135
- proven: 110
- proven_no_uptrend: 52
- dip: 33
- research_passed: 16

Warning: 666 judged pools had an unreadable mint/freeze value. Check mint_raw / freeze_raw in candidates.csv; the parsing may need fixing.
