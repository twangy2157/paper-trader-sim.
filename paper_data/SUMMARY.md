# Paper trader summary

SIMULATION ONLY. No real trades.

Updated 2026-11-12T00:28:31Z. Bankroll cash (research-selected trades): 456.400154541351. Open positions: 17. Pools on watchlist: 80.

| group | n | win | avg | CI | P&L $ |
|---|---|---|---|---|---|
| research-picked | 16 | 25% | -33.9% | -64 to -3 | -544 |
| momentum, not picked | 1819 | 12% | -64.6% | -67 to -62 | -117637 |
| all momentum | 1835 | 12% | -64.3% | -67 to -62 | -118180 |
| control | 2604 | 5% | -18.0% | -19 to -17 | -47155 |
| dip buy | 21 | 24% | -20.0% | -47 to 7 | -422 |
| proven pools | 87 | 36% | -28.3% | -39 to -18 | -2474 |

What-if exit rules on the SAME trades. Cells: avg return (trades, win rate).

| exit rule | momentum | control | dip | proven |
|---|---|---|---|---|
| base_sl30_tp100 | -65% (1814, 12%) | -18% (2604, 5%) | -20% (21, 24%) | -28% (87, 36%) |
| wide_sl50_tp100 | -65% (1814, 13%) | -18% (2604, 6%) | -24% (21, 29%) | -30% (87, 36%) |
| sl30_tp50 | -66% (1814, 15%) | -18% (2604, 6%) | -29% (21, 24%) | -29% (87, 36%) |
| sl50_tp50 | -65% (1814, 16%) | -19% (2604, 6%) | -33% (21, 29%) | -31% (87, 36%) |
| no_stop_tp100 | -65% (1814, 14%) | -19% (2604, 6%) | -20% (21, 29%) | -30% (87, 36%) |

Verdict: NOT ENOUGH DATA (need 30+ closed filter=1 trades and a CI above zero before believing anything).

Pools seen: 65599. Outcomes:

- missed_window: 43366
- low_liquidity: 10550
- proven_liquidity_gone: 5089
- no_momentum: 2655
- research_failed: 1827
- proven_low_volume: 1009
- simulated failed buy: 825
- proven_price_collapsed_or_parabolic: 114
- proven: 88
- proven_no_uptrend: 38
- dip: 22
- research_passed: 16

Warning: 549 judged pools had an unreadable mint/freeze value. Check mint_raw / freeze_raw in candidates.csv; the parsing may need fixing.
