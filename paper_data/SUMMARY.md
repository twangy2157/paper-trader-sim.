# Paper trader summary

SIMULATION ONLY. No real trades.

Updated 2026-11-16T00:00:26Z. Bankroll cash (research-selected trades): 456.400154541351. Open positions: 9. Pools on watchlist: 64.

| group | n | win | avg | CI | P&L $ |
|---|---|---|---|---|---|
| research-picked | 16 | 25% | -33.9% | -64 to -3 | -544 |
| momentum, not picked | 2606 | 12% | -65.9% | -68 to -64 | -172047 |
| all momentum | 2622 | 12% | -65.7% | -68 to -63 | -172590 |
| control | 3338 | 6% | -18.7% | -20 to -17 | -62605 |
| dip buy | 35 | 29% | -12.5% | -31 to 8 | -440 |
| proven pools | 113 | 34% | -33.8% | -43 to -24 | -3825 |

What-if exit rules on the SAME trades. Cells: avg return (trades, win rate).

| exit rule | momentum | control | dip | proven |
|---|---|---|---|---|
| base_sl30_tp100 | -66% (2601, 12%) | -19% (3338, 6%) | -13% (35, 29%) | -34% (113, 34%) |
| wide_sl50_tp100 | -66% (2601, 13%) | -19% (3338, 6%) | -15% (35, 31%) | -35% (113, 34%) |
| sl30_tp50 | -67% (2601, 14%) | -19% (3338, 7%) | -18% (35, 31%) | -34% (113, 35%) |
| sl50_tp50 | -67% (2601, 16%) | -19% (3338, 7%) | -19% (35, 37%) | -35% (113, 35%) |
| no_stop_tp100 | -66% (2601, 14%) | -19% (3338, 6%) | -13% (35, 31%) | -36% (113, 34%) |

Verdict: NOT ENOUGH DATA (need 30+ closed filter=1 trades and a CI above zero before believing anything).

Pools seen: 90507. Outcomes:

- missed_window: 59351
- low_liquidity: 14891
- proven_liquidity_gone: 7587
- no_momentum: 3387
- research_failed: 2610
- proven_low_volume: 1204
- simulated failed buy: 1117
- proven_price_collapsed_or_parabolic: 138
- proven: 113
- proven_no_uptrend: 58
- dip: 35
- research_passed: 16

Warning: 713 judged pools had an unreadable mint/freeze value. Check mint_raw / freeze_raw in candidates.csv; the parsing may need fixing.
