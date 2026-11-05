# Paper trader summary

SIMULATION ONLY. No real trades.

Updated 2026-11-05T19:01:14Z. Bankroll cash (research-selected trades): 749.6403049524637. Open positions: 18. Pools on watchlist: 43.

| group | n | win | avg | CI | P&L $ |
|---|---|---|---|---|---|
| research-picked | 8 | 25% | -31.0% | -68 to 8 | -250 |
| momentum, not picked | 703 | 15% | -56.5% | -61 to -52 | -39747 |
| all momentum | 711 | 15% | -56.2% | -61 to -51 | -39998 |
| control | 849 | 7% | -19.2% | -22 to -17 | -16339 |
| dip buy | 7 | 14% | -27.3% | -65 to 10 | -191 |
| proven pools | 38 | 42% | -17.9% | -34 to -2 | -681 |

What-if exit rules on the SAME trades. Cells: avg return (trades, win rate).

| exit rule | momentum | control | dip | proven |
|---|---|---|---|---|
| base_sl30_tp100 | -57% (690, 15%) | -19% (849, 7%) | -27% (7, 14%) | -18% (38, 42%) |
| wide_sl50_tp100 | -57% (690, 17%) | -20% (849, 7%) | -32% (7, 14%) | -18% (38, 42%) |
| sl30_tp50 | -58% (690, 18%) | -19% (849, 8%) | -32% (7, 14%) | -20% (38, 42%) |
| sl50_tp50 | -57% (690, 21%) | -20% (849, 9%) | -36% (7, 14%) | -20% (38, 42%) |
| no_stop_tp100 | -56% (690, 18%) | -20% (849, 8%) | -27% (7, 14%) | -18% (38, 42%) |

Verdict: NOT ENOUGH DATA (need 30+ closed filter=1 trades and a CI above zero before believing anything).

Pools seen: 25034. Outcomes:

- missed_window: 16357
- low_liquidity: 4578
- proven_liquidity_gone: 1831
- no_momentum: 901
- research_failed: 711
- simulated failed buy: 282
- proven_low_volume: 248
- proven_price_collapsed_or_parabolic: 49
- proven: 40
- proven_no_uptrend: 22
- research_passed: 8
- dip: 7

Warning: 185 judged pools had an unreadable mint/freeze value. Check mint_raw / freeze_raw in candidates.csv; the parsing may need fixing.
