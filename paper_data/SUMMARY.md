# Paper trader summary

SIMULATION ONLY. No real trades.

Updated 2026-11-05T19:34:21Z. Bankroll cash (research-selected trades): 749.6403049524637. Open positions: 16. Pools on watchlist: 44.

| group | n | win | avg | CI | P&L $ |
|---|---|---|---|---|---|
| research-picked | 8 | 25% | -31.0% | -68 to 8 | -250 |
| momentum, not picked | 708 | 14% | -56.8% | -61 to -52 | -40250 |
| all momentum | 716 | 15% | -56.5% | -61 to -52 | -40500 |
| control | 854 | 7% | -19.2% | -22 to -17 | -16456 |
| dip buy | 7 | 14% | -27.3% | -65 to 10 | -191 |
| proven pools | 38 | 42% | -17.9% | -34 to -2 | -681 |

What-if exit rules on the SAME trades. Cells: avg return (trades, win rate).

| exit rule | momentum | control | dip | proven |
|---|---|---|---|---|
| base_sl30_tp100 | -57% (695, 15%) | -19% (854, 7%) | -27% (7, 14%) | -18% (38, 42%) |
| wide_sl50_tp100 | -57% (695, 17%) | -20% (854, 7%) | -32% (7, 14%) | -18% (38, 42%) |
| sl30_tp50 | -58% (695, 18%) | -19% (854, 8%) | -32% (7, 14%) | -20% (38, 42%) |
| sl50_tp50 | -58% (695, 20%) | -20% (854, 9%) | -36% (7, 14%) | -20% (38, 42%) |
| no_stop_tp100 | -56% (695, 18%) | -20% (854, 8%) | -27% (7, 14%) | -18% (38, 42%) |

Verdict: NOT ENOUGH DATA (need 30+ closed filter=1 trades and a CI above zero before believing anything).

Pools seen: 25177. Outcomes:

- missed_window: 16445
- low_liquidity: 4604
- proven_liquidity_gone: 1847
- no_momentum: 905
- research_failed: 715
- simulated failed buy: 285
- proven_low_volume: 250
- proven_price_collapsed_or_parabolic: 49
- proven: 40
- proven_no_uptrend: 22
- research_passed: 8
- dip: 7

Warning: 185 judged pools had an unreadable mint/freeze value. Check mint_raw / freeze_raw in candidates.csv; the parsing may need fixing.
