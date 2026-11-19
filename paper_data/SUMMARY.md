# Paper trader summary

SIMULATION ONLY. No real trades.

Updated 2026-11-19T20:26:28Z. Bankroll cash (research-selected trades): 506.50475787222217. Open positions: 13. Pools on watchlist: 54.

| group | n | win | avg | CI | P&L $ |
|---|---|---|---|---|---|
| research-picked | 18 | 33% | -21.7% | -51 to 11 | -394 |
| momentum, not picked | 3202 | 11% | -67.2% | -69 to -65 | -215493 |
| all momentum | 3220 | 11% | -67.0% | -69 to -65 | -215886 |
| control | 3920 | 6% | -19.1% | -20 to -18 | -75386 |
| dip buy | 41 | 27% | -12.0% | -29 to 6 | -494 |
| proven pools | 123 | 33% | -31.5% | -41 to -22 | -3883 |

What-if exit rules on the SAME trades. Cells: avg return (trades, win rate).

| exit rule | momentum | control | dip | proven |
|---|---|---|---|---|
| base_sl30_tp100 | -67% (3199, 11%) | -19% (3920, 6%) | -12% (41, 27%) | -31% (123, 33%) |
| wide_sl50_tp100 | -67% (3199, 13%) | -19% (3920, 7%) | -15% (41, 29%) | -32% (123, 33%) |
| sl30_tp50 | -68% (3199, 14%) | -19% (3920, 7%) | -18% (41, 29%) | -32% (123, 34%) |
| sl50_tp50 | -68% (3199, 15%) | -19% (3920, 8%) | -19% (41, 34%) | -33% (123, 34%) |
| no_stop_tp100 | -67% (3199, 13%) | -20% (3920, 7%) | -13% (41, 29%) | -33% (123, 33%) |

Verdict: NOT ENOUGH DATA (need 30+ closed filter=1 trades and a CI above zero before believing anything).

Pools seen: 106140. Outcomes:

- missed_window: 68983
- low_liquidity: 17741
- proven_liquidity_gone: 9137
- no_momentum: 3970
- research_failed: 3208
- proven_low_volume: 1369
- simulated failed buy: 1330
- proven_price_collapsed_or_parabolic: 158
- proven: 123
- proven_no_uptrend: 61
- dip: 41
- research_passed: 19

Warning: 839 judged pools had an unreadable mint/freeze value. Check mint_raw / freeze_raw in candidates.csv; the parsing may need fixing.
