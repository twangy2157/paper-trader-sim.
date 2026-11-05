# Paper trader summary

SIMULATION ONLY. No real trades.

Updated 2026-11-05T13:51:20Z. Bankroll cash (research-selected trades): 749.6403049524637. Open positions: 12. Pools on watchlist: 77.

| group | n | win | avg | CI | P&L $ |
|---|---|---|---|---|---|
| research-picked | 8 | 25% | -31.0% | -68 to 8 | -250 |
| momentum, not picked | 661 | 15% | -55.4% | -60 to -51 | -36648 |
| all momentum | 669 | 15% | -55.1% | -60 to -50 | -36899 |
| control | 793 | 7% | -18.7% | -21 to -16 | -14936 |
| dip buy | 7 | 14% | -27.3% | -65 to 10 | -191 |
| proven pools | 38 | 42% | -17.9% | -34 to -2 | -681 |

What-if exit rules on the SAME trades. Cells: avg return (trades, win rate).

| exit rule | momentum | control | dip | proven |
|---|---|---|---|---|
| base_sl30_tp100 | -56% (648, 15%) | -19% (793, 7%) | -27% (7, 14%) | -18% (38, 42%) |
| wide_sl50_tp100 | -55% (648, 17%) | -19% (793, 8%) | -32% (7, 14%) | -18% (38, 42%) |
| sl30_tp50 | -57% (648, 19%) | -19% (793, 8%) | -32% (7, 14%) | -20% (38, 42%) |
| sl50_tp50 | -56% (648, 21%) | -19% (793, 9%) | -36% (7, 14%) | -20% (38, 42%) |
| no_stop_tp100 | -55% (648, 19%) | -19% (793, 8%) | -27% (7, 14%) | -18% (38, 42%) |

Verdict: NOT ENOUGH DATA (need 30+ closed filter=1 trades and a CI above zero before believing anything).

Pools seen: 23536. Outcomes:

- missed_window: 15336
- low_liquidity: 4367
- proven_liquidity_gone: 1697
- no_momentum: 846
- research_failed: 664
- simulated failed buy: 268
- proven_low_volume: 236
- proven_price_collapsed_or_parabolic: 48
- proven: 38
- proven_no_uptrend: 21
- research_passed: 8
- dip: 7

Warning: 174 judged pools had an unreadable mint/freeze value. Check mint_raw / freeze_raw in candidates.csv; the parsing may need fixing.
