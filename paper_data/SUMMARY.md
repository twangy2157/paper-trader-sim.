# Paper trader summary

SIMULATION ONLY. No real trades.

Updated 2026-11-06T01:49:35Z. Bankroll cash (research-selected trades): 749.6403049524637. Open positions: 19. Pools on watchlist: 80.

| group | n | win | avg | CI | P&L $ |
|---|---|---|---|---|---|
| research-picked | 8 | 25% | -31.0% | -68 to 8 | -250 |
| momentum, not picked | 752 | 14% | -58.1% | -62 to -54 | -43725 |
| all momentum | 760 | 14% | -57.8% | -62 to -53 | -43976 |
| control | 910 | 7% | -19.1% | -22 to -17 | -17497 |
| dip buy | 7 | 14% | -27.3% | -65 to 10 | -191 |
| proven pools | 40 | 45% | -15.2% | -31 to 0 | -612 |

What-if exit rules on the SAME trades. Cells: avg return (trades, win rate).

| exit rule | momentum | control | dip | proven |
|---|---|---|---|---|
| base_sl30_tp100 | -58% (739, 14%) | -19% (910, 7%) | -27% (7, 14%) | -15% (40, 45%) |
| wide_sl50_tp100 | -58% (739, 16%) | -20% (910, 7%) | -32% (7, 14%) | -15% (40, 45%) |
| sl30_tp50 | -60% (739, 18%) | -20% (910, 8%) | -32% (7, 14%) | -18% (40, 45%) |
| sl50_tp50 | -59% (739, 20%) | -20% (910, 8%) | -36% (7, 14%) | -18% (40, 45%) |
| no_stop_tp100 | -58% (739, 17%) | -20% (910, 7%) | -27% (7, 14%) | -15% (40, 45%) |

Verdict: NOT ENOUGH DATA (need 30+ closed filter=1 trades and a CI above zero before believing anything).

Pools seen: 26950. Outcomes:

- missed_window: 17578
- low_liquidity: 4925
- proven_liquidity_gone: 2008
- no_momentum: 962
- research_failed: 762
- simulated failed buy: 318
- proven_low_volume: 267
- proven_price_collapsed_or_parabolic: 52
- proven: 40
- proven_no_uptrend: 22
- research_passed: 8
- dip: 8

Warning: 206 judged pools had an unreadable mint/freeze value. Check mint_raw / freeze_raw in candidates.csv; the parsing may need fixing.
