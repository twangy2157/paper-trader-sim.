# Paper trader summary

SIMULATION ONLY. No real trades.

Updated 2026-11-21T08:29:46Z. Bankroll cash (research-selected trades): 563.74568815387. Open positions: 22. Pools on watchlist: 39.

| group | n | win | avg | CI | P&L $ |
|---|---|---|---|---|---|
| research-picked | 20 | 35% | -21.7% | -51 to 10 | -436 |
| momentum, not picked | 3360 | 12% | -66.3% | -68 to -64 | -223012 |
| all momentum | 3380 | 12% | -66.0% | -68 to -64 | -223448 |
| control | 4096 | 6% | -19.2% | -20 to -18 | -79061 |
| dip buy | 46 | 26% | -15.1% | -32 to 2 | -695 |
| proven pools | 127 | 33% | -30.5% | -40 to -21 | -3883 |

What-if exit rules on the SAME trades. Cells: avg return (trades, win rate).

| exit rule | momentum | control | dip | proven |
|---|---|---|---|---|
| base_sl30_tp100 | -66% (3359, 12%) | -19% (4096, 6%) | -15% (46, 26%) | -30% (127, 33%) |
| wide_sl50_tp100 | -66% (3359, 13%) | -19% (4096, 6%) | -15% (46, 30%) | -31% (127, 33%) |
| sl30_tp50 | -68% (3359, 14%) | -19% (4096, 7%) | -18% (46, 33%) | -31% (127, 34%) |
| sl50_tp50 | -67% (3359, 15%) | -20% (4096, 8%) | -19% (46, 37%) | -32% (127, 34%) |
| no_stop_tp100 | -66% (3359, 14%) | -20% (4096, 7%) | -14% (46, 30%) | -32% (127, 33%) |

Verdict: NOT ENOUGH DATA (need 30+ closed filter=1 trades and a CI above zero before believing anything).

Pools seen: 111109. Outcomes:

- missed_window: 71985
- low_liquidity: 18736
- proven_liquidity_gone: 9641
- no_momentum: 4151
- research_failed: 3371
- proven_low_volume: 1416
- simulated failed buy: 1392
- proven_price_collapsed_or_parabolic: 161
- proven: 127
- proven_no_uptrend: 63
- dip: 46
- research_passed: 20

Warning: 878 judged pools had an unreadable mint/freeze value. Check mint_raw / freeze_raw in candidates.csv; the parsing may need fixing.
