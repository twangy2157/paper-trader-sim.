# Paper trader summary

SIMULATION ONLY. No real trades.

Updated 2026-11-02T07:14:45Z. Bankroll cash (research-selected trades): 898.5. Open positions: 21. Pools on watchlist: 54.

| group | n | win | avg | CI | P&L $ |
|---|---|---|---|---|---|
| research-picked | 1 | 0% | -101.0% | - | -102 |
| momentum, not picked | 121 | 15% | -47.9% | -59 to -37 | -5811 |
| all momentum | 122 | 15% | -48.4% | -59 to -38 | -5912 |
| control | 94 | 12% | -15.7% | -24 to -7 | -1490 |

What-if exit rules on the SAME trades. Cells: avg return (trades, win rate).

| exit rule | momentum | control |
|---|---|---|
| base_sl30_tp100 | -51% (101, 17%) | -16% (94, 12%) |
| wide_sl50_tp100 | -52% (101, 18%) | -16% (94, 12%) |
| sl30_tp50 | -53% (101, 20%) | -19% (94, 12%) |
| sl50_tp50 | -53% (101, 22%) | -18% (94, 13%) |
| no_stop_tp100 | -53% (101, 18%) | -17% (94, 12%) |

Verdict: NOT ENOUGH DATA (need 30+ closed filter=1 trades and a CI above zero before believing anything).

Pools seen: 4547. Outcomes:

- missed_window: 2961
- low_liquidity: 1264
- no_momentum: 152
- research_failed: 128
- simulated failed buy: 41
- research_passed: 1

Warning: 28 judged pools had an unreadable mint/freeze value. Check mint_raw / freeze_raw in candidates.csv; the parsing may need fixing.
