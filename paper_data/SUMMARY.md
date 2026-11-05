# Paper trader summary

SIMULATION ONLY. No real trades.

Updated 2026-11-05T20:58:13Z. Bankroll cash (research-selected trades): 749.6403049524637. Open positions: 20. Pools on watchlist: 66.

| group | n | win | avg | CI | P&L $ |
|---|---|---|---|---|---|
| research-picked | 8 | 25% | -31.0% | -68 to 8 | -250 |
| momentum, not picked | 719 | 14% | -57.4% | -62 to -53 | -41350 |
| all momentum | 727 | 14% | -57.1% | -62 to -53 | -41601 |
| control | 863 | 7% | -19.3% | -22 to -17 | -16712 |
| dip buy | 7 | 14% | -27.3% | -65 to 10 | -191 |
| proven pools | 39 | 44% | -15.7% | -33 to 0 | -615 |

What-if exit rules on the SAME trades. Cells: avg return (trades, win rate).

| exit rule | momentum | control | dip | proven |
|---|---|---|---|---|
| base_sl30_tp100 | -58% (706, 15%) | -19% (863, 7%) | -27% (7, 14%) | -16% (39, 44%) |
| wide_sl50_tp100 | -57% (706, 16%) | -20% (863, 8%) | -32% (7, 14%) | -16% (39, 44%) |
| sl30_tp50 | -59% (706, 18%) | -20% (863, 8%) | -32% (7, 14%) | -18% (39, 44%) |
| sl50_tp50 | -58% (706, 20%) | -20% (863, 9%) | -36% (7, 14%) | -18% (39, 44%) |
| no_stop_tp100 | -57% (706, 17%) | -20% (863, 8%) | -27% (7, 14%) | -16% (39, 44%) |

Verdict: NOT ENOUGH DATA (need 30+ closed filter=1 trades and a CI above zero before believing anything).

Pools seen: 25620. Outcomes:

- missed_window: 16738
- low_liquidity: 4687
- proven_liquidity_gone: 1882
- no_momentum: 916
- research_failed: 729
- simulated failed buy: 289
- proven_low_volume: 253
- proven_price_collapsed_or_parabolic: 49
- proven: 40
- proven_no_uptrend: 22
- research_passed: 8
- dip: 7

Warning: 188 judged pools had an unreadable mint/freeze value. Check mint_raw / freeze_raw in candidates.csv; the parsing may need fixing.
