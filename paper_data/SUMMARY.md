# Paper trader summary

SIMULATION ONLY. No real trades.

Updated 2026-11-11T15:08:01Z. Bankroll cash (research-selected trades): 456.400154541351. Open positions: 19. Pools on watchlist: 61.

| group | n | win | avg | CI | P&L $ |
|---|---|---|---|---|---|
| research-picked | 16 | 25% | -33.9% | -64 to -3 | -544 |
| momentum, not picked | 1746 | 12% | -64.9% | -67 to -62 | -113390 |
| all momentum | 1762 | 12% | -64.6% | -67 to -62 | -113933 |
| control | 2515 | 5% | -17.9% | -19 to -16 | -45147 |
| dip buy | 20 | 25% | -16.1% | -42 to 10 | -323 |
| proven pools | 84 | 36% | -28.3% | -40 to -18 | -2382 |

What-if exit rules on the SAME trades. Cells: avg return (trades, win rate).

| exit rule | momentum | control | dip | proven |
|---|---|---|---|---|
| base_sl30_tp100 | -65% (1741, 12%) | -18% (2515, 5%) | -16% (20, 25%) | -28% (84, 36%) |
| wide_sl50_tp100 | -65% (1741, 13%) | -18% (2515, 6%) | -20% (20, 30%) | -30% (84, 36%) |
| sl30_tp50 | -66% (1741, 15%) | -18% (2515, 6%) | -26% (20, 25%) | -29% (84, 36%) |
| sl50_tp50 | -66% (1741, 16%) | -18% (2515, 7%) | -30% (20, 30%) | -31% (84, 36%) |
| no_stop_tp100 | -65% (1741, 14%) | -18% (2515, 6%) | -17% (20, 30%) | -30% (84, 36%) |

Verdict: NOT ENOUGH DATA (need 30+ closed filter=1 trades and a CI above zero before believing anything).

Pools seen: 62797. Outcomes:

- missed_window: 41453
- low_liquidity: 10121
- proven_liquidity_gone: 4855
- no_momentum: 2565
- research_failed: 1757
- proven_low_volume: 980
- simulated failed buy: 799
- proven_price_collapsed_or_parabolic: 108
- proven: 85
- proven_no_uptrend: 37
- dip: 21
- research_passed: 16

Warning: 536 judged pools had an unreadable mint/freeze value. Check mint_raw / freeze_raw in candidates.csv; the parsing may need fixing.
