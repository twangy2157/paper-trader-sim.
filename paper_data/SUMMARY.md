# Paper trader summary

SIMULATION ONLY. No real trades.

Updated 2026-11-12T01:12:54Z. Bankroll cash (research-selected trades): 456.400154541351. Open positions: 9. Pools on watchlist: 72.

| group | n | win | avg | CI | P&L $ |
|---|---|---|---|---|---|
| research-picked | 16 | 25% | -33.9% | -64 to -3 | -544 |
| momentum, not picked | 1824 | 12% | -64.6% | -67 to -62 | -117957 |
| all momentum | 1840 | 12% | -64.3% | -67 to -62 | -118500 |
| control | 2608 | 5% | -18.0% | -19 to -17 | -47209 |
| dip buy | 21 | 24% | -20.0% | -47 to 7 | -422 |
| proven pools | 87 | 36% | -28.3% | -39 to -18 | -2474 |

What-if exit rules on the SAME trades. Cells: avg return (trades, win rate).

| exit rule | momentum | control | dip | proven |
|---|---|---|---|---|
| base_sl30_tp100 | -65% (1819, 12%) | -18% (2608, 5%) | -20% (21, 24%) | -28% (87, 36%) |
| wide_sl50_tp100 | -65% (1819, 13%) | -18% (2608, 6%) | -24% (21, 29%) | -30% (87, 36%) |
| sl30_tp50 | -66% (1819, 15%) | -18% (2608, 6%) | -29% (21, 24%) | -29% (87, 36%) |
| sl50_tp50 | -65% (1819, 16%) | -19% (2608, 6%) | -33% (21, 29%) | -31% (87, 36%) |
| no_stop_tp100 | -65% (1819, 14%) | -19% (2608, 6%) | -20% (21, 29%) | -30% (87, 36%) |

Verdict: NOT ENOUGH DATA (need 30+ closed filter=1 trades and a CI above zero before believing anything).

Pools seen: 65712. Outcomes:

- missed_window: 43463
- low_liquidity: 10556
- proven_liquidity_gone: 5096
- no_momentum: 2656
- research_failed: 1827
- proven_low_volume: 1011
- simulated failed buy: 825
- proven_price_collapsed_or_parabolic: 114
- proven: 88
- proven_no_uptrend: 38
- dip: 22
- research_passed: 16

Warning: 549 judged pools had an unreadable mint/freeze value. Check mint_raw / freeze_raw in candidates.csv; the parsing may need fixing.
