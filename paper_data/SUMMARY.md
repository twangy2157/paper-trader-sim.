# Paper trader summary

SIMULATION ONLY. No real trades.

Updated 2026-11-07T23:46:41Z. Bankroll cash (research-selected trades): 499.4001435479087. Open positions: 15. Pools on watchlist: 85.

| group | n | win | avg | CI | P&L $ |
|---|---|---|---|---|---|
| research-picked | 14 | 21% | -35.6% | -66 to -4 | -501 |
| momentum, not picked | 1064 | 13% | -61.5% | -65 to -58 | -65522 |
| all momentum | 1078 | 13% | -61.2% | -65 to -58 | -66023 |
| control | 1408 | 6% | -19.7% | -22 to -18 | -27813 |
| dip buy | 11 | 9% | -40.6% | -69 to -11 | -447 |
| proven pools | 54 | 48% | -15.1% | -29 to -3 | -820 |

What-if exit rules on the SAME trades. Cells: avg return (trades, win rate).

| exit rule | momentum | control | dip | proven |
|---|---|---|---|---|
| base_sl30_tp100 | -62% (1057, 13%) | -20% (1408, 6%) | -41% (11, 9%) | -15% (54, 48%) |
| wide_sl50_tp100 | -62% (1057, 15%) | -20% (1408, 6%) | -48% (11, 9%) | -15% (54, 48%) |
| sl30_tp50 | -63% (1057, 16%) | -20% (1408, 7%) | -44% (11, 9%) | -17% (54, 48%) |
| sl50_tp50 | -62% (1057, 18%) | -20% (1408, 7%) | -52% (11, 9%) | -17% (54, 48%) |
| no_stop_tp100 | -61% (1057, 16%) | -20% (1408, 6%) | -45% (11, 9%) | -15% (54, 48%) |

Verdict: NOT ENOUGH DATA (need 30+ closed filter=1 trades and a CI above zero before believing anything).

Pools seen: 38298. Outcomes:

- missed_window: 24981
- low_liquidity: 6732
- proven_liquidity_gone: 2967
- no_momentum: 1462
- research_failed: 1068
- simulated failed buy: 467
- proven_low_volume: 452
- proven_price_collapsed_or_parabolic: 65
- proven: 55
- proven_no_uptrend: 24
- research_passed: 14
- dip: 11

Warning: 295 judged pools had an unreadable mint/freeze value. Check mint_raw / freeze_raw in candidates.csv; the parsing may need fixing.
