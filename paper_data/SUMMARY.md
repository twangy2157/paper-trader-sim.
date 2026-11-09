# Paper trader summary

SIMULATION ONLY. No real trades.

Updated 2026-11-09T00:17:32Z. Bankroll cash (research-selected trades): 456.400154541351. Open positions: 19. Pools on watchlist: 101.

| group | n | win | avg | CI | P&L $ |
|---|---|---|---|---|---|
| research-picked | 16 | 25% | -33.9% | -64 to -3 | -544 |
| momentum, not picked | 1238 | 12% | -63.8% | -67 to -60 | -79137 |
| all momentum | 1254 | 12% | -63.5% | -67 to -60 | -79681 |
| control | 1698 | 5% | -18.6% | -20 to -17 | -31696 |
| dip buy | 12 | 8% | -39.5% | -67 to -12 | -474 |
| proven pools | 59 | 44% | -17.4% | -30 to -5 | -1035 |

What-if exit rules on the SAME trades. Cells: avg return (trades, win rate).

| exit rule | momentum | control | dip | proven |
|---|---|---|---|---|
| base_sl30_tp100 | -64% (1233, 13%) | -19% (1698, 5%) | -39% (12, 8%) | -17% (59, 44%) |
| wide_sl50_tp100 | -64% (1233, 14%) | -19% (1698, 6%) | -47% (12, 8%) | -17% (59, 44%) |
| sl30_tp50 | -65% (1233, 15%) | -19% (1698, 6%) | -42% (12, 8%) | -19% (59, 44%) |
| sl50_tp50 | -64% (1233, 17%) | -19% (1698, 6%) | -49% (12, 8%) | -19% (59, 44%) |
| no_stop_tp100 | -64% (1233, 15%) | -19% (1698, 6%) | -44% (12, 8%) | -17% (59, 44%) |

Verdict: NOT ENOUGH DATA (need 30+ closed filter=1 trades and a CI above zero before believing anything).

Pools seen: 45765. Outcomes:

- missed_window: 30290
- low_liquidity: 7626
- proven_liquidity_gone: 3478
- no_momentum: 1754
- research_failed: 1244
- proven_low_volume: 633
- simulated failed buy: 550
- proven_price_collapsed_or_parabolic: 76
- proven: 60
- proven_no_uptrend: 26
- research_passed: 16
- dip: 12

Warning: 359 judged pools had an unreadable mint/freeze value. Check mint_raw / freeze_raw in candidates.csv; the parsing may need fixing.
