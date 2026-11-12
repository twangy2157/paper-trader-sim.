# Paper trader summary

SIMULATION ONLY. No real trades.

Updated 2026-11-12T06:40:11Z. Bankroll cash (research-selected trades): 456.400154541351. Open positions: 15. Pools on watchlist: 34.

| group | n | win | avg | CI | P&L $ |
|---|---|---|---|---|---|
| research-picked | 16 | 25% | -33.9% | -64 to -3 | -544 |
| momentum, not picked | 1880 | 12% | -64.6% | -67 to -62 | -121649 |
| all momentum | 1896 | 12% | -64.4% | -67 to -62 | -122192 |
| control | 2652 | 6% | -17.9% | -19 to -17 | -47792 |
| dip buy | 24 | 25% | -16.7% | -40 to 7 | -402 |
| proven pools | 89 | 35% | -28.6% | -39 to -18 | -2554 |

What-if exit rules on the SAME trades. Cells: avg return (trades, win rate).

| exit rule | momentum | control | dip | proven |
|---|---|---|---|---|
| base_sl30_tp100 | -65% (1875, 12%) | -18% (2652, 6%) | -17% (24, 25%) | -29% (89, 35%) |
| wide_sl50_tp100 | -65% (1875, 13%) | -18% (2652, 6%) | -20% (24, 29%) | -30% (89, 35%) |
| sl30_tp50 | -66% (1875, 15%) | -18% (2652, 6%) | -26% (24, 25%) | -30% (89, 35%) |
| sl50_tp50 | -66% (1875, 16%) | -18% (2652, 7%) | -30% (24, 29%) | -31% (89, 35%) |
| no_stop_tp100 | -65% (1875, 14%) | -18% (2652, 6%) | -17% (24, 29%) | -31% (89, 35%) |

Verdict: NOT ENOUGH DATA (need 30+ closed filter=1 trades and a CI above zero before believing anything).

Pools seen: 67183. Outcomes:

- missed_window: 44417
- low_liquidity: 10778
- proven_liquidity_gone: 5250
- no_momentum: 2702
- research_failed: 1886
- proven_low_volume: 1023
- simulated failed buy: 840
- proven_price_collapsed_or_parabolic: 116
- proven: 91
- proven_no_uptrend: 39
- dip: 25
- research_passed: 16

Warning: 557 judged pools had an unreadable mint/freeze value. Check mint_raw / freeze_raw in candidates.csv; the parsing may need fixing.
