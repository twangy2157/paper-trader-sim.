# Paper trader summary

SIMULATION ONLY. No real trades.

Updated 2026-11-02T06:19:08Z. Bankroll cash (research-selected trades): 898.5. Open positions: 24. Pools on watchlist: 59.

| group | n | win | avg | CI | P&L $ |
|---|---|---|---|---|---|
| research-picked | 1 | 0% | -101.0% | - | -102 |
| momentum, not picked | 111 | 14% | -48.2% | -59 to -36 | -5359 |
| all momentum | 112 | 14% | -48.7% | -59 to -38 | -5461 |
| control | 82 | 11% | -17.2% | -26 to -8 | -1422 |

What-if exit rules on the SAME trades. Cells: avg return (trades, win rate).

| exit rule | momentum | control |
|---|---|---|
| base_sl30_tp100 | -51% (91, 16%) | -17% (82, 11%) |
| wide_sl50_tp100 | -53% (91, 18%) | -18% (82, 11%) |
| sl30_tp50 | -53% (91, 20%) | -20% (82, 11%) |
| sl50_tp50 | -53% (91, 22%) | -19% (82, 12%) |
| no_stop_tp100 | -54% (91, 18%) | -18% (82, 11%) |

Verdict: NOT ENOUGH DATA (need 30+ closed filter=1 trades and a CI above zero before believing anything).

Pools seen: 4332. Outcomes:

- missed_window: 2828
- low_liquidity: 1204
- no_momentum: 138
- research_failed: 123
- simulated failed buy: 38
- research_passed: 1

Warning: 27 judged pools had an unreadable mint/freeze value. Check mint_raw / freeze_raw in candidates.csv; the parsing may need fixing.
