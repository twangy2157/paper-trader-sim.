# Paper trader summary

SIMULATION ONLY. No real trades.

Updated 2026-11-05T13:30:45Z. Bankroll cash (research-selected trades): 749.6403049524637. Open positions: 12. Pools on watchlist: 55.

| group | n | win | avg | CI | P&L $ |
|---|---|---|---|---|---|
| research-picked | 8 | 25% | -31.0% | -68 to 8 | -250 |
| momentum, not picked | 656 | 15% | -55.4% | -60 to -51 | -36407 |
| all momentum | 664 | 15% | -55.1% | -60 to -51 | -36658 |
| control | 792 | 7% | -18.9% | -22 to -16 | -15027 |
| dip buy | 7 | 14% | -27.3% | -65 to 10 | -191 |
| proven pools | 38 | 42% | -17.9% | -34 to -2 | -681 |

What-if exit rules on the SAME trades. Cells: avg return (trades, win rate).

| exit rule | momentum | control | dip | proven |
|---|---|---|---|---|
| base_sl30_tp100 | -56% (643, 15%) | -19% (792, 7%) | -27% (7, 14%) | -18% (38, 42%) |
| wide_sl50_tp100 | -56% (643, 17%) | -19% (792, 8%) | -32% (7, 14%) | -18% (38, 42%) |
| sl30_tp50 | -57% (643, 19%) | -19% (792, 8%) | -32% (7, 14%) | -20% (38, 42%) |
| sl50_tp50 | -56% (643, 21%) | -19% (792, 9%) | -36% (7, 14%) | -20% (38, 42%) |
| no_stop_tp100 | -55% (643, 18%) | -20% (792, 8%) | -27% (7, 14%) | -18% (38, 42%) |

Verdict: NOT ENOUGH DATA (need 30+ closed filter=1 trades and a CI above zero before believing anything).

Pools seen: 23443. Outcomes:

- missed_window: 15281
- low_liquidity: 4348
- proven_liquidity_gone: 1688
- no_momentum: 842
- research_failed: 662
- simulated failed buy: 268
- proven_low_volume: 233
- proven_price_collapsed_or_parabolic: 48
- proven: 38
- proven_no_uptrend: 20
- research_passed: 8
- dip: 7

Warning: 174 judged pools had an unreadable mint/freeze value. Check mint_raw / freeze_raw in candidates.csv; the parsing may need fixing.
