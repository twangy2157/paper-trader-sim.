# Paper trader summary

SIMULATION ONLY. No real trades.

Updated 2026-11-04T17:19:08Z. Bankroll cash (research-selected trades): 913.731903378573. Open positions: 40. Pools on watchlist: 48.

| group | n | win | avg | CI | P&L $ |
|---|---|---|---|---|---|
| research-picked | 4 | 25% | -21.2% | - | -86 |
| momentum, not picked | 502 | 15% | -53.7% | -59 to -48 | -27012 |
| all momentum | 506 | 15% | -53.5% | -59 to -48 | -27098 |
| control | 604 | 7% | -18.8% | -22 to -16 | -11443 |
| dip buy | 4 | 25% | -13.1% | - | -52 |
| proven pools | 27 | 41% | -15.9% | -35 to 2 | -431 |

What-if exit rules on the SAME trades. Cells: avg return (trades, win rate).

| exit rule | momentum | control | dip | proven |
|---|---|---|---|---|
| base_sl30_tp100 | -54% (485, 16%) | -19% (604, 7%) | -13% (4, 25%) | -16% (27, 41%) |
| wide_sl50_tp100 | -54% (485, 18%) | -19% (604, 7%) | -13% (4, 25%) | -16% (27, 41%) |
| sl30_tp50 | -56% (485, 19%) | -19% (604, 8%) | -22% (4, 25%) | -18% (27, 41%) |
| sl50_tp50 | -55% (485, 22%) | -19% (604, 9%) | -22% (4, 25%) | -18% (27, 41%) |
| no_stop_tp100 | -53% (485, 19%) | -20% (604, 7%) | -13% (4, 25%) | -16% (27, 41%) |

Verdict: NOT ENOUGH DATA (need 30+ closed filter=1 trades and a CI above zero before believing anything).

Pools seen: 18771. Outcomes:

- missed_window: 12415
- low_liquidity: 3487
- proven_liquidity_gone: 1205
- no_momentum: 670
- research_failed: 518
- simulated failed buy: 214
- proven_low_volume: 175
- proven_price_collapsed_or_parabolic: 35
- proven: 29
- proven_no_uptrend: 15
- research_passed: 4
- dip: 4

Warning: 145 judged pools had an unreadable mint/freeze value. Check mint_raw / freeze_raw in candidates.csv; the parsing may need fixing.
