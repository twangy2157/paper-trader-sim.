# Paper trader summary

SIMULATION ONLY. No real trades.

Updated 2026-11-02T17:55:20Z. Bankroll cash (research-selected trades): 898.5. Open positions: 18. Pools on watchlist: 108.

| group | n | win | avg | CI | P&L $ |
|---|---|---|---|---|---|
| research-picked | 1 | 0% | -101.0% | - | -102 |
| momentum, not picked | 169 | 15% | -52.6% | -62 to -43 | -8899 |
| all momentum | 170 | 15% | -52.9% | -62 to -43 | -9001 |
| control | 142 | 11% | -15.7% | -22 to -9 | -2248 |
| dip buy | 0 | - | - | - | 0 |
| proven pools | 0 | - | - | - | 0 |

What-if exit rules on the SAME trades. Cells: avg return (trades, win rate).

| exit rule | momentum | control | dip | proven |
|---|---|---|---|---|
| base_sl30_tp100 | -55% (149, 16%) | -16% (142, 11%) | - | - |
| wide_sl50_tp100 | -56% (149, 17%) | -17% (142, 11%) | - | - |
| sl30_tp50 | -56% (149, 19%) | -18% (142, 12%) | - | - |
| sl50_tp50 | -56% (149, 21%) | -18% (142, 13%) | - | - |
| no_stop_tp100 | -55% (149, 18%) | -17% (142, 11%) | - | - |

Verdict: NOT ENOUGH DATA (need 30+ closed filter=1 trades and a CI above zero before believing anything).

Pools seen: 6034. Outcomes:

- missed_window: 3970
- low_liquidity: 1537
- no_momentum: 198
- research_failed: 174
- proven_liquidity_gone: 89
- simulated failed buy: 57
- proven_low_volume: 6
- research_passed: 1
- proven: 1
- proven_no_uptrend: 1

Warning: 36 judged pools had an unreadable mint/freeze value. Check mint_raw / freeze_raw in candidates.csv; the parsing may need fixing.
