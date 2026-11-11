# Paper trader summary

SIMULATION ONLY. No real trades.

Updated 2026-11-11T05:07:41Z. Bankroll cash (research-selected trades): 456.400154541351. Open positions: 23. Pools on watchlist: 35.

| group | n | win | avg | CI | P&L $ |
|---|---|---|---|---|---|
| research-picked | 16 | 25% | -33.9% | -64 to -3 | -544 |
| momentum, not picked | 1669 | 12% | -64.8% | -68 to -62 | -108336 |
| all momentum | 1685 | 12% | -64.5% | -67 to -62 | -108880 |
| control | 2416 | 5% | -18.0% | -20 to -17 | -43802 |
| dip buy | 19 | 21% | -21.9% | -46 to 3 | -416 |
| proven pools | 80 | 36% | -26.2% | -37 to -15 | -2106 |

What-if exit rules on the SAME trades. Cells: avg return (trades, win rate).

| exit rule | momentum | control | dip | proven |
|---|---|---|---|---|
| base_sl30_tp100 | -65% (1664, 12%) | -18% (2416, 5%) | -22% (19, 21%) | -26% (80, 36%) |
| wide_sl50_tp100 | -65% (1664, 13%) | -18% (2416, 5%) | -26% (19, 26%) | -28% (80, 36%) |
| sl30_tp50 | -66% (1664, 15%) | -18% (2416, 6%) | -30% (19, 21%) | -27% (80, 36%) |
| sl50_tp50 | -65% (1664, 16%) | -19% (2416, 6%) | -33% (19, 26%) | -29% (80, 36%) |
| no_stop_tp100 | -65% (1664, 14%) | -19% (2416, 5%) | -22% (19, 26%) | -28% (80, 36%) |

Verdict: NOT ENOUGH DATA (need 30+ closed filter=1 trades and a CI above zero before believing anything).

Pools seen: 60641. Outcomes:

- missed_window: 40179
- low_liquidity: 9725
- proven_liquidity_gone: 4593
- no_momentum: 2472
- research_failed: 1679
- proven_low_volume: 963
- simulated failed buy: 774
- proven_price_collapsed_or_parabolic: 104
- proven: 80
- proven_no_uptrend: 36
- dip: 20
- research_passed: 16

Warning: 516 judged pools had an unreadable mint/freeze value. Check mint_raw / freeze_raw in candidates.csv; the parsing may need fixing.
