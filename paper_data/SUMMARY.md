# Paper trader summary

SIMULATION ONLY. No real trades.

Updated 2026-11-21T23:23:58Z. Bankroll cash (research-selected trades): 563.74568815387. Open positions: 24. Pools on watchlist: 40.

| group | n | win | avg | CI | P&L $ |
|---|---|---|---|---|---|
| research-picked | 20 | 35% | -21.7% | -51 to 10 | -436 |
| momentum, not picked | 3430 | 12% | -66.2% | -68 to -64 | -227265 |
| all momentum | 3450 | 12% | -65.9% | -68 to -64 | -227701 |
| control | 4165 | 6% | -19.3% | -20 to -18 | -80556 |
| dip buy | 46 | 26% | -15.1% | -32 to 2 | -695 |
| proven pools | 129 | 33% | -31.0% | -40 to -22 | -4017 |

What-if exit rules on the SAME trades. Cells: avg return (trades, win rate).

| exit rule | momentum | control | dip | proven |
|---|---|---|---|---|
| base_sl30_tp100 | -66% (3429, 12%) | -19% (4165, 6%) | -15% (46, 26%) | -31% (129, 33%) |
| wide_sl50_tp100 | -66% (3429, 13%) | -20% (4165, 6%) | -15% (46, 30%) | -32% (129, 33%) |
| sl30_tp50 | -68% (3429, 14%) | -19% (4165, 7%) | -18% (46, 33%) | -31% (129, 33%) |
| sl50_tp50 | -67% (3429, 15%) | -20% (4165, 8%) | -19% (46, 37%) | -32% (129, 33%) |
| no_stop_tp100 | -66% (3429, 14%) | -20% (4165, 7%) | -14% (46, 30%) | -33% (129, 33%) |

Verdict: NOT ENOUGH DATA (need 30+ closed filter=1 trades and a CI above zero before believing anything).

Pools seen: 113450. Outcomes:

- missed_window: 73517
- low_liquidity: 19177
- proven_liquidity_gone: 9803
- no_momentum: 4222
- research_failed: 3441
- proven_low_volume: 1441
- simulated failed buy: 1427
- proven_price_collapsed_or_parabolic: 163
- proven: 129
- proven_no_uptrend: 64
- dip: 46
- research_passed: 20

Warning: 889 judged pools had an unreadable mint/freeze value. Check mint_raw / freeze_raw in candidates.csv; the parsing may need fixing.
