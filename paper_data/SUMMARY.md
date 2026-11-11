# Paper trader summary

SIMULATION ONLY. No real trades.

Updated 2026-11-11T19:33:42Z. Bankroll cash (research-selected trades): 456.400154541351. Open positions: 9. Pools on watchlist: 69.

| group | n | win | avg | CI | P&L $ |
|---|---|---|---|---|---|
| research-picked | 16 | 25% | -33.9% | -64 to -3 | -544 |
| momentum, not picked | 1783 | 12% | -64.8% | -68 to -62 | -115768 |
| all momentum | 1799 | 12% | -64.6% | -67 to -62 | -116311 |
| control | 2559 | 5% | -18.0% | -19 to -17 | -46376 |
| dip buy | 21 | 24% | -20.0% | -47 to 7 | -422 |
| proven pools | 85 | 36% | -27.8% | -38 to -17 | -2368 |

What-if exit rules on the SAME trades. Cells: avg return (trades, win rate).

| exit rule | momentum | control | dip | proven |
|---|---|---|---|---|
| base_sl30_tp100 | -65% (1778, 12%) | -18% (2559, 5%) | -20% (21, 24%) | -28% (85, 36%) |
| wide_sl50_tp100 | -65% (1778, 13%) | -18% (2559, 6%) | -24% (21, 29%) | -29% (85, 36%) |
| sl30_tp50 | -66% (1778, 15%) | -18% (2559, 6%) | -29% (21, 24%) | -29% (85, 36%) |
| sl50_tp50 | -66% (1778, 16%) | -18% (2559, 6%) | -33% (21, 29%) | -30% (85, 36%) |
| no_stop_tp100 | -65% (1778, 14%) | -19% (2559, 6%) | -20% (21, 29%) | -29% (85, 36%) |

Verdict: NOT ENOUGH DATA (need 30+ closed filter=1 trades and a CI above zero before believing anything).

Pools seen: 64196. Outcomes:

- missed_window: 42449
- low_liquidity: 10307
- proven_liquidity_gone: 4971
- no_momentum: 2607
- research_failed: 1786
- proven_low_volume: 992
- simulated failed buy: 814
- proven_price_collapsed_or_parabolic: 109
- proven: 87
- proven_no_uptrend: 37
- dip: 21
- research_passed: 16

Warning: 543 judged pools had an unreadable mint/freeze value. Check mint_raw / freeze_raw in candidates.csv; the parsing may need fixing.
