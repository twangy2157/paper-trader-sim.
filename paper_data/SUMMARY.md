# Paper trader summary

SIMULATION ONLY. No real trades.

Updated 2026-11-10T20:55:01Z. Bankroll cash (research-selected trades): 456.400154541351. Open positions: 34. Pools on watchlist: 46.

| group | n | win | avg | CI | P&L $ |
|---|---|---|---|---|---|
| research-picked | 16 | 25% | -33.9% | -64 to -3 | -544 |
| momentum, not picked | 1603 | 12% | -64.5% | -67 to -62 | -103530 |
| all momentum | 1619 | 12% | -64.2% | -67 to -61 | -104074 |
| control | 2329 | 5% | -18.0% | -19 to -17 | -42142 |
| dip buy | 16 | 19% | -24.9% | -52 to 4 | -400 |
| proven pools | 78 | 37% | -26.4% | -38 to -15 | -2065 |

What-if exit rules on the SAME trades. Cells: avg return (trades, win rate).

| exit rule | momentum | control | dip | proven |
|---|---|---|---|---|
| base_sl30_tp100 | -65% (1598, 12%) | -18% (2329, 5%) | -25% (16, 19%) | -26% (78, 37%) |
| wide_sl50_tp100 | -64% (1598, 14%) | -18% (2329, 5%) | -31% (16, 19%) | -27% (78, 37%) |
| sl30_tp50 | -65% (1598, 15%) | -18% (2329, 6%) | -32% (16, 19%) | -28% (78, 37%) |
| sl50_tp50 | -65% (1598, 17%) | -19% (2329, 6%) | -38% (16, 19%) | -28% (78, 37%) |
| no_stop_tp100 | -64% (1598, 14%) | -19% (2329, 5%) | -27% (16, 19%) | -27% (78, 37%) |

Verdict: NOT ENOUGH DATA (need 30+ closed filter=1 trades and a CI above zero before believing anything).

Pools seen: 58602. Outcomes:

- missed_window: 38869
- low_liquidity: 9400
- proven_liquidity_gone: 4411
- no_momentum: 2393
- research_failed: 1615
- proven_low_volume: 919
- simulated failed buy: 745
- proven_price_collapsed_or_parabolic: 102
- proven: 79
- proven_no_uptrend: 36
- dip: 17
- research_passed: 16

Warning: 498 judged pools had an unreadable mint/freeze value. Check mint_raw / freeze_raw in candidates.csv; the parsing may need fixing.
