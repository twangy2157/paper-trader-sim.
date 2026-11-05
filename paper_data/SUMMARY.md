# Paper trader summary

SIMULATION ONLY. No real trades.

Updated 2026-11-05T14:33:36Z. Bankroll cash (research-selected trades): 749.6403049524637. Open positions: 20. Pools on watchlist: 56.

| group | n | win | avg | CI | P&L $ |
|---|---|---|---|---|---|
| research-picked | 8 | 25% | -31.0% | -68 to 8 | -250 |
| momentum, not picked | 662 | 15% | -55.4% | -60 to -50 | -36749 |
| all momentum | 670 | 15% | -55.1% | -60 to -50 | -37000 |
| control | 798 | 7% | -18.7% | -21 to -16 | -14967 |
| dip buy | 7 | 14% | -27.3% | -65 to 10 | -191 |
| proven pools | 38 | 42% | -17.9% | -34 to -2 | -681 |

What-if exit rules on the SAME trades. Cells: avg return (trades, win rate).

| exit rule | momentum | control | dip | proven |
|---|---|---|---|---|
| base_sl30_tp100 | -56% (649, 15%) | -19% (798, 7%) | -27% (7, 14%) | -18% (38, 42%) |
| wide_sl50_tp100 | -55% (649, 17%) | -19% (798, 8%) | -32% (7, 14%) | -18% (38, 42%) |
| sl30_tp50 | -57% (649, 19%) | -19% (798, 8%) | -32% (7, 14%) | -20% (38, 42%) |
| sl50_tp50 | -56% (649, 21%) | -19% (798, 9%) | -36% (7, 14%) | -20% (38, 42%) |
| no_stop_tp100 | -55% (649, 18%) | -19% (798, 8%) | -27% (7, 14%) | -18% (38, 42%) |

Verdict: NOT ENOUGH DATA (need 30+ closed filter=1 trades and a CI above zero before believing anything).

Pools seen: 23809. Outcomes:

- missed_window: 15527
- low_liquidity: 4406
- proven_liquidity_gone: 1724
- no_momentum: 851
- research_failed: 673
- simulated failed buy: 269
- proven_low_volume: 237
- proven_price_collapsed_or_parabolic: 48
- proven: 38
- proven_no_uptrend: 21
- research_passed: 8
- dip: 7

Warning: 175 judged pools had an unreadable mint/freeze value. Check mint_raw / freeze_raw in candidates.csv; the parsing may need fixing.
