# Paper trader summary

SIMULATION ONLY. No real trades.

Updated 2026-11-21T11:17:41Z. Bankroll cash (research-selected trades): 563.74568815387. Open positions: 25. Pools on watchlist: 51.

| group | n | win | avg | CI | P&L $ |
|---|---|---|---|---|---|
| research-picked | 20 | 35% | -21.7% | -51 to 10 | -436 |
| momentum, not picked | 3384 | 12% | -66.2% | -68 to -64 | -224238 |
| all momentum | 3404 | 12% | -65.9% | -68 to -64 | -224675 |
| control | 4116 | 6% | -19.2% | -20 to -18 | -79500 |
| dip buy | 46 | 26% | -15.1% | -32 to 2 | -695 |
| proven pools | 127 | 33% | -30.5% | -40 to -21 | -3883 |

What-if exit rules on the SAME trades. Cells: avg return (trades, win rate).

| exit rule | momentum | control | dip | proven |
|---|---|---|---|---|
| base_sl30_tp100 | -66% (3383, 12%) | -19% (4116, 6%) | -15% (46, 26%) | -30% (127, 33%) |
| wide_sl50_tp100 | -66% (3383, 13%) | -19% (4116, 6%) | -15% (46, 30%) | -31% (127, 33%) |
| sl30_tp50 | -68% (3383, 14%) | -19% (4116, 7%) | -18% (46, 33%) | -31% (127, 34%) |
| sl50_tp50 | -67% (3383, 15%) | -20% (4116, 7%) | -19% (46, 37%) | -32% (127, 34%) |
| no_stop_tp100 | -66% (3383, 14%) | -20% (4116, 7%) | -14% (46, 30%) | -32% (127, 33%) |

Verdict: NOT ENOUGH DATA (need 30+ closed filter=1 trades and a CI above zero before believing anything).

Pools seen: 111868. Outcomes:

- missed_window: 72454
- low_liquidity: 18890
- proven_liquidity_gone: 9707
- no_momentum: 4175
- research_failed: 3393
- proven_low_volume: 1427
- simulated failed buy: 1402
- proven_price_collapsed_or_parabolic: 163
- proven: 128
- proven_no_uptrend: 63
- dip: 46
- research_passed: 20

Warning: 882 judged pools had an unreadable mint/freeze value. Check mint_raw / freeze_raw in candidates.csv; the parsing may need fixing.
