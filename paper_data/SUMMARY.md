# Paper trader summary

SIMULATION ONLY. No real trades.

Updated 2026-11-02T05:56:29Z. Bankroll cash (research-selected trades): 898.5. Open positions: 27. Pools on watchlist: 56.

| group | n | win | avg | CI | P&L $ |
|---|---|---|---|---|---|
| research-picked | 1 | 0% | -101.0% | - | -102 |
| momentum, not picked | 107 | 15% | -46.7% | -58 to -35 | -5010 |
| all momentum | 108 | 15% | -47.3% | -58 to -36 | -5112 |
| control | 76 | 11% | -17.0% | -27 to -7 | -1301 |

What-if exit rules on the SAME trades. Cells: avg return (trades, win rate).

| exit rule | momentum | control |
|---|---|---|
| base_sl30_tp100 | -50% (87, 17%) | -17% (76, 11%) |
| wide_sl50_tp100 | -51% (87, 18%) | -18% (76, 11%) |
| sl30_tp50 | -52% (87, 21%) | -20% (76, 11%) |
| sl50_tp50 | -52% (87, 23%) | -19% (76, 12%) |
| no_stop_tp100 | -52% (87, 18%) | -18% (76, 11%) |

Verdict: NOT ENOUGH DATA (need 30+ closed filter=1 trades and a CI above zero before believing anything).

Pools seen: 4243. Outcomes:

- missed_window: 2770
- low_liquidity: 1182
- no_momentum: 135
- research_failed: 119
- simulated failed buy: 36
- research_passed: 1

Warning: 26 judged pools had an unreadable mint/freeze value. Check mint_raw / freeze_raw in candidates.csv; the parsing may need fixing.
