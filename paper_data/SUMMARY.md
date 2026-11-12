# Paper trader summary

SIMULATION ONLY. No real trades.

Updated 2026-11-12T23:38:33Z. Bankroll cash (research-selected trades): 456.400154541351. Open positions: 23. Pools on watchlist: 54.

| group | n | win | avg | CI | P&L $ |
|---|---|---|---|---|---|
| research-picked | 16 | 25% | -33.9% | -64 to -3 | -544 |
| momentum, not picked | 2012 | 12% | -64.8% | -67 to -62 | -130629 |
| all momentum | 2028 | 12% | -64.6% | -67 to -62 | -131173 |
| control | 2788 | 6% | -17.8% | -19 to -17 | -49934 |
| dip buy | 28 | 25% | -19.9% | -41 to 3 | -559 |
| proven pools | 97 | 34% | -31.8% | -42 to -21 | -3092 |

What-if exit rules on the SAME trades. Cells: avg return (trades, win rate).

| exit rule | momentum | control | dip | proven |
|---|---|---|---|---|
| base_sl30_tp100 | -65% (2007, 12%) | -18% (2788, 6%) | -20% (28, 25%) | -32% (97, 34%) |
| wide_sl50_tp100 | -65% (2007, 13%) | -18% (2788, 6%) | -23% (28, 29%) | -33% (97, 34%) |
| sl30_tp50 | -66% (2007, 15%) | -18% (2788, 6%) | -24% (28, 29%) | -32% (97, 35%) |
| sl50_tp50 | -66% (2007, 16%) | -18% (2788, 7%) | -27% (28, 32%) | -33% (97, 35%) |
| no_stop_tp100 | -65% (2007, 14%) | -18% (2788, 6%) | -20% (28, 29%) | -34% (97, 34%) |

Verdict: NOT ENOUGH DATA (need 30+ closed filter=1 trades and a CI above zero before believing anything).

Pools seen: 71324. Outcomes:

- missed_window: 46981
- low_liquidity: 11536
- proven_liquidity_gone: 5689
- no_momentum: 2839
- research_failed: 2024
- proven_low_volume: 1058
- simulated failed buy: 889
- proven_price_collapsed_or_parabolic: 121
- proven: 100
- proven_no_uptrend: 42
- dip: 29
- research_passed: 16

Warning: 586 judged pools had an unreadable mint/freeze value. Check mint_raw / freeze_raw in candidates.csv; the parsing may need fixing.
