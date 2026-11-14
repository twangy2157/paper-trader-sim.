# Paper trader summary

SIMULATION ONLY. No real trades.

Updated 2026-11-14T01:04:10Z. Bankroll cash (research-selected trades): 456.400154541351. Open positions: 7. Pools on watchlist: 36.

| group | n | win | avg | CI | P&L $ |
|---|---|---|---|---|---|
| research-picked | 16 | 25% | -33.9% | -64 to -3 | -544 |
| momentum, not picked | 2219 | 12% | -64.4% | -67 to -62 | -143207 |
| all momentum | 2235 | 12% | -64.2% | -67 to -62 | -143750 |
| control | 2968 | 6% | -18.3% | -20 to -17 | -54566 |
| dip buy | 31 | 26% | -18.1% | -40 to 2 | -564 |
| proven pools | 107 | 35% | -33.0% | -43 to -23 | -3544 |

What-if exit rules on the SAME trades. Cells: avg return (trades, win rate).

| exit rule | momentum | control | dip | proven |
|---|---|---|---|---|
| base_sl30_tp100 | -64% (2214, 12%) | -18% (2968, 6%) | -18% (31, 26%) | -33% (107, 35%) |
| wide_sl50_tp100 | -65% (2214, 14%) | -19% (2968, 6%) | -21% (31, 29%) | -34% (107, 35%) |
| sl30_tp50 | -66% (2214, 15%) | -19% (2968, 6%) | -22% (31, 29%) | -33% (107, 36%) |
| sl50_tp50 | -66% (2214, 16%) | -19% (2968, 7%) | -25% (31, 32%) | -34% (107, 36%) |
| no_stop_tp100 | -64% (2214, 14%) | -19% (2968, 6%) | -19% (31, 29%) | -35% (107, 35%) |

Verdict: NOT ENOUGH DATA (need 30+ closed filter=1 trades and a CI above zero before believing anything).

Pools seen: 77830. Outcomes:

- missed_window: 51133
- low_liquidity: 12714
- proven_liquidity_gone: 6360
- no_momentum: 3015
- research_failed: 2222
- proven_low_volume: 1094
- simulated failed buy: 965
- proven_price_collapsed_or_parabolic: 126
- proven: 107
- proven_no_uptrend: 46
- dip: 32
- research_passed: 16

Warning: 624 judged pools had an unreadable mint/freeze value. Check mint_raw / freeze_raw in candidates.csv; the parsing may need fixing.
