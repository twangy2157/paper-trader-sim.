# Paper trader summary

SIMULATION ONLY. No real trades.

Updated 2026-11-11T23:25:54Z. Bankroll cash (research-selected trades): 456.400154541351. Open positions: 24. Pools on watchlist: 120.

| group | n | win | avg | CI | P&L $ |
|---|---|---|---|---|---|
| research-picked | 16 | 25% | -33.9% | -64 to -3 | -544 |
| momentum, not picked | 1811 | 12% | -64.8% | -68 to -62 | -117492 |
| all momentum | 1827 | 12% | -64.5% | -67 to -62 | -118036 |
| control | 2589 | 5% | -18.0% | -19 to -17 | -46802 |
| dip buy | 21 | 24% | -20.0% | -47 to 7 | -422 |
| proven pools | 87 | 36% | -28.3% | -39 to -18 | -2474 |

What-if exit rules on the SAME trades. Cells: avg return (trades, win rate).

| exit rule | momentum | control | dip | proven |
|---|---|---|---|---|
| base_sl30_tp100 | -65% (1806, 12%) | -18% (2589, 5%) | -20% (21, 24%) | -28% (87, 36%) |
| wide_sl50_tp100 | -65% (1806, 13%) | -18% (2589, 6%) | -24% (21, 29%) | -30% (87, 36%) |
| sl30_tp50 | -66% (1806, 15%) | -18% (2589, 6%) | -29% (21, 24%) | -29% (87, 36%) |
| sl50_tp50 | -66% (1806, 16%) | -18% (2589, 6%) | -33% (21, 29%) | -31% (87, 36%) |
| no_stop_tp100 | -65% (1806, 14%) | -19% (2589, 6%) | -20% (21, 29%) | -30% (87, 36%) |

Verdict: NOT ENOUGH DATA (need 30+ closed filter=1 trades and a CI above zero before believing anything).

Pools seen: 65276. Outcomes:

- missed_window: 43141
- low_liquidity: 10500
- proven_liquidity_gone: 5063
- no_momentum: 2648
- research_failed: 1819
- proven_low_volume: 1006
- simulated failed buy: 823
- proven_price_collapsed_or_parabolic: 114
- proven: 88
- proven_no_uptrend: 37
- dip: 21
- research_passed: 16

Warning: 547 judged pools had an unreadable mint/freeze value. Check mint_raw / freeze_raw in candidates.csv; the parsing may need fixing.
