# Paper trader summary

SIMULATION ONLY. No real trades.

Updated 2026-11-12T06:19:09Z. Bankroll cash (research-selected trades): 456.400154541351. Open positions: 15. Pools on watchlist: 60.

| group | n | win | avg | CI | P&L $ |
|---|---|---|---|---|---|
| research-picked | 16 | 25% | -33.9% | -64 to -3 | -544 |
| momentum, not picked | 1877 | 12% | -64.6% | -67 to -62 | -121348 |
| all momentum | 1893 | 12% | -64.3% | -67 to -62 | -121892 |
| control | 2647 | 6% | -17.9% | -19 to -17 | -47723 |
| dip buy | 24 | 25% | -16.7% | -40 to 7 | -402 |
| proven pools | 89 | 35% | -28.6% | -39 to -18 | -2554 |

What-if exit rules on the SAME trades. Cells: avg return (trades, win rate).

| exit rule | momentum | control | dip | proven |
|---|---|---|---|---|
| base_sl30_tp100 | -65% (1872, 12%) | -18% (2647, 6%) | -17% (24, 25%) | -29% (89, 35%) |
| wide_sl50_tp100 | -65% (1872, 13%) | -18% (2647, 6%) | -20% (24, 29%) | -30% (89, 35%) |
| sl30_tp50 | -66% (1872, 15%) | -18% (2647, 6%) | -26% (24, 25%) | -30% (89, 35%) |
| sl50_tp50 | -65% (1872, 16%) | -18% (2647, 7%) | -30% (24, 29%) | -31% (89, 35%) |
| no_stop_tp100 | -65% (1872, 14%) | -18% (2647, 6%) | -17% (24, 29%) | -31% (89, 35%) |

Verdict: NOT ENOUGH DATA (need 30+ closed filter=1 trades and a CI above zero before believing anything).

Pools seen: 67079. Outcomes:

- missed_window: 44345
- low_liquidity: 10767
- proven_liquidity_gone: 5240
- no_momentum: 2699
- research_failed: 1883
- proven_low_volume: 1023
- simulated failed buy: 837
- proven_price_collapsed_or_parabolic: 116
- proven: 89
- proven_no_uptrend: 39
- dip: 25
- research_passed: 16

Warning: 555 judged pools had an unreadable mint/freeze value. Check mint_raw / freeze_raw in candidates.csv; the parsing may need fixing.
