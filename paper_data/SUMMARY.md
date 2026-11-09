# Paper trader summary

SIMULATION ONLY. No real trades.

Updated 2026-11-09T16:46:41Z. Bankroll cash (research-selected trades): 456.400154541351. Open positions: 31. Pools on watchlist: 84.

| group | n | win | avg | CI | P&L $ |
|---|---|---|---|---|---|
| research-picked | 16 | 25% | -33.9% | -64 to -3 | -544 |
| momentum, not picked | 1350 | 13% | -63.5% | -67 to -60 | -85912 |
| all momentum | 1366 | 13% | -63.2% | -66 to -60 | -86456 |
| control | 1887 | 6% | -18.7% | -20 to -17 | -35548 |
| dip buy | 13 | 8% | -38.7% | -63 to -14 | -504 |
| proven pools | 66 | 42% | -20.6% | -33 to -8 | -1368 |

What-if exit rules on the SAME trades. Cells: avg return (trades, win rate).

| exit rule | momentum | control | dip | proven |
|---|---|---|---|---|
| base_sl30_tp100 | -64% (1345, 13%) | -19% (1887, 6%) | -39% (13, 8%) | -21% (66, 42%) |
| wide_sl50_tp100 | -63% (1345, 14%) | -19% (1887, 6%) | -45% (13, 8%) | -21% (66, 42%) |
| sl30_tp50 | -64% (1345, 16%) | -19% (1887, 6%) | -41% (13, 8%) | -22% (66, 42%) |
| sl50_tp50 | -64% (1345, 17%) | -19% (1887, 7%) | -48% (13, 8%) | -22% (66, 42%) |
| no_stop_tp100 | -63% (1345, 15%) | -19% (1887, 6%) | -43% (13, 8%) | -21% (66, 42%) |

Verdict: NOT ENOUGH DATA (need 30+ closed filter=1 trades and a CI above zero before believing anything).

Pools seen: 50425. Outcomes:

- missed_window: 33554
- low_liquidity: 8184
- proven_liquidity_gone: 3820
- no_momentum: 1950
- research_failed: 1354
- proven_low_volume: 723
- simulated failed buy: 621
- proven_price_collapsed_or_parabolic: 85
- proven: 74
- proven_no_uptrend: 31
- research_passed: 16
- dip: 13

Warning: 416 judged pools had an unreadable mint/freeze value. Check mint_raw / freeze_raw in candidates.csv; the parsing may need fixing.
