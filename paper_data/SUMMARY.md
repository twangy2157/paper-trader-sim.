# Paper trader summary

SIMULATION ONLY. No real trades.

Updated 2026-11-08T16:05:29Z. Bankroll cash (research-selected trades): 456.400154541351. Open positions: 19. Pools on watchlist: 51.

| group | n | win | avg | CI | P&L $ |
|---|---|---|---|---|---|
| research-picked | 16 | 25% | -33.9% | -64 to -3 | -544 |
| momentum, not picked | 1181 | 12% | -63.3% | -67 to -60 | -74875 |
| all momentum | 1197 | 13% | -62.9% | -66 to -59 | -75419 |
| control | 1582 | 6% | -19.0% | -21 to -17 | -30146 |
| dip buy | 11 | 9% | -40.6% | -69 to -11 | -447 |
| proven pools | 56 | 46% | -16.4% | -30 to -3 | -927 |

What-if exit rules on the SAME trades. Cells: avg return (trades, win rate).

| exit rule | momentum | control | dip | proven |
|---|---|---|---|---|
| base_sl30_tp100 | -63% (1176, 13%) | -19% (1582, 6%) | -41% (11, 9%) | -16% (56, 46%) |
| wide_sl50_tp100 | -63% (1176, 14%) | -19% (1582, 6%) | -48% (11, 9%) | -16% (56, 46%) |
| sl30_tp50 | -65% (1176, 15%) | -19% (1582, 6%) | -44% (11, 9%) | -18% (56, 46%) |
| sl50_tp50 | -64% (1176, 17%) | -19% (1582, 7%) | -52% (11, 9%) | -18% (56, 46%) |
| no_stop_tp100 | -63% (1176, 15%) | -20% (1582, 6%) | -45% (11, 9%) | -16% (56, 46%) |

Verdict: NOT ENOUGH DATA (need 30+ closed filter=1 trades and a CI above zero before believing anything).

Pools seen: 42775. Outcomes:

- missed_window: 28016
- low_liquidity: 7366
- proven_liquidity_gone: 3315
- no_momentum: 1635
- research_failed: 1190
- proven_low_volume: 562
- simulated failed buy: 510
- proven_price_collapsed_or_parabolic: 73
- proven: 57
- proven_no_uptrend: 24
- research_passed: 16
- dip: 11

Warning: 320 judged pools had an unreadable mint/freeze value. Check mint_raw / freeze_raw in candidates.csv; the parsing may need fixing.
