# Paper trader summary

SIMULATION ONLY. No real trades.

Updated 2026-11-13T03:40:41Z. Bankroll cash (research-selected trades): 456.400154541351. Open positions: 22. Pools on watchlist: 74.

| group | n | win | avg | CI | P&L $ |
|---|---|---|---|---|---|
| research-picked | 16 | 25% | -33.9% | -64 to -3 | -544 |
| momentum, not picked | 2044 | 12% | -64.7% | -67 to -62 | -132488 |
| all momentum | 2060 | 12% | -64.5% | -67 to -62 | -133031 |
| control | 2812 | 6% | -17.9% | -19 to -17 | -50540 |
| dip buy | 29 | 24% | -20.4% | -41 to 2 | -593 |
| proven pools | 100 | 33% | -33.6% | -43 to -23 | -3368 |

What-if exit rules on the SAME trades. Cells: avg return (trades, win rate).

| exit rule | momentum | control | dip | proven |
|---|---|---|---|---|
| base_sl30_tp100 | -65% (2039, 12%) | -18% (2812, 6%) | -20% (29, 24%) | -34% (100, 33%) |
| wide_sl50_tp100 | -65% (2039, 13%) | -18% (2812, 6%) | -24% (29, 28%) | -35% (100, 33%) |
| sl30_tp50 | -66% (2039, 15%) | -18% (2812, 6%) | -25% (29, 28%) | -33% (100, 34%) |
| sl50_tp50 | -66% (2039, 16%) | -18% (2812, 7%) | -28% (29, 31%) | -35% (100, 34%) |
| no_stop_tp100 | -65% (2039, 14%) | -18% (2812, 6%) | -22% (29, 28%) | -36% (100, 33%) |

Verdict: NOT ENOUGH DATA (need 30+ closed filter=1 trades and a CI above zero before believing anything).

Pools seen: 72391. Outcomes:

- missed_window: 47706
- low_liquidity: 11702
- proven_liquidity_gone: 5789
- no_momentum: 2864
- research_failed: 2055
- proven_low_volume: 1063
- simulated failed buy: 901
- proven_price_collapsed_or_parabolic: 121
- proven: 103
- proven_no_uptrend: 42
- dip: 29
- research_passed: 16

Warning: 592 judged pools had an unreadable mint/freeze value. Check mint_raw / freeze_raw in candidates.csv; the parsing may need fixing.
