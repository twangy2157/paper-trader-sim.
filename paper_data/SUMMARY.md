# Paper trader summary

SIMULATION ONLY. No real trades.

Updated 2026-11-04T21:05:40Z. Bankroll cash (research-selected trades): 816.8065461812329. Open positions: 19. Pools on watchlist: 47.

| group | n | win | avg | CI | P&L $ |
|---|---|---|---|---|---|
| research-picked | 5 | 20% | -36.3% | - | -183 |
| momentum, not picked | 529 | 16% | -53.1% | -58 to -48 | -28111 |
| all momentum | 534 | 16% | -52.9% | -58 to -47 | -28294 |
| control | 646 | 7% | -18.8% | -22 to -16 | -12193 |
| dip buy | 4 | 25% | -13.1% | - | -52 |
| proven pools | 29 | 41% | -18.2% | -37 to -1 | -530 |

What-if exit rules on the SAME trades. Cells: avg return (trades, win rate).

| exit rule | momentum | control | dip | proven |
|---|---|---|---|---|
| base_sl30_tp100 | -54% (513, 16%) | -19% (646, 7%) | -13% (4, 25%) | -18% (29, 41%) |
| wide_sl50_tp100 | -53% (513, 18%) | -19% (646, 8%) | -13% (4, 25%) | -18% (29, 41%) |
| sl30_tp50 | -55% (513, 20%) | -19% (646, 8%) | -22% (4, 25%) | -20% (29, 41%) |
| sl50_tp50 | -54% (513, 23%) | -19% (646, 9%) | -22% (4, 25%) | -20% (29, 41%) |
| no_stop_tp100 | -52% (513, 19%) | -20% (646, 8%) | -13% (4, 25%) | -18% (29, 41%) |

Verdict: NOT ENOUGH DATA (need 30+ closed filter=1 trades and a CI above zero before believing anything).

Pools seen: 19713. Outcomes:

- missed_window: 13031
- low_liquidity: 3649
- proven_liquidity_gone: 1287
- no_momentum: 696
- research_failed: 540
- simulated failed buy: 223
- proven_low_volume: 187
- proven_price_collapsed_or_parabolic: 40
- proven: 31
- proven_no_uptrend: 20
- research_passed: 5
- dip: 4

Warning: 150 judged pools had an unreadable mint/freeze value. Check mint_raw / freeze_raw in candidates.csv; the parsing may need fixing.
