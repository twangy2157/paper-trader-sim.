# Paper trader summary

SIMULATION ONLY. No real trades.

Updated 2026-11-11T07:25:45Z. Bankroll cash (research-selected trades): 456.400154541351. Open positions: 9. Pools on watchlist: 43.

| group | n | win | avg | CI | P&L $ |
|---|---|---|---|---|---|
| research-picked | 16 | 25% | -33.9% | -64 to -3 | -544 |
| momentum, not picked | 1685 | 12% | -65.0% | -68 to -62 | -109650 |
| all momentum | 1701 | 12% | -64.7% | -67 to -62 | -110194 |
| control | 2440 | 5% | -18.0% | -19 to -17 | -44107 |
| dip buy | 20 | 25% | -16.1% | -42 to 10 | -323 |
| proven pools | 80 | 36% | -26.2% | -37 to -15 | -2106 |

What-if exit rules on the SAME trades. Cells: avg return (trades, win rate).

| exit rule | momentum | control | dip | proven |
|---|---|---|---|---|
| base_sl30_tp100 | -65% (1680, 12%) | -18% (2440, 5%) | -16% (20, 25%) | -26% (80, 36%) |
| wide_sl50_tp100 | -65% (1680, 13%) | -18% (2440, 5%) | -20% (20, 30%) | -28% (80, 36%) |
| sl30_tp50 | -66% (1680, 15%) | -18% (2440, 6%) | -26% (20, 25%) | -27% (80, 36%) |
| sl50_tp50 | -66% (1680, 16%) | -18% (2440, 6%) | -30% (20, 30%) | -29% (80, 36%) |
| no_stop_tp100 | -65% (1680, 14%) | -19% (2440, 5%) | -17% (20, 30%) | -28% (80, 36%) |

Verdict: NOT ENOUGH DATA (need 30+ closed filter=1 trades and a CI above zero before believing anything).

Pools seen: 61006. Outcomes:

- missed_window: 40382
- low_liquidity: 9793
- proven_liquidity_gone: 4649
- no_momentum: 2489
- research_failed: 1687
- proven_low_volume: 966
- simulated failed buy: 780
- proven_price_collapsed_or_parabolic: 105
- proven: 82
- proven_no_uptrend: 37
- dip: 20
- research_passed: 16

Warning: 522 judged pools had an unreadable mint/freeze value. Check mint_raw / freeze_raw in candidates.csv; the parsing may need fixing.
