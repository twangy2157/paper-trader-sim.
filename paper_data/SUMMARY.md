# Paper trader summary

SIMULATION ONLY. No real trades.

Updated 2026-11-11T22:12:56Z. Bankroll cash (research-selected trades): 456.400154541351. Open positions: 22. Pools on watchlist: 51.

| group | n | win | avg | CI | P&L $ |
|---|---|---|---|---|---|
| research-picked | 16 | 25% | -33.9% | -64 to -3 | -544 |
| momentum, not picked | 1801 | 12% | -64.9% | -68 to -62 | -117070 |
| all momentum | 1817 | 12% | -64.6% | -67 to -62 | -117613 |
| control | 2574 | 5% | -18.0% | -19 to -17 | -46494 |
| dip buy | 21 | 24% | -20.0% | -47 to 7 | -422 |
| proven pools | 87 | 36% | -28.3% | -39 to -18 | -2474 |

What-if exit rules on the SAME trades. Cells: avg return (trades, win rate).

| exit rule | momentum | control | dip | proven |
|---|---|---|---|---|
| base_sl30_tp100 | -65% (1796, 12%) | -18% (2574, 5%) | -20% (21, 24%) | -28% (87, 36%) |
| wide_sl50_tp100 | -65% (1796, 13%) | -18% (2574, 6%) | -24% (21, 29%) | -30% (87, 36%) |
| sl30_tp50 | -66% (1796, 15%) | -18% (2574, 6%) | -29% (21, 24%) | -29% (87, 36%) |
| sl50_tp50 | -66% (1796, 16%) | -18% (2574, 6%) | -33% (21, 29%) | -31% (87, 36%) |
| no_stop_tp100 | -65% (1796, 14%) | -19% (2574, 6%) | -20% (21, 29%) | -30% (87, 36%) |

Verdict: NOT ENOUGH DATA (need 30+ closed filter=1 trades and a CI above zero before believing anything).

Pools seen: 64935. Outcomes:

- missed_window: 42917
- low_liquidity: 10448
- proven_liquidity_gone: 5031
- no_momentum: 2631
- research_failed: 1810
- proven_low_volume: 1002
- simulated failed buy: 821
- proven_price_collapsed_or_parabolic: 114
- proven: 87
- proven_no_uptrend: 37
- dip: 21
- research_passed: 16

Warning: 546 judged pools had an unreadable mint/freeze value. Check mint_raw / freeze_raw in candidates.csv; the parsing may need fixing.
