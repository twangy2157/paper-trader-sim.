# Paper trader summary

SIMULATION ONLY. No real trades.

Updated 2026-11-21T20:55:58Z. Bankroll cash (research-selected trades): 563.74568815387. Open positions: 20. Pools on watchlist: 80.

| group | n | win | avg | CI | P&L $ |
|---|---|---|---|---|---|
| research-picked | 20 | 35% | -21.7% | -51 to 10 | -436 |
| momentum, not picked | 3407 | 12% | -66.1% | -68 to -64 | -225630 |
| all momentum | 3427 | 12% | -65.9% | -68 to -64 | -226067 |
| control | 4151 | 6% | -19.3% | -20 to -18 | -80583 |
| dip buy | 46 | 26% | -15.1% | -32 to 2 | -695 |
| proven pools | 129 | 33% | -31.0% | -40 to -22 | -4016 |

What-if exit rules on the SAME trades. Cells: avg return (trades, win rate).

| exit rule | momentum | control | dip | proven |
|---|---|---|---|---|
| base_sl30_tp100 | -66% (3406, 12%) | -19% (4151, 6%) | -15% (46, 26%) | -31% (129, 33%) |
| wide_sl50_tp100 | -66% (3406, 13%) | -20% (4151, 6%) | -15% (46, 30%) | -32% (129, 33%) |
| sl30_tp50 | -68% (3406, 14%) | -19% (4151, 7%) | -18% (46, 33%) | -31% (129, 33%) |
| sl50_tp50 | -67% (3406, 15%) | -20% (4151, 7%) | -19% (46, 37%) | -32% (129, 33%) |
| no_stop_tp100 | -66% (3406, 14%) | -20% (4151, 7%) | -14% (46, 30%) | -33% (129, 33%) |

Verdict: NOT ENOUGH DATA (need 30+ closed filter=1 trades and a CI above zero before believing anything).

Pools seen: 112701. Outcomes:

- missed_window: 73001
- low_liquidity: 19067
- proven_liquidity_gone: 9743
- no_momentum: 4202
- research_failed: 3420
- proven_low_volume: 1430
- simulated failed buy: 1417
- proven_price_collapsed_or_parabolic: 163
- proven: 129
- proven_no_uptrend: 63
- dip: 46
- research_passed: 20

Warning: 888 judged pools had an unreadable mint/freeze value. Check mint_raw / freeze_raw in candidates.csv; the parsing may need fixing.
