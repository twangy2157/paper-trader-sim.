# Paper trader summary

SIMULATION ONLY. No real trades.

Updated 2026-11-07T23:14:11Z. Bankroll cash (research-selected trades): 499.4001435479087. Open positions: 24. Pools on watchlist: 63.

| group | n | win | avg | CI | P&L $ |
|---|---|---|---|---|---|
| research-picked | 14 | 21% | -35.6% | -66 to -4 | -501 |
| momentum, not picked | 1061 | 13% | -61.4% | -65 to -58 | -65222 |
| all momentum | 1075 | 13% | -61.0% | -65 to -58 | -65723 |
| control | 1395 | 6% | -19.7% | -21 to -18 | -27541 |
| dip buy | 11 | 9% | -40.6% | -69 to -11 | -447 |
| proven pools | 54 | 48% | -15.1% | -29 to -3 | -820 |

What-if exit rules on the SAME trades. Cells: avg return (trades, win rate).

| exit rule | momentum | control | dip | proven |
|---|---|---|---|---|
| base_sl30_tp100 | -62% (1054, 13%) | -20% (1395, 6%) | -41% (11, 9%) | -15% (54, 48%) |
| wide_sl50_tp100 | -61% (1054, 15%) | -20% (1395, 6%) | -48% (11, 9%) | -15% (54, 48%) |
| sl30_tp50 | -63% (1054, 16%) | -20% (1395, 7%) | -44% (11, 9%) | -17% (54, 48%) |
| sl50_tp50 | -62% (1054, 18%) | -20% (1395, 7%) | -52% (11, 9%) | -17% (54, 48%) |
| no_stop_tp100 | -61% (1054, 16%) | -20% (1395, 6%) | -45% (11, 9%) | -15% (54, 48%) |

Verdict: NOT ENOUGH DATA (need 30+ closed filter=1 trades and a CI above zero before believing anything).

Pools seen: 38124. Outcomes:

- missed_window: 24848
- low_liquidity: 6716
- proven_liquidity_gone: 2958
- no_momentum: 1457
- research_failed: 1066
- simulated failed buy: 467
- proven_low_volume: 443
- proven_price_collapsed_or_parabolic: 65
- proven: 55
- proven_no_uptrend: 24
- research_passed: 14
- dip: 11

Warning: 295 judged pools had an unreadable mint/freeze value. Check mint_raw / freeze_raw in candidates.csv; the parsing may need fixing.
