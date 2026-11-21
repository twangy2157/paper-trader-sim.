# Paper trader summary

SIMULATION ONLY. No real trades.

Updated 2026-11-21T08:40:11Z. Bankroll cash (research-selected trades): 563.74568815387. Open positions: 24. Pools on watchlist: 43.

| group | n | win | avg | CI | P&L $ |
|---|---|---|---|---|---|
| research-picked | 20 | 35% | -21.7% | -51 to 10 | -436 |
| momentum, not picked | 3361 | 12% | -66.3% | -68 to -64 | -223016 |
| all momentum | 3381 | 12% | -66.0% | -68 to -64 | -223453 |
| control | 4098 | 6% | -19.2% | -20 to -18 | -79072 |
| dip buy | 46 | 26% | -15.1% | -32 to 2 | -695 |
| proven pools | 127 | 33% | -30.5% | -40 to -21 | -3883 |

What-if exit rules on the SAME trades. Cells: avg return (trades, win rate).

| exit rule | momentum | control | dip | proven |
|---|---|---|---|---|
| base_sl30_tp100 | -66% (3360, 12%) | -19% (4098, 6%) | -15% (46, 26%) | -30% (127, 33%) |
| wide_sl50_tp100 | -66% (3360, 13%) | -19% (4098, 6%) | -15% (46, 30%) | -31% (127, 33%) |
| sl30_tp50 | -68% (3360, 14%) | -19% (4098, 7%) | -18% (46, 33%) | -31% (127, 34%) |
| sl50_tp50 | -67% (3360, 15%) | -20% (4098, 8%) | -19% (46, 37%) | -32% (127, 34%) |
| no_stop_tp100 | -66% (3360, 14%) | -20% (4098, 7%) | -14% (46, 30%) | -32% (127, 33%) |

Verdict: NOT ENOUGH DATA (need 30+ closed filter=1 trades and a CI above zero before believing anything).

Pools seen: 111139. Outcomes:

- missed_window: 72000
- low_liquidity: 18745
- proven_liquidity_gone: 9641
- no_momentum: 4154
- research_failed: 3373
- proven_low_volume: 1416
- simulated failed buy: 1393
- proven_price_collapsed_or_parabolic: 161
- proven: 127
- proven_no_uptrend: 63
- dip: 46
- research_passed: 20

Warning: 879 judged pools had an unreadable mint/freeze value. Check mint_raw / freeze_raw in candidates.csv; the parsing may need fixing.
