# Paper trader summary

SIMULATION ONLY. No real trades.

Updated 2026-11-12T05:57:12Z. Bankroll cash (research-selected trades): 456.400154541351. Open positions: 22. Pools on watchlist: 69.

| group | n | win | avg | CI | P&L $ |
|---|---|---|---|---|---|
| research-picked | 16 | 25% | -33.9% | -64 to -3 | -544 |
| momentum, not picked | 1874 | 12% | -64.6% | -67 to -62 | -121144 |
| all momentum | 1890 | 12% | -64.3% | -67 to -62 | -121687 |
| control | 2640 | 6% | -17.9% | -19 to -17 | -47567 |
| dip buy | 24 | 25% | -16.7% | -40 to 7 | -402 |
| proven pools | 88 | 35% | -28.5% | -39 to -18 | -2514 |

What-if exit rules on the SAME trades. Cells: avg return (trades, win rate).

| exit rule | momentum | control | dip | proven |
|---|---|---|---|---|
| base_sl30_tp100 | -65% (1869, 12%) | -18% (2640, 6%) | -17% (24, 25%) | -28% (88, 35%) |
| wide_sl50_tp100 | -65% (1869, 13%) | -18% (2640, 6%) | -20% (24, 29%) | -30% (88, 35%) |
| sl30_tp50 | -66% (1869, 15%) | -18% (2640, 6%) | -26% (24, 25%) | -30% (88, 35%) |
| sl50_tp50 | -65% (1869, 16%) | -18% (2640, 7%) | -30% (24, 29%) | -31% (88, 35%) |
| no_stop_tp100 | -65% (1869, 14%) | -18% (2640, 6%) | -17% (24, 29%) | -31% (88, 35%) |

Verdict: NOT ENOUGH DATA (need 30+ closed filter=1 trades and a CI above zero before believing anything).

Pools seen: 66974. Outcomes:

- missed_window: 44268
- low_liquidity: 10758
- proven_liquidity_gone: 5228
- no_momentum: 2697
- research_failed: 1881
- proven_low_volume: 1021
- simulated failed buy: 836
- proven_price_collapsed_or_parabolic: 116
- proven: 89
- proven_no_uptrend: 39
- dip: 25
- research_passed: 16

Warning: 554 judged pools had an unreadable mint/freeze value. Check mint_raw / freeze_raw in candidates.csv; the parsing may need fixing.
