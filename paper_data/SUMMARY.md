# Paper trader summary

SIMULATION ONLY. No real trades.

Updated 2026-11-06T10:22:44Z. Bankroll cash (research-selected trades): 649.8381952860861. Open positions: 17. Pools on watchlist: 43.

| group | n | win | avg | CI | P&L $ |
|---|---|---|---|---|---|
| research-picked | 9 | 22% | -38.7% | -74 to -0 | -350 |
| momentum, not picked | 830 | 14% | -59.1% | -63 to -55 | -49125 |
| all momentum | 839 | 14% | -58.9% | -63 to -55 | -49475 |
| control | 985 | 7% | -20.2% | -23 to -18 | -19939 |
| dip buy | 8 | 12% | -36.3% | -72 to 3 | -290 |
| proven pools | 41 | 46% | -14.7% | -30 to 0 | -607 |

What-if exit rules on the SAME trades. Cells: avg return (trades, win rate).

| exit rule | momentum | control | dip | proven |
|---|---|---|---|---|
| base_sl30_tp100 | -59% (818, 14%) | -20% (985, 7%) | -36% (8, 12%) | -15% (41, 46%) |
| wide_sl50_tp100 | -59% (818, 16%) | -21% (985, 7%) | -40% (8, 12%) | -15% (41, 46%) |
| sl30_tp50 | -61% (818, 17%) | -21% (985, 8%) | -40% (8, 12%) | -17% (41, 46%) |
| sl50_tp50 | -60% (818, 19%) | -21% (985, 8%) | -44% (8, 12%) | -17% (41, 46%) |
| no_stop_tp100 | -59% (818, 17%) | -21% (985, 7%) | -36% (8, 12%) | -15% (41, 46%) |

Verdict: NOT ENOUGH DATA (need 30+ closed filter=1 trades and a CI above zero before believing anything).

Pools seen: 29201. Outcomes:

- missed_window: 19008
- low_liquidity: 5322
- proven_liquidity_gone: 2234
- no_momentum: 1040
- research_failed: 834
- simulated failed buy: 344
- proven_low_volume: 283
- proven_price_collapsed_or_parabolic: 54
- proven: 43
- proven_no_uptrend: 22
- research_passed: 9
- dip: 8

Warning: 219 judged pools had an unreadable mint/freeze value. Check mint_raw / freeze_raw in candidates.csv; the parsing may need fixing.
