# Paper trader summary

SIMULATION ONLY. No real trades.

Updated 2026-11-02T06:50:45Z. Bankroll cash (research-selected trades): 898.5. Open positions: 27. Pools on watchlist: 57.

| group | n | win | avg | CI | P&L $ |
|---|---|---|---|---|---|
| research-picked | 1 | 0% | -101.0% | - | -102 |
| momentum, not picked | 116 | 15% | -47.2% | -58 to -36 | -5489 |
| all momentum | 117 | 15% | -47.7% | -59 to -37 | -5591 |
| control | 87 | 10% | -16.7% | -26 to -8 | -1463 |

What-if exit rules on the SAME trades. Cells: avg return (trades, win rate).

| exit rule | momentum | control |
|---|---|---|
| base_sl30_tp100 | -50% (96, 17%) | -17% (87, 10%) |
| wide_sl50_tp100 | -52% (96, 18%) | -17% (87, 10%) |
| sl30_tp50 | -52% (96, 20%) | -20% (87, 10%) |
| sl50_tp50 | -52% (96, 22%) | -19% (87, 11%) |
| no_stop_tp100 | -52% (96, 18%) | -18% (87, 10%) |

Verdict: NOT ENOUGH DATA (need 30+ closed filter=1 trades and a CI above zero before believing anything).

Pools seen: 4456. Outcomes:

- missed_window: 2900
- low_liquidity: 1241
- no_momentum: 147
- research_failed: 127
- simulated failed buy: 40
- research_passed: 1

Warning: 28 judged pools had an unreadable mint/freeze value. Check mint_raw / freeze_raw in candidates.csv; the parsing may need fixing.
