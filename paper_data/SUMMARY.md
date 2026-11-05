# Paper trader summary

SIMULATION ONLY. No real trades.

Updated 2026-11-05T16:40:20Z. Bankroll cash (research-selected trades): 749.6403049524637. Open positions: 23. Pools on watchlist: 38.

| group | n | win | avg | CI | P&L $ |
|---|---|---|---|---|---|
| research-picked | 8 | 25% | -31.0% | -68 to 8 | -250 |
| momentum, not picked | 683 | 14% | -56.5% | -61 to -52 | -38626 |
| all momentum | 691 | 15% | -56.2% | -60 to -52 | -38876 |
| control | 817 | 7% | -18.7% | -21 to -16 | -15353 |
| dip buy | 7 | 14% | -27.3% | -65 to 10 | -191 |
| proven pools | 38 | 42% | -17.9% | -34 to -2 | -681 |

What-if exit rules on the SAME trades. Cells: avg return (trades, win rate).

| exit rule | momentum | control | dip | proven |
|---|---|---|---|---|
| base_sl30_tp100 | -57% (670, 15%) | -19% (817, 7%) | -27% (7, 14%) | -18% (38, 42%) |
| wide_sl50_tp100 | -57% (670, 17%) | -19% (817, 8%) | -32% (7, 14%) | -18% (38, 42%) |
| sl30_tp50 | -58% (670, 19%) | -19% (817, 8%) | -32% (7, 14%) | -20% (38, 42%) |
| sl50_tp50 | -57% (670, 21%) | -19% (817, 9%) | -36% (7, 14%) | -20% (38, 42%) |
| no_stop_tp100 | -56% (670, 18%) | -19% (817, 8%) | -27% (7, 14%) | -18% (38, 42%) |

Verdict: NOT ENOUGH DATA (need 30+ closed filter=1 trades and a CI above zero before believing anything).

Pools seen: 24459. Outcomes:

- missed_window: 15976
- low_liquidity: 4493
- proven_liquidity_gone: 1778
- no_momentum: 878
- research_failed: 689
- simulated failed buy: 280
- proven_low_volume: 242
- proven_price_collapsed_or_parabolic: 48
- proven: 38
- proven_no_uptrend: 22
- research_passed: 8
- dip: 7

Warning: 182 judged pools had an unreadable mint/freeze value. Check mint_raw / freeze_raw in candidates.csv; the parsing may need fixing.
