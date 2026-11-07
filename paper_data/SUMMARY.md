# Paper trader summary

SIMULATION ONLY. No real trades.

Updated 2026-11-07T09:44:12Z. Bankroll cash (research-selected trades): 605.1869477321155. Open positions: 20. Pools on watchlist: 47.

| group | n | win | avg | CI | P&L $ |
|---|---|---|---|---|---|
| research-picked | 12 | 25% | -32.7% | -67 to 6 | -395 |
| momentum, not picked | 962 | 13% | -60.6% | -64 to -57 | -58364 |
| all momentum | 974 | 13% | -60.2% | -64 to -56 | -58758 |
| control | 1234 | 6% | -19.9% | -22 to -18 | -24658 |
| dip buy | 10 | 10% | -40.3% | -73 to -7 | -404 |
| proven pools | 48 | 46% | -16.2% | -30 to -3 | -783 |

What-if exit rules on the SAME trades. Cells: avg return (trades, win rate).

| exit rule | momentum | control | dip | proven |
|---|---|---|---|---|
| base_sl30_tp100 | -61% (953, 13%) | -20% (1234, 6%) | -40% (10, 10%) | -16% (48, 46%) |
| wide_sl50_tp100 | -60% (953, 15%) | -20% (1234, 7%) | -43% (10, 10%) | -16% (48, 46%) |
| sl30_tp50 | -62% (953, 16%) | -20% (1234, 7%) | -44% (10, 10%) | -18% (48, 46%) |
| sl50_tp50 | -62% (953, 18%) | -21% (1234, 8%) | -47% (10, 10%) | -18% (48, 46%) |
| no_stop_tp100 | -60% (953, 16%) | -21% (1234, 7%) | -40% (10, 10%) | -16% (48, 46%) |

Verdict: NOT ENOUGH DATA (need 30+ closed filter=1 trades and a CI above zero before believing anything).

Pools seen: 34214. Outcomes:

- missed_window: 22170
- low_liquidity: 6192
- proven_liquidity_gone: 2640
- no_momentum: 1289
- research_failed: 968
- simulated failed buy: 421
- proven_low_volume: 380
- proven_price_collapsed_or_parabolic: 58
- proven: 51
- proven_no_uptrend: 23
- research_passed: 12
- dip: 10

Warning: 268 judged pools had an unreadable mint/freeze value. Check mint_raw / freeze_raw in candidates.csv; the parsing may need fixing.
