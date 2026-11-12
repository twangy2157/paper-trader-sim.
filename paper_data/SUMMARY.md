# Paper trader summary

SIMULATION ONLY. No real trades.

Updated 2026-11-12T01:33:55Z. Bankroll cash (research-selected trades): 456.400154541351. Open positions: 7. Pools on watchlist: 64.

| group | n | win | avg | CI | P&L $ |
|---|---|---|---|---|---|
| research-picked | 16 | 25% | -33.9% | -64 to -3 | -544 |
| momentum, not picked | 1827 | 12% | -64.6% | -67 to -62 | -118257 |
| all momentum | 1843 | 12% | -64.4% | -67 to -62 | -118800 |
| control | 2611 | 5% | -18.0% | -19 to -17 | -47267 |
| dip buy | 22 | 23% | -19.4% | -45 to 6 | -427 |
| proven pools | 88 | 35% | -28.5% | -39 to -18 | -2514 |

What-if exit rules on the SAME trades. Cells: avg return (trades, win rate).

| exit rule | momentum | control | dip | proven |
|---|---|---|---|---|
| base_sl30_tp100 | -65% (1822, 12%) | -18% (2611, 5%) | -19% (22, 23%) | -28% (88, 35%) |
| wide_sl50_tp100 | -65% (1822, 13%) | -18% (2611, 6%) | -23% (22, 27%) | -30% (88, 35%) |
| sl30_tp50 | -66% (1822, 15%) | -18% (2611, 6%) | -28% (22, 23%) | -30% (88, 35%) |
| sl50_tp50 | -66% (1822, 16%) | -18% (2611, 7%) | -32% (22, 27%) | -31% (88, 35%) |
| no_stop_tp100 | -65% (1822, 14%) | -19% (2611, 6%) | -20% (22, 27%) | -31% (88, 35%) |

Verdict: NOT ENOUGH DATA (need 30+ closed filter=1 trades and a CI above zero before believing anything).

Pools seen: 65826. Outcomes:

- missed_window: 43543
- low_liquidity: 10570
- proven_liquidity_gone: 5108
- no_momentum: 2657
- research_failed: 1832
- proven_low_volume: 1013
- simulated failed buy: 825
- proven_price_collapsed_or_parabolic: 114
- proven: 88
- proven_no_uptrend: 38
- dip: 22
- research_passed: 16

Warning: 549 judged pools had an unreadable mint/freeze value. Check mint_raw / freeze_raw in candidates.csv; the parsing may need fixing.
