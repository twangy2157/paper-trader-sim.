# Paper trader summary

SIMULATION ONLY. No real trades.

Updated 2026-11-10T23:55:11Z. Bankroll cash (research-selected trades): 456.400154541351. Open positions: 24. Pools on watchlist: 45.

| group | n | win | avg | CI | P&L $ |
|---|---|---|---|---|---|
| research-picked | 16 | 25% | -33.9% | -64 to -3 | -544 |
| momentum, not picked | 1632 | 12% | -64.7% | -68 to -62 | -105815 |
| all momentum | 1648 | 12% | -64.4% | -67 to -62 | -106359 |
| control | 2370 | 5% | -18.0% | -19 to -17 | -42839 |
| dip buy | 17 | 24% | -20.2% | -47 to 8 | -345 |
| proven pools | 79 | 37% | -26.1% | -37 to -15 | -2066 |

What-if exit rules on the SAME trades. Cells: avg return (trades, win rate).

| exit rule | momentum | control | dip | proven |
|---|---|---|---|---|
| base_sl30_tp100 | -65% (1627, 12%) | -18% (2370, 5%) | -20% (17, 24%) | -26% (79, 37%) |
| wide_sl50_tp100 | -64% (1627, 13%) | -18% (2370, 5%) | -26% (17, 24%) | -27% (79, 37%) |
| sl30_tp50 | -66% (1627, 15%) | -18% (2370, 6%) | -29% (17, 24%) | -27% (79, 37%) |
| sl50_tp50 | -65% (1627, 16%) | -18% (2370, 6%) | -34% (17, 24%) | -28% (79, 37%) |
| no_stop_tp100 | -65% (1627, 14%) | -19% (2370, 5%) | -22% (17, 24%) | -27% (79, 37%) |

Verdict: NOT ENOUGH DATA (need 30+ closed filter=1 trades and a CI above zero before believing anything).

Pools seen: 59417. Outcomes:

- missed_window: 39393
- low_liquidity: 9525
- proven_liquidity_gone: 4475
- no_momentum: 2426
- research_failed: 1644
- proven_low_volume: 941
- simulated failed buy: 762
- proven_price_collapsed_or_parabolic: 103
- proven: 79
- proven_no_uptrend: 36
- dip: 17
- research_passed: 16

Warning: 509 judged pools had an unreadable mint/freeze value. Check mint_raw / freeze_raw in candidates.csv; the parsing may need fixing.
