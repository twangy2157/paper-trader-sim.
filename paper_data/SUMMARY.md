# Paper trader summary

SIMULATION ONLY. No real trades.

Updated 2026-11-02T03:19:29Z. Bankroll cash (research-selected trades): 899.0. Open positions: 35. Pools on watchlist: 59.

| group | n | win | avg | CI | P&L $ |
|---|---|---|---|---|---|
| research-picked | 1 | 0% | -101.0% | - | -101 |
| momentum, not picked | 69 | 14% | -40.0% | -55 to -24 | -2770 |
| all momentum | 70 | 14% | -40.9% | -55 to -26 | -2871 |
| control | 48 | 10% | -9.2% | -20 to 1 | -447 |

What-if exit rules on the SAME trades. Cells: avg return (trades, win rate).

| exit rule | momentum | control |
|---|---|---|
| base_sl30_tp100 | -43% (49, 18%) | -9% (48, 10%) |
| wide_sl50_tp100 | -42% (49, 20%) | -11% (48, 10%) |
| sl30_tp50 | -47% (49, 20%) | -13% (48, 10%) |
| sl50_tp50 | -47% (49, 22%) | -11% (48, 12%) |
| no_stop_tp100 | -42% (49, 20%) | -11% (48, 10%) |

Verdict: NOT ENOUGH DATA (need 30+ closed filter=1 trades and a CI above zero before believing anything).

Pools seen: 3664. Outcomes:

- missed_window: 2409
- low_liquidity: 1035
- no_momentum: 109
- research_failed: 87
- simulated failed buy: 23
- research_passed: 1

Warning: 14 judged pools had an unreadable mint/freeze value. Check mint_raw / freeze_raw in candidates.csv; the parsing may need fixing.
