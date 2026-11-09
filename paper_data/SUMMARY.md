# Paper trader summary

SIMULATION ONLY. No real trades.

Updated 2026-11-09T15:00:42Z. Bankroll cash (research-selected trades): 456.400154541351. Open positions: 27. Pools on watchlist: 81.

| group | n | win | avg | CI | P&L $ |
|---|---|---|---|---|---|
| research-picked | 16 | 25% | -33.9% | -64 to -3 | -544 |
| momentum, not picked | 1335 | 13% | -63.2% | -66 to -60 | -84476 |
| all momentum | 1351 | 13% | -62.8% | -66 to -60 | -85019 |
| control | 1861 | 5% | -18.7% | -20 to -17 | -35020 |
| dip buy | 13 | 8% | -38.7% | -63 to -14 | -504 |
| proven pools | 65 | 43% | -19.4% | -31 to -7 | -1266 |

What-if exit rules on the SAME trades. Cells: avg return (trades, win rate).

| exit rule | momentum | control | dip | proven |
|---|---|---|---|---|
| base_sl30_tp100 | -63% (1330, 13%) | -19% (1861, 5%) | -39% (13, 8%) | -19% (65, 43%) |
| wide_sl50_tp100 | -63% (1330, 15%) | -19% (1861, 6%) | -45% (13, 8%) | -20% (65, 43%) |
| sl30_tp50 | -64% (1330, 16%) | -19% (1861, 6%) | -41% (13, 8%) | -21% (65, 43%) |
| sl50_tp50 | -64% (1330, 18%) | -19% (1861, 7%) | -48% (13, 8%) | -21% (65, 43%) |
| no_stop_tp100 | -63% (1330, 15%) | -19% (1861, 6%) | -43% (13, 8%) | -20% (65, 43%) |

Verdict: NOT ENOUGH DATA (need 30+ closed filter=1 trades and a CI above zero before believing anything).

Pools seen: 49819. Outcomes:

- missed_window: 33102
- low_liquidity: 8140
- proven_liquidity_gone: 3779
- no_momentum: 1913
- research_failed: 1345
- proven_low_volume: 718
- simulated failed buy: 606
- proven_price_collapsed_or_parabolic: 83
- proven: 74
- proven_no_uptrend: 30
- research_passed: 16
- dip: 13

Warning: 403 judged pools had an unreadable mint/freeze value. Check mint_raw / freeze_raw in candidates.csv; the parsing may need fixing.
