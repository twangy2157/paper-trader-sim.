# Paper trader summary

SIMULATION ONLY. No real trades.

Updated 2026-11-12T20:59:21Z. Bankroll cash (research-selected trades): 456.400154541351. Open positions: 15. Pools on watchlist: 54.

| group | n | win | avg | CI | P&L $ |
|---|---|---|---|---|---|
| research-picked | 16 | 25% | -33.9% | -64 to -3 | -544 |
| momentum, not picked | 1997 | 12% | -65.0% | -67 to -62 | -130025 |
| all momentum | 2013 | 12% | -64.8% | -67 to -62 | -130569 |
| control | 2767 | 6% | -17.8% | -19 to -16 | -49591 |
| dip buy | 28 | 25% | -19.9% | -41 to 3 | -559 |
| proven pools | 96 | 34% | -31.1% | -42 to -20 | -2992 |

What-if exit rules on the SAME trades. Cells: avg return (trades, win rate).

| exit rule | momentum | control | dip | proven |
|---|---|---|---|---|
| base_sl30_tp100 | -65% (1992, 12%) | -18% (2767, 6%) | -20% (28, 25%) | -31% (96, 34%) |
| wide_sl50_tp100 | -65% (1992, 13%) | -18% (2767, 6%) | -23% (28, 29%) | -33% (96, 34%) |
| sl30_tp50 | -66% (1992, 15%) | -18% (2767, 7%) | -24% (28, 29%) | -31% (96, 35%) |
| sl50_tp50 | -66% (1992, 16%) | -18% (2767, 7%) | -27% (28, 32%) | -33% (96, 35%) |
| no_stop_tp100 | -65% (1992, 14%) | -18% (2767, 6%) | -20% (28, 29%) | -33% (96, 34%) |

Verdict: NOT ENOUGH DATA (need 30+ closed filter=1 trades and a CI above zero before believing anything).

Pools seen: 70579. Outcomes:

- missed_window: 46511
- low_liquidity: 11385
- proven_liquidity_gone: 5626
- no_momentum: 2818
- research_failed: 2004
- proven_low_volume: 1048
- simulated failed buy: 883
- proven_price_collapsed_or_parabolic: 121
- proven: 97
- proven_no_uptrend: 42
- dip: 28
- research_passed: 16

Warning: 582 judged pools had an unreadable mint/freeze value. Check mint_raw / freeze_raw in candidates.csv; the parsing may need fixing.
