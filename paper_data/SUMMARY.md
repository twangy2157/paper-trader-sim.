# Paper trader summary

SIMULATION ONLY. No real trades.

Updated 2026-11-02T05:24:45Z. Bankroll cash (research-selected trades): 899.0. Open positions: 25. Pools on watchlist: 76.

| group | n | win | avg | CI | P&L $ |
|---|---|---|---|---|---|
| research-picked | 1 | 0% | -101.0% | - | -101 |
| momentum, not picked | 102 | 15% | -47.0% | -58 to -35 | -4804 |
| all momentum | 103 | 15% | -47.6% | -59 to -35 | -4905 |
| control | 69 | 12% | -13.8% | -24 to -4 | -965 |

What-if exit rules on the SAME trades. Cells: avg return (trades, win rate).

| exit rule | momentum | control |
|---|---|---|
| base_sl30_tp100 | -50% (82, 17%) | -14% (69, 12%) |
| wide_sl50_tp100 | -52% (82, 18%) | -15% (69, 12%) |
| sl30_tp50 | -52% (82, 21%) | -17% (69, 12%) |
| sl50_tp50 | -52% (82, 23%) | -17% (69, 13%) |
| no_stop_tp100 | -52% (82, 18%) | -15% (69, 12%) |

Verdict: NOT ENOUGH DATA (need 30+ closed filter=1 trades and a CI above zero before believing anything).

Pools seen: 4108. Outcomes:

- missed_window: 2680
- low_liquidity: 1154
- no_momentum: 128
- research_failed: 112
- simulated failed buy: 33
- research_passed: 1

Warning: 24 judged pools had an unreadable mint/freeze value. Check mint_raw / freeze_raw in candidates.csv; the parsing may need fixing.
