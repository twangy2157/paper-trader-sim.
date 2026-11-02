# Paper trader summary

SIMULATION ONLY. No real trades.

Updated 2026-11-02T07:13:29Z. Bankroll cash (research-selected trades): 898.5. Open positions: 22. Pools on watchlist: 53.

| group | n | win | avg | CI | P&L $ |
|---|---|---|---|---|---|
| research-picked | 1 | 0% | -101.0% | - | -102 |
| momentum, not picked | 120 | 15% | -47.5% | -58 to -36 | -5711 |
| all momentum | 121 | 15% | -47.9% | -58 to -37 | -5812 |
| control | 94 | 12% | -15.7% | -24 to -7 | -1490 |

What-if exit rules on the SAME trades. Cells: avg return (trades, win rate).

| exit rule | momentum | control |
|---|---|---|
| base_sl30_tp100 | -50% (100, 17%) | -16% (94, 12%) |
| wide_sl50_tp100 | -52% (100, 18%) | -16% (94, 12%) |
| sl30_tp50 | -52% (100, 20%) | -19% (94, 12%) |
| sl50_tp50 | -52% (100, 22%) | -18% (94, 13%) |
| no_stop_tp100 | -52% (100, 18%) | -17% (94, 12%) |

Verdict: NOT ENOUGH DATA (need 30+ closed filter=1 trades and a CI above zero before believing anything).

Pools seen: 4544. Outcomes:

- missed_window: 2958
- low_liquidity: 1264
- no_momentum: 152
- research_failed: 128
- simulated failed buy: 41
- research_passed: 1

Warning: 28 judged pools had an unreadable mint/freeze value. Check mint_raw / freeze_raw in candidates.csv; the parsing may need fixing.
