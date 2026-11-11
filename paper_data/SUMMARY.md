# Paper trader summary

SIMULATION ONLY. No real trades.

Updated 2026-11-11T23:36:31Z. Bankroll cash (research-selected trades): 456.400154541351. Open positions: 24. Pools on watchlist: 63.

| group | n | win | avg | CI | P&L $ |
|---|---|---|---|---|---|
| research-picked | 16 | 25% | -33.9% | -64 to -3 | -544 |
| momentum, not picked | 1813 | 12% | -64.7% | -67 to -62 | -117438 |
| all momentum | 1829 | 12% | -64.4% | -67 to -62 | -117981 |
| control | 2591 | 5% | -18.0% | -19 to -17 | -46824 |
| dip buy | 21 | 24% | -20.0% | -47 to 7 | -422 |
| proven pools | 87 | 36% | -28.3% | -39 to -18 | -2474 |

What-if exit rules on the SAME trades. Cells: avg return (trades, win rate).

| exit rule | momentum | control | dip | proven |
|---|---|---|---|---|
| base_sl30_tp100 | -65% (1808, 12%) | -18% (2591, 5%) | -20% (21, 24%) | -28% (87, 36%) |
| wide_sl50_tp100 | -65% (1808, 13%) | -18% (2591, 6%) | -24% (21, 29%) | -30% (87, 36%) |
| sl30_tp50 | -66% (1808, 15%) | -18% (2591, 6%) | -29% (21, 24%) | -29% (87, 36%) |
| sl50_tp50 | -66% (1808, 16%) | -18% (2591, 6%) | -33% (21, 29%) | -31% (87, 36%) |
| no_stop_tp100 | -65% (1808, 14%) | -19% (2591, 6%) | -20% (21, 29%) | -30% (87, 36%) |

Verdict: NOT ENOUGH DATA (need 30+ closed filter=1 trades and a CI above zero before believing anything).

Pools seen: 65385. Outcomes:

- missed_window: 43234
- low_liquidity: 10505
- proven_liquidity_gone: 5070
- no_momentum: 2649
- research_failed: 1822
- proven_low_volume: 1006
- simulated failed buy: 823
- proven_price_collapsed_or_parabolic: 114
- proven: 88
- proven_no_uptrend: 37
- dip: 21
- research_passed: 16

Warning: 548 judged pools had an unreadable mint/freeze value. Check mint_raw / freeze_raw in candidates.csv; the parsing may need fixing.
