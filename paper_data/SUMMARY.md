# Paper trader summary

SIMULATION ONLY. No real trades.

Updated 2026-11-11T09:36:42Z. Bankroll cash (research-selected trades): 456.400154541351. Open positions: 18. Pools on watchlist: 43.

| group | n | win | avg | CI | P&L $ |
|---|---|---|---|---|---|
| research-picked | 16 | 25% | -33.9% | -64 to -3 | -544 |
| momentum, not picked | 1708 | 12% | -64.9% | -68 to -62 | -110945 |
| all momentum | 1724 | 12% | -64.6% | -67 to -62 | -111489 |
| control | 2458 | 5% | -17.9% | -19 to -17 | -44239 |
| dip buy | 20 | 25% | -16.1% | -42 to 10 | -323 |
| proven pools | 81 | 36% | -27.1% | -38 to -17 | -2201 |

What-if exit rules on the SAME trades. Cells: avg return (trades, win rate).

| exit rule | momentum | control | dip | proven |
|---|---|---|---|---|
| base_sl30_tp100 | -65% (1703, 12%) | -18% (2458, 5%) | -16% (20, 25%) | -27% (81, 36%) |
| wide_sl50_tp100 | -65% (1703, 13%) | -18% (2458, 5%) | -20% (20, 30%) | -29% (81, 36%) |
| sl30_tp50 | -66% (1703, 15%) | -18% (2458, 6%) | -26% (20, 25%) | -28% (81, 36%) |
| sl50_tp50 | -65% (1703, 16%) | -18% (2458, 6%) | -30% (20, 30%) | -30% (81, 36%) |
| no_stop_tp100 | -65% (1703, 14%) | -19% (2458, 5%) | -17% (20, 30%) | -29% (81, 36%) |

Verdict: NOT ENOUGH DATA (need 30+ closed filter=1 trades and a CI above zero before believing anything).

Pools seen: 61506. Outcomes:

- missed_window: 40660
- low_liquidity: 9892
- proven_liquidity_gone: 4705
- no_momentum: 2513
- research_failed: 1713
- proven_low_volume: 971
- simulated failed buy: 790
- proven_price_collapsed_or_parabolic: 106
- proven: 83
- proven_no_uptrend: 37
- dip: 20
- research_passed: 16

Warning: 529 judged pools had an unreadable mint/freeze value. Check mint_raw / freeze_raw in candidates.csv; the parsing may need fixing.
