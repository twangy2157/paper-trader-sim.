# Paper trader summary

SIMULATION ONLY. No real trades.

Updated 2026-11-02T04:01:29Z. Bankroll cash (research-selected trades): 899.0. Open positions: 19. Pools on watchlist: 53.

| group | n | win | avg | CI | P&L $ |
|---|---|---|---|---|---|
| research-picked | 1 | 0% | -101.0% | - | -101 |
| momentum, not picked | 84 | 13% | -46.1% | -59 to -33 | -3875 |
| all momentum | 85 | 13% | -46.7% | -60 to -33 | -3976 |
| control | 60 | 13% | -10.4% | -21 to 0 | -632 |

What-if exit rules on the SAME trades. Cells: avg return (trades, win rate).

| exit rule | momentum | control |
|---|---|---|
| base_sl30_tp100 | -50% (64, 16%) | -10% (60, 13%) |
| wide_sl50_tp100 | -50% (64, 17%) | -12% (60, 13%) |
| sl30_tp50 | -52% (64, 19%) | -15% (60, 13%) |
| sl50_tp50 | -53% (64, 20%) | -14% (60, 15%) |
| no_stop_tp100 | -50% (64, 17%) | -12% (60, 13%) |

Verdict: NOT ENOUGH DATA (need 30+ closed filter=1 trades and a CI above zero before believing anything).

Pools seen: 3821. Outcomes:

- missed_window: 2522
- low_liquidity: 1065
- no_momentum: 111
- research_failed: 96
- simulated failed buy: 26
- research_passed: 1

Warning: 17 judged pools had an unreadable mint/freeze value. Check mint_raw / freeze_raw in candidates.csv; the parsing may need fixing.
