# Paper trader summary

SIMULATION ONLY. No real trades.

Updated 2026-11-08T21:16:30Z. Bankroll cash (research-selected trades): 456.400154541351. Open positions: 30. Pools on watchlist: 106.

| group | n | win | avg | CI | P&L $ |
|---|---|---|---|---|---|
| research-picked | 16 | 25% | -33.9% | -64 to -3 | -544 |
| momentum, not picked | 1220 | 12% | -63.5% | -67 to -60 | -77562 |
| all momentum | 1236 | 13% | -63.1% | -67 to -60 | -78105 |
| control | 1635 | 6% | -19.0% | -21 to -17 | -31136 |
| dip buy | 12 | 8% | -39.5% | -67 to -12 | -474 |
| proven pools | 57 | 46% | -16.2% | -30 to -4 | -932 |

What-if exit rules on the SAME trades. Cells: avg return (trades, win rate).

| exit rule | momentum | control | dip | proven |
|---|---|---|---|---|
| base_sl30_tp100 | -64% (1215, 13%) | -19% (1635, 6%) | -39% (12, 8%) | -16% (57, 46%) |
| wide_sl50_tp100 | -63% (1215, 14%) | -19% (1635, 6%) | -47% (12, 8%) | -16% (57, 46%) |
| sl30_tp50 | -64% (1215, 16%) | -19% (1635, 6%) | -42% (12, 8%) | -18% (57, 46%) |
| sl50_tp50 | -64% (1215, 17%) | -19% (1635, 7%) | -49% (12, 8%) | -18% (57, 46%) |
| no_stop_tp100 | -63% (1215, 15%) | -20% (1635, 6%) | -44% (12, 8%) | -16% (57, 46%) |

Verdict: NOT ENOUGH DATA (need 30+ closed filter=1 trades and a CI above zero before believing anything).

Pools seen: 44521. Outcomes:

- missed_window: 29298
- low_liquidity: 7549
- proven_liquidity_gone: 3419
- no_momentum: 1698
- research_failed: 1229
- proven_low_volume: 600
- simulated failed buy: 539
- proven_price_collapsed_or_parabolic: 76
- proven: 59
- proven_no_uptrend: 26
- research_passed: 16
- dip: 12

Warning: 349 judged pools had an unreadable mint/freeze value. Check mint_raw / freeze_raw in candidates.csv; the parsing may need fixing.
