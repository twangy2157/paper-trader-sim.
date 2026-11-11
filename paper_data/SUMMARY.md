# Paper trader summary

SIMULATION ONLY. No real trades.

Updated 2026-11-11T21:20:12Z. Bankroll cash (research-selected trades): 456.400154541351. Open positions: 17. Pools on watchlist: 56.

| group | n | win | avg | CI | P&L $ |
|---|---|---|---|---|---|
| research-picked | 16 | 25% | -33.9% | -64 to -3 | -544 |
| momentum, not picked | 1793 | 12% | -64.9% | -68 to -62 | -116615 |
| all momentum | 1809 | 12% | -64.7% | -67 to -62 | -117159 |
| control | 2569 | 5% | -18.0% | -19 to -17 | -46543 |
| dip buy | 21 | 24% | -20.0% | -47 to 7 | -422 |
| proven pools | 86 | 36% | -28.6% | -40 to -18 | -2469 |

What-if exit rules on the SAME trades. Cells: avg return (trades, win rate).

| exit rule | momentum | control | dip | proven |
|---|---|---|---|---|
| base_sl30_tp100 | -65% (1788, 12%) | -18% (2569, 5%) | -20% (21, 24%) | -29% (86, 36%) |
| wide_sl50_tp100 | -65% (1788, 13%) | -18% (2569, 6%) | -24% (21, 29%) | -30% (86, 36%) |
| sl30_tp50 | -66% (1788, 15%) | -18% (2569, 6%) | -29% (21, 24%) | -30% (86, 36%) |
| sl50_tp50 | -66% (1788, 16%) | -18% (2569, 6%) | -33% (21, 29%) | -31% (86, 36%) |
| no_stop_tp100 | -65% (1788, 14%) | -19% (2569, 6%) | -20% (21, 29%) | -30% (86, 36%) |

Verdict: NOT ENOUGH DATA (need 30+ closed filter=1 trades and a CI above zero before believing anything).

Pools seen: 64694. Outcomes:

- missed_window: 42766
- low_liquidity: 10402
- proven_liquidity_gone: 5008
- no_momentum: 2619
- research_failed: 1803
- proven_low_volume: 1002
- simulated failed buy: 820
- proven_price_collapsed_or_parabolic: 113
- proven: 87
- proven_no_uptrend: 37
- dip: 21
- research_passed: 16

Warning: 545 judged pools had an unreadable mint/freeze value. Check mint_raw / freeze_raw in candidates.csv; the parsing may need fixing.
