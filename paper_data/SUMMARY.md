# Paper trader summary

SIMULATION ONLY. No real trades.

Updated 2026-11-11T17:48:09Z. Bankroll cash (research-selected trades): 456.400154541351. Open positions: 30. Pools on watchlist: 53.

| group | n | win | avg | CI | P&L $ |
|---|---|---|---|---|---|
| research-picked | 16 | 25% | -33.9% | -64 to -3 | -544 |
| momentum, not picked | 1768 | 12% | -64.7% | -68 to -62 | -114580 |
| all momentum | 1784 | 12% | -64.4% | -67 to -62 | -115123 |
| control | 2534 | 5% | -18.0% | -19 to -17 | -45884 |
| dip buy | 21 | 24% | -20.0% | -47 to 7 | -422 |
| proven pools | 85 | 36% | -27.8% | -38 to -17 | -2368 |

What-if exit rules on the SAME trades. Cells: avg return (trades, win rate).

| exit rule | momentum | control | dip | proven |
|---|---|---|---|---|
| base_sl30_tp100 | -65% (1763, 12%) | -18% (2534, 5%) | -20% (21, 24%) | -28% (85, 36%) |
| wide_sl50_tp100 | -65% (1763, 13%) | -18% (2534, 6%) | -24% (21, 29%) | -29% (85, 36%) |
| sl30_tp50 | -66% (1763, 15%) | -18% (2534, 6%) | -29% (21, 24%) | -29% (85, 36%) |
| sl50_tp50 | -66% (1763, 16%) | -18% (2534, 7%) | -33% (21, 29%) | -30% (85, 36%) |
| no_stop_tp100 | -65% (1763, 14%) | -19% (2534, 6%) | -20% (21, 29%) | -29% (85, 36%) |

Verdict: NOT ENOUGH DATA (need 30+ closed filter=1 trades and a CI above zero before believing anything).

Pools seen: 63699. Outcomes:

- missed_window: 42079
- low_liquidity: 10255
- proven_liquidity_gone: 4929
- no_momentum: 2597
- research_failed: 1778
- proven_low_volume: 983
- simulated failed buy: 809
- proven_price_collapsed_or_parabolic: 109
- proven: 86
- proven_no_uptrend: 37
- dip: 21
- research_passed: 16

Warning: 541 judged pools had an unreadable mint/freeze value. Check mint_raw / freeze_raw in candidates.csv; the parsing may need fixing.
