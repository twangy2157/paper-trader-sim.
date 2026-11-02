# Paper trader summary

SIMULATION ONLY. No real trades.

Updated 2026-11-02T16:20:53Z. Bankroll cash (research-selected trades): 898.5. Open positions: 20. Pools on watchlist: 52.

| group | n | win | avg | CI | P&L $ |
|---|---|---|---|---|---|
| research-picked | 1 | 0% | -101.0% | - | -102 |
| momentum, not picked | 150 | 15% | -51.7% | -61 to -42 | -7763 |
| all momentum | 151 | 15% | -52.0% | -62 to -42 | -7865 |
| control | 130 | 11% | -15.3% | -22 to -9 | -2003 |
| dip buy | 0 | - | - | - | 0 |
| proven pools | 0 | - | - | - | 0 |

What-if exit rules on the SAME trades. Cells: avg return (trades, win rate).

| exit rule | momentum | control | dip | proven |
|---|---|---|---|---|
| base_sl30_tp100 | -54% (130, 16%) | -15% (130, 11%) | - | - |
| wide_sl50_tp100 | -55% (130, 18%) | -16% (130, 11%) | - | - |
| sl30_tp50 | -55% (130, 20%) | -17% (130, 12%) | - | - |
| sl50_tp50 | -55% (130, 22%) | -17% (130, 12%) | - | - |
| no_stop_tp100 | -56% (130, 18%) | -17% (130, 11%) | - | - |

Verdict: NOT ENOUGH DATA (need 30+ closed filter=1 trades and a CI above zero before believing anything).

Pools seen: 5595. Outcomes:

- missed_window: 3682
- low_liquidity: 1461
- no_momentum: 184
- research_failed: 160
- proven_liquidity_gone: 52
- simulated failed buy: 49
- proven_low_volume: 6
- research_passed: 1

Warning: 31 judged pools had an unreadable mint/freeze value. Check mint_raw / freeze_raw in candidates.csv; the parsing may need fixing.
