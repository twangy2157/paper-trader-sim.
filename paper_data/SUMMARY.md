# Paper trader summary

SIMULATION ONLY. No real trades.

Updated 2026-11-05T11:05:10Z. Bankroll cash (research-selected trades): 651.1520680225926. Open positions: 19. Pools on watchlist: 40.

| group | n | win | avg | CI | P&L $ |
|---|---|---|---|---|---|
| research-picked | 6 | 17% | -41.1% | -82 to 7 | -249 |
| momentum, not picked | 640 | 15% | -55.1% | -60 to -50 | -35295 |
| all momentum | 646 | 15% | -54.9% | -60 to -50 | -35543 |
| control | 771 | 7% | -18.9% | -22 to -16 | -14635 |
| dip buy | 5 | 20% | -30.5% | - | -152 |
| proven pools | 37 | 41% | -18.9% | -36 to -2 | -701 |

What-if exit rules on the SAME trades. Cells: avg return (trades, win rate).

| exit rule | momentum | control | dip | proven |
|---|---|---|---|---|
| base_sl30_tp100 | -56% (625, 16%) | -19% (771, 7%) | -30% (5, 20%) | -19% (37, 41%) |
| wide_sl50_tp100 | -56% (625, 17%) | -19% (771, 8%) | -30% (5, 20%) | -19% (37, 41%) |
| sl30_tp50 | -57% (625, 19%) | -19% (771, 8%) | -37% (5, 20%) | -21% (37, 41%) |
| sl50_tp50 | -56% (625, 21%) | -19% (771, 9%) | -37% (5, 20%) | -21% (37, 41%) |
| no_stop_tp100 | -55% (625, 18%) | -20% (771, 8%) | -30% (5, 20%) | -19% (37, 41%) |

Verdict: NOT ENOUGH DATA (need 30+ closed filter=1 trades and a CI above zero before believing anything).

Pools seen: 22880. Outcomes:

- missed_window: 14944
- low_liquidity: 4234
- proven_liquidity_gone: 1625
- no_momentum: 824
- research_failed: 647
- simulated failed buy: 260
- proven_low_volume: 227
- proven_price_collapsed_or_parabolic: 48
- proven: 38
- proven_no_uptrend: 20
- research_passed: 7
- dip: 6

Warning: 170 judged pools had an unreadable mint/freeze value. Check mint_raw / freeze_raw in candidates.csv; the parsing may need fixing.
