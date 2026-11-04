# Paper trader summary

SIMULATION ONLY. No real trades.

Updated 2026-11-04T16:05:10Z. Bankroll cash (research-selected trades): 759.5946161788225. Open positions: 11. Pools on watchlist: 64.

| group | n | win | avg | CI | P&L $ |
|---|---|---|---|---|---|
| research-picked | 2 | 0% | -69.5% | - | -140 |
| momentum, not picked | 498 | 15% | -54.1% | -60 to -49 | -26996 |
| all momentum | 500 | 15% | -54.2% | -60 to -48 | -27136 |
| control | 599 | 7% | -18.6% | -22 to -16 | -11224 |
| dip buy | 4 | 25% | -13.1% | - | -52 |
| proven pools | 27 | 41% | -15.9% | -35 to 2 | -431 |

What-if exit rules on the SAME trades. Cells: avg return (trades, win rate).

| exit rule | momentum | control | dip | proven |
|---|---|---|---|---|
| base_sl30_tp100 | -55% (479, 15%) | -19% (599, 7%) | -13% (4, 25%) | -16% (27, 41%) |
| wide_sl50_tp100 | -55% (479, 18%) | -19% (599, 8%) | -13% (4, 25%) | -16% (27, 41%) |
| sl30_tp50 | -57% (479, 19%) | -19% (599, 8%) | -22% (4, 25%) | -18% (27, 41%) |
| sl50_tp50 | -56% (479, 21%) | -19% (599, 9%) | -22% (4, 25%) | -18% (27, 41%) |
| no_stop_tp100 | -54% (479, 19%) | -20% (599, 8%) | -13% (4, 25%) | -16% (27, 41%) |

Verdict: NOT ENOUGH DATA (need 30+ closed filter=1 trades and a CI above zero before believing anything).

Pools seen: 18423. Outcomes:

- missed_window: 12201
- low_liquidity: 3427
- proven_liquidity_gone: 1178
- no_momentum: 647
- research_failed: 502
- simulated failed buy: 209
- proven_low_volume: 174
- proven_price_collapsed_or_parabolic: 34
- proven: 29
- proven_no_uptrend: 15
- dip: 4
- research_passed: 3

Warning: 139 judged pools had an unreadable mint/freeze value. Check mint_raw / freeze_raw in candidates.csv; the parsing may need fixing.
