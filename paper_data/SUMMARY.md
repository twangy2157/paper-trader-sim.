# Paper trader summary

SIMULATION ONLY. No real trades.

Updated 2026-11-07T04:00:41Z. Bankroll cash (research-selected trades): 605.1869477321155. Open positions: 18. Pools on watchlist: 67.

| group | n | win | avg | CI | P&L $ |
|---|---|---|---|---|---|
| research-picked | 12 | 25% | -32.7% | -67 to 6 | -395 |
| momentum, not picked | 923 | 13% | -60.2% | -64 to -56 | -55617 |
| all momentum | 935 | 13% | -59.8% | -64 to -56 | -56012 |
| control | 1166 | 6% | -19.8% | -22 to -18 | -23147 |
| dip buy | 10 | 10% | -40.3% | -73 to -7 | -404 |
| proven pools | 46 | 46% | -14.8% | -29 to -1 | -684 |

What-if exit rules on the SAME trades. Cells: avg return (trades, win rate).

| exit rule | momentum | control | dip | proven |
|---|---|---|---|---|
| base_sl30_tp100 | -60% (914, 14%) | -20% (1166, 6%) | -40% (10, 10%) | -15% (46, 46%) |
| wide_sl50_tp100 | -60% (914, 15%) | -20% (1166, 7%) | -43% (10, 10%) | -15% (46, 46%) |
| sl30_tp50 | -62% (914, 16%) | -20% (1166, 7%) | -44% (10, 10%) | -17% (46, 46%) |
| sl50_tp50 | -61% (914, 18%) | -20% (1166, 8%) | -47% (10, 10%) | -17% (46, 46%) |
| no_stop_tp100 | -60% (914, 16%) | -21% (1166, 7%) | -40% (10, 10%) | -15% (46, 46%) |

Verdict: NOT ENOUGH DATA (need 30+ closed filter=1 trades and a CI above zero before believing anything).

Pools seen: 32788. Outcomes:

- missed_window: 21273
- low_liquidity: 5953
- proven_liquidity_gone: 2503
- no_momentum: 1222
- research_failed: 928
- simulated failed buy: 403
- proven_low_volume: 357
- proven_price_collapsed_or_parabolic: 58
- proven: 47
- proven_no_uptrend: 22
- research_passed: 12
- dip: 10

Warning: 255 judged pools had an unreadable mint/freeze value. Check mint_raw / freeze_raw in candidates.csv; the parsing may need fixing.
