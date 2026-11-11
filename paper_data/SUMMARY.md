# Paper trader summary

SIMULATION ONLY. No real trades.

Updated 2026-11-11T09:47:42Z. Bankroll cash (research-selected trades): 456.400154541351. Open positions: 15. Pools on watchlist: 65.

| group | n | win | avg | CI | P&L $ |
|---|---|---|---|---|---|
| research-picked | 16 | 25% | -33.9% | -64 to -3 | -544 |
| momentum, not picked | 1709 | 12% | -64.9% | -68 to -62 | -111045 |
| all momentum | 1725 | 12% | -64.6% | -67 to -62 | -111589 |
| control | 2463 | 5% | -18.0% | -19 to -17 | -44454 |
| dip buy | 20 | 25% | -16.1% | -42 to 10 | -323 |
| proven pools | 81 | 36% | -27.1% | -38 to -17 | -2201 |

What-if exit rules on the SAME trades. Cells: avg return (trades, win rate).

| exit rule | momentum | control | dip | proven |
|---|---|---|---|---|
| base_sl30_tp100 | -65% (1704, 12%) | -18% (2463, 5%) | -16% (20, 25%) | -27% (81, 36%) |
| wide_sl50_tp100 | -65% (1704, 13%) | -18% (2463, 5%) | -20% (20, 30%) | -29% (81, 36%) |
| sl30_tp50 | -66% (1704, 15%) | -18% (2463, 6%) | -26% (20, 25%) | -28% (81, 36%) |
| sl50_tp50 | -66% (1704, 16%) | -18% (2463, 6%) | -30% (20, 30%) | -30% (81, 36%) |
| no_stop_tp100 | -65% (1704, 14%) | -19% (2463, 5%) | -17% (20, 30%) | -29% (81, 36%) |

Verdict: NOT ENOUGH DATA (need 30+ closed filter=1 trades and a CI above zero before believing anything).

Pools seen: 61547. Outcomes:

- missed_window: 40690
- low_liquidity: 9896
- proven_liquidity_gone: 4709
- no_momentum: 2516
- research_failed: 1713
- proven_low_volume: 971
- simulated failed buy: 790
- proven_price_collapsed_or_parabolic: 106
- proven: 83
- proven_no_uptrend: 37
- dip: 20
- research_passed: 16

Warning: 529 judged pools had an unreadable mint/freeze value. Check mint_raw / freeze_raw in candidates.csv; the parsing may need fixing.
