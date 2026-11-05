# Paper trader summary

SIMULATION ONLY. No real trades.

Updated 2026-11-05T00:32:23Z. Bankroll cash (research-selected trades): 816.8065461812329. Open positions: 17. Pools on watchlist: 38.

| group | n | win | avg | CI | P&L $ |
|---|---|---|---|---|---|
| research-picked | 5 | 20% | -36.3% | - | -183 |
| momentum, not picked | 555 | 16% | -53.7% | -59 to -48 | -29854 |
| all momentum | 560 | 16% | -53.6% | -59 to -48 | -30038 |
| control | 686 | 7% | -19.1% | -22 to -16 | -13189 |
| dip buy | 4 | 25% | -13.1% | - | -52 |
| proven pools | 31 | 42% | -17.5% | -35 to -1 | -545 |

What-if exit rules on the SAME trades. Cells: avg return (trades, win rate).

| exit rule | momentum | control | dip | proven |
|---|---|---|---|---|
| base_sl30_tp100 | -54% (539, 16%) | -19% (686, 7%) | -13% (4, 25%) | -18% (31, 42%) |
| wide_sl50_tp100 | -54% (539, 18%) | -20% (686, 8%) | -13% (4, 25%) | -18% (31, 42%) |
| sl30_tp50 | -55% (539, 20%) | -20% (686, 8%) | -22% (4, 25%) | -19% (31, 42%) |
| sl50_tp50 | -55% (539, 22%) | -20% (686, 9%) | -22% (4, 25%) | -19% (31, 42%) |
| no_stop_tp100 | -53% (539, 19%) | -20% (686, 8%) | -13% (4, 25%) | -18% (31, 42%) |

Verdict: NOT ENOUGH DATA (need 30+ closed filter=1 trades and a CI above zero before believing anything).

Pools seen: 20475. Outcomes:

- missed_window: 13461
- low_liquidity: 3799
- proven_liquidity_gone: 1382
- no_momentum: 736
- research_failed: 565
- simulated failed buy: 230
- proven_low_volume: 197
- proven_price_collapsed_or_parabolic: 44
- proven: 32
- proven_no_uptrend: 20
- research_passed: 5
- dip: 4

Warning: 154 judged pools had an unreadable mint/freeze value. Check mint_raw / freeze_raw in candidates.csv; the parsing may need fixing.
