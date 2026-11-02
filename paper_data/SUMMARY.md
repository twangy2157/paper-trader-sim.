# Paper trader summary

SIMULATION ONLY. No real trades.

Updated 2026-11-02T07:02:11Z. Bankroll cash (research-selected trades): 898.5. Open positions: 23. Pools on watchlist: 48.

| group | n | win | avg | CI | P&L $ |
|---|---|---|---|---|---|
| research-picked | 1 | 0% | -101.0% | - | -102 |
| momentum, not picked | 119 | 14% | -48.1% | -59 to -37 | -5738 |
| all momentum | 120 | 14% | -48.6% | -59 to -37 | -5839 |
| control | 91 | 11% | -15.2% | -24 to -6 | -1396 |

What-if exit rules on the SAME trades. Cells: avg return (trades, win rate).

| exit rule | momentum | control |
|---|---|---|
| base_sl30_tp100 | -51% (99, 16%) | -15% (91, 11%) |
| wide_sl50_tp100 | -53% (99, 17%) | -16% (91, 11%) |
| sl30_tp50 | -53% (99, 19%) | -18% (91, 11%) |
| sl50_tp50 | -53% (99, 21%) | -18% (91, 12%) |
| no_stop_tp100 | -53% (99, 17%) | -16% (91, 11%) |

Verdict: NOT ENOUGH DATA (need 30+ closed filter=1 trades and a CI above zero before believing anything).

Pools seen: 4499. Outcomes:

- missed_window: 2931
- low_liquidity: 1249
- no_momentum: 150
- research_failed: 127
- simulated failed buy: 41
- research_passed: 1

Warning: 28 judged pools had an unreadable mint/freeze value. Check mint_raw / freeze_raw in candidates.csv; the parsing may need fixing.
