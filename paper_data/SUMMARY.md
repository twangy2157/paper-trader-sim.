# Paper trader summary

SIMULATION ONLY. No real trades.

Updated 2026-11-15T05:13:16Z. Bankroll cash (research-selected trades): 456.400154541351. Open positions: 19. Pools on watchlist: 55.

| group | n | win | avg | CI | P&L $ |
|---|---|---|---|---|---|
| research-picked | 16 | 25% | -33.9% | -64 to -3 | -544 |
| momentum, not picked | 2446 | 12% | -65.5% | -68 to -63 | -160538 |
| all momentum | 2462 | 12% | -65.3% | -68 to -63 | -161082 |
| control | 3167 | 6% | -18.8% | -20 to -18 | -59835 |
| dip buy | 33 | 30% | -12.1% | -32 to 8 | -402 |
| proven pools | 110 | 34% | -34.0% | -44 to -24 | -3747 |

What-if exit rules on the SAME trades. Cells: avg return (trades, win rate).

| exit rule | momentum | control | dip | proven |
|---|---|---|---|---|
| base_sl30_tp100 | -66% (2441, 12%) | -19% (3167, 6%) | -12% (33, 30%) | -34% (110, 34%) |
| wide_sl50_tp100 | -66% (2441, 13%) | -19% (3167, 6%) | -15% (33, 33%) | -35% (110, 34%) |
| sl30_tp50 | -67% (2441, 14%) | -19% (3167, 7%) | -18% (33, 33%) | -34% (110, 35%) |
| sl50_tp50 | -67% (2441, 16%) | -19% (3167, 7%) | -21% (33, 36%) | -35% (110, 35%) |
| no_stop_tp100 | -65% (2441, 14%) | -19% (3167, 6%) | -13% (33, 33%) | -36% (110, 34%) |

Verdict: NOT ENOUGH DATA (need 30+ closed filter=1 trades and a CI above zero before believing anything).

Pools seen: 85809. Outcomes:

- missed_window: 56400
- low_liquidity: 14090
- proven_liquidity_gone: 7106
- no_momentum: 3220
- research_failed: 2456
- proven_low_volume: 1143
- simulated failed buy: 1048
- proven_price_collapsed_or_parabolic: 135
- proven: 110
- proven_no_uptrend: 52
- dip: 33
- research_passed: 16

Warning: 666 judged pools had an unreadable mint/freeze value. Check mint_raw / freeze_raw in candidates.csv; the parsing may need fixing.
