# Paper trader summary

SIMULATION ONLY. No real trades.

Updated 2026-11-13T04:22:44Z. Bankroll cash (research-selected trades): 456.400154541351. Open positions: 20. Pools on watchlist: 54.

| group | n | win | avg | CI | P&L $ |
|---|---|---|---|---|---|
| research-picked | 16 | 25% | -33.9% | -64 to -3 | -544 |
| momentum, not picked | 2053 | 12% | -64.8% | -67 to -62 | -133125 |
| all momentum | 2069 | 12% | -64.5% | -67 to -62 | -133669 |
| control | 2818 | 6% | -17.8% | -19 to -16 | -50503 |
| dip buy | 29 | 24% | -20.4% | -41 to 2 | -593 |
| proven pools | 100 | 33% | -33.6% | -43 to -23 | -3368 |

What-if exit rules on the SAME trades. Cells: avg return (trades, win rate).

| exit rule | momentum | control | dip | proven |
|---|---|---|---|---|
| base_sl30_tp100 | -65% (2048, 12%) | -18% (2818, 6%) | -20% (29, 24%) | -34% (100, 33%) |
| wide_sl50_tp100 | -65% (2048, 13%) | -18% (2818, 6%) | -24% (29, 28%) | -35% (100, 33%) |
| sl30_tp50 | -66% (2048, 15%) | -18% (2818, 6%) | -25% (29, 28%) | -33% (100, 34%) |
| sl50_tp50 | -66% (2048, 16%) | -18% (2818, 7%) | -28% (29, 31%) | -35% (100, 34%) |
| no_stop_tp100 | -65% (2048, 14%) | -18% (2818, 6%) | -22% (29, 28%) | -36% (100, 33%) |

Verdict: NOT ENOUGH DATA (need 30+ closed filter=1 trades and a CI above zero before believing anything).

Pools seen: 72614. Outcomes:

- missed_window: 47867
- low_liquidity: 11721
- proven_liquidity_gone: 5816
- no_momentum: 2872
- research_failed: 2060
- proven_low_volume: 1065
- simulated failed buy: 902
- proven_price_collapsed_or_parabolic: 121
- proven: 103
- proven_no_uptrend: 42
- dip: 29
- research_passed: 16

Warning: 593 judged pools had an unreadable mint/freeze value. Check mint_raw / freeze_raw in candidates.csv; the parsing may need fixing.
