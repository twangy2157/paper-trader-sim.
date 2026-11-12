# Paper trader summary

SIMULATION ONLY. No real trades.

Updated 2026-11-12T05:05:15Z. Bankroll cash (research-selected trades): 456.400154541351. Open positions: 34. Pools on watchlist: 54.

| group | n | win | avg | CI | P&L $ |
|---|---|---|---|---|---|
| research-picked | 16 | 25% | -33.9% | -64 to -3 | -544 |
| momentum, not picked | 1860 | 12% | -64.6% | -67 to -62 | -120269 |
| all momentum | 1876 | 12% | -64.3% | -67 to -62 | -120812 |
| control | 2631 | 6% | -18.0% | -19 to -17 | -47514 |
| dip buy | 22 | 23% | -19.4% | -45 to 6 | -427 |
| proven pools | 88 | 35% | -28.5% | -39 to -18 | -2514 |

What-if exit rules on the SAME trades. Cells: avg return (trades, win rate).

| exit rule | momentum | control | dip | proven |
|---|---|---|---|---|
| base_sl30_tp100 | -65% (1855, 12%) | -18% (2631, 6%) | -19% (22, 23%) | -28% (88, 35%) |
| wide_sl50_tp100 | -65% (1855, 13%) | -18% (2631, 6%) | -23% (22, 27%) | -30% (88, 35%) |
| sl30_tp50 | -66% (1855, 15%) | -18% (2631, 6%) | -28% (22, 23%) | -30% (88, 35%) |
| sl50_tp50 | -66% (1855, 16%) | -18% (2631, 7%) | -32% (22, 27%) | -31% (88, 35%) |
| no_stop_tp100 | -65% (1855, 14%) | -18% (2631, 6%) | -20% (22, 27%) | -31% (88, 35%) |

Verdict: NOT ENOUGH DATA (need 30+ closed filter=1 trades and a CI above zero before believing anything).

Pools seen: 66730. Outcomes:

- missed_window: 44097
- low_liquidity: 10731
- proven_liquidity_gone: 5195
- no_momentum: 2689
- research_failed: 1877
- proven_low_volume: 1021
- simulated failed buy: 836
- proven_price_collapsed_or_parabolic: 116
- proven: 89
- proven_no_uptrend: 39
- dip: 24
- research_passed: 16

Warning: 554 judged pools had an unreadable mint/freeze value. Check mint_raw / freeze_raw in candidates.csv; the parsing may need fixing.
