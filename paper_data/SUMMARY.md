# Paper trader summary

SIMULATION ONLY. No real trades.

Updated 2026-11-05T20:47:57Z. Bankroll cash (research-selected trades): 749.6403049524637. Open positions: 20. Pools on watchlist: 67.

| group | n | win | avg | CI | P&L $ |
|---|---|---|---|---|---|
| research-picked | 8 | 25% | -31.0% | -68 to 8 | -250 |
| momentum, not picked | 717 | 14% | -57.3% | -62 to -53 | -41150 |
| all momentum | 725 | 14% | -57.0% | -61 to -53 | -41401 |
| control | 862 | 7% | -19.3% | -22 to -17 | -16708 |
| dip buy | 7 | 14% | -27.3% | -65 to 10 | -191 |
| proven pools | 38 | 42% | -17.9% | -34 to -2 | -681 |

What-if exit rules on the SAME trades. Cells: avg return (trades, win rate).

| exit rule | momentum | control | dip | proven |
|---|---|---|---|---|
| base_sl30_tp100 | -58% (704, 15%) | -19% (862, 7%) | -27% (7, 14%) | -18% (38, 42%) |
| wide_sl50_tp100 | -57% (704, 16%) | -20% (862, 8%) | -32% (7, 14%) | -18% (38, 42%) |
| sl30_tp50 | -59% (704, 18%) | -20% (862, 8%) | -32% (7, 14%) | -20% (38, 42%) |
| sl50_tp50 | -58% (704, 20%) | -20% (862, 9%) | -36% (7, 14%) | -20% (38, 42%) |
| no_stop_tp100 | -57% (704, 17%) | -20% (862, 8%) | -27% (7, 14%) | -18% (38, 42%) |

Verdict: NOT ENOUGH DATA (need 30+ closed filter=1 trades and a CI above zero before believing anything).

Pools seen: 25570. Outcomes:

- missed_window: 16705
- low_liquidity: 4678
- proven_liquidity_gone: 1879
- no_momentum: 914
- research_failed: 727
- simulated failed buy: 289
- proven_low_volume: 252
- proven_price_collapsed_or_parabolic: 49
- proven: 40
- proven_no_uptrend: 22
- research_passed: 8
- dip: 7

Warning: 188 judged pools had an unreadable mint/freeze value. Check mint_raw / freeze_raw in candidates.csv; the parsing may need fixing.
