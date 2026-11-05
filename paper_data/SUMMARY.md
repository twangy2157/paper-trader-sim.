# Paper trader summary

SIMULATION ONLY. No real trades.

Updated 2026-11-05T19:56:08Z. Bankroll cash (research-selected trades): 749.6403049524637. Open positions: 18. Pools on watchlist: 105.

| group | n | win | avg | CI | P&L $ |
|---|---|---|---|---|---|
| research-picked | 8 | 25% | -31.0% | -68 to 8 | -250 |
| momentum, not picked | 709 | 14% | -56.8% | -61 to -52 | -40350 |
| all momentum | 717 | 15% | -56.5% | -61 to -52 | -40601 |
| control | 857 | 7% | -19.4% | -22 to -17 | -16664 |
| dip buy | 7 | 14% | -27.3% | -65 to 10 | -191 |
| proven pools | 38 | 42% | -17.9% | -34 to -2 | -681 |

What-if exit rules on the SAME trades. Cells: avg return (trades, win rate).

| exit rule | momentum | control | dip | proven |
|---|---|---|---|---|
| base_sl30_tp100 | -57% (696, 15%) | -19% (857, 7%) | -27% (7, 14%) | -18% (38, 42%) |
| wide_sl50_tp100 | -57% (696, 17%) | -20% (857, 7%) | -32% (7, 14%) | -18% (38, 42%) |
| sl30_tp50 | -58% (696, 18%) | -20% (857, 8%) | -32% (7, 14%) | -20% (38, 42%) |
| sl50_tp50 | -58% (696, 20%) | -20% (857, 9%) | -36% (7, 14%) | -20% (38, 42%) |
| no_stop_tp100 | -56% (696, 18%) | -20% (857, 8%) | -27% (7, 14%) | -18% (38, 42%) |

Verdict: NOT ENOUGH DATA (need 30+ closed filter=1 trades and a CI above zero before believing anything).

Pools seen: 25273. Outcomes:

- missed_window: 16502
- low_liquidity: 4624
- proven_liquidity_gone: 1856
- no_momentum: 907
- research_failed: 719
- simulated failed buy: 288
- proven_low_volume: 251
- proven_price_collapsed_or_parabolic: 49
- proven: 40
- proven_no_uptrend: 22
- research_passed: 8
- dip: 7

Warning: 187 judged pools had an unreadable mint/freeze value. Check mint_raw / freeze_raw in candidates.csv; the parsing may need fixing.
