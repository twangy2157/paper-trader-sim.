# Paper trader summary

SIMULATION ONLY. No real trades.

Updated 2026-11-21T12:20:31Z. Bankroll cash (research-selected trades): 563.74568815387. Open positions: 12. Pools on watchlist: 66.

| group | n | win | avg | CI | P&L $ |
|---|---|---|---|---|---|
| research-picked | 20 | 35% | -21.7% | -51 to 10 | -436 |
| momentum, not picked | 3393 | 12% | -66.2% | -68 to -64 | -224857 |
| all momentum | 3413 | 12% | -65.9% | -68 to -64 | -225294 |
| control | 4131 | 6% | -19.3% | -20 to -18 | -79947 |
| dip buy | 46 | 26% | -15.1% | -32 to 2 | -695 |
| proven pools | 128 | 33% | -31.0% | -40 to -22 | -3984 |

What-if exit rules on the SAME trades. Cells: avg return (trades, win rate).

| exit rule | momentum | control | dip | proven |
|---|---|---|---|---|
| base_sl30_tp100 | -66% (3392, 12%) | -19% (4131, 6%) | -15% (46, 26%) | -31% (128, 33%) |
| wide_sl50_tp100 | -66% (3392, 13%) | -20% (4131, 6%) | -15% (46, 30%) | -32% (128, 33%) |
| sl30_tp50 | -68% (3392, 14%) | -19% (4131, 7%) | -18% (46, 33%) | -31% (128, 34%) |
| sl50_tp50 | -67% (3392, 15%) | -20% (4131, 7%) | -19% (46, 37%) | -32% (128, 34%) |
| no_stop_tp100 | -66% (3392, 14%) | -20% (4131, 7%) | -14% (46, 30%) | -33% (128, 33%) |

Verdict: NOT ENOUGH DATA (need 30+ closed filter=1 trades and a CI above zero before believing anything).

Pools seen: 112139. Outcomes:

- missed_window: 72634
- low_liquidity: 18929
- proven_liquidity_gone: 9742
- no_momentum: 4179
- research_failed: 3400
- proven_low_volume: 1429
- simulated failed buy: 1405
- proven_price_collapsed_or_parabolic: 163
- proven: 129
- proven_no_uptrend: 63
- dip: 46
- research_passed: 20

Warning: 883 judged pools had an unreadable mint/freeze value. Check mint_raw / freeze_raw in candidates.csv; the parsing may need fixing.
