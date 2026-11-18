# Paper trader summary

SIMULATION ONLY. No real trades.

Updated 2026-11-18T18:59:45Z. Bankroll cash (research-selected trades): 549.3536238229275. Open positions: 9. Pools on watchlist: 64.

| group | n | win | avg | CI | P&L $ |
|---|---|---|---|---|---|
| research-picked | 17 | 29% | -26.4% | -58 to 8 | -451 |
| momentum, not picked | 3086 | 11% | -66.7% | -69 to -65 | -205977 |
| all momentum | 3103 | 11% | -66.4% | -68 to -65 | -206428 |
| control | 3821 | 6% | -19.1% | -20 to -18 | -73183 |
| dip buy | 41 | 27% | -12.0% | -29 to 6 | -494 |
| proven pools | 120 | 33% | -32.6% | -42 to -23 | -3923 |

What-if exit rules on the SAME trades. Cells: avg return (trades, win rate).

| exit rule | momentum | control | dip | proven |
|---|---|---|---|---|
| base_sl30_tp100 | -67% (3082, 11%) | -19% (3821, 6%) | -12% (41, 27%) | -33% (120, 33%) |
| wide_sl50_tp100 | -66% (3082, 13%) | -19% (3821, 6%) | -15% (41, 29%) | -34% (120, 33%) |
| sl30_tp50 | -68% (3082, 14%) | -19% (3821, 7%) | -18% (41, 29%) | -33% (120, 34%) |
| sl50_tp50 | -67% (3082, 15%) | -19% (3821, 7%) | -19% (41, 34%) | -34% (120, 34%) |
| no_stop_tp100 | -66% (3082, 13%) | -20% (3821, 7%) | -13% (41, 29%) | -35% (120, 33%) |

Verdict: NOT ENOUGH DATA (need 30+ closed filter=1 trades and a CI above zero before believing anything).

Pools seen: 102805. Outcomes:

- missed_window: 66885
- low_liquidity: 17097
- proven_liquidity_gone: 8837
- no_momentum: 3867
- research_failed: 3092
- proven_low_volume: 1345
- simulated failed buy: 1289
- proven_price_collapsed_or_parabolic: 153
- proven: 121
- proven_no_uptrend: 61
- dip: 41
- research_passed: 17

Warning: 816 judged pools had an unreadable mint/freeze value. Check mint_raw / freeze_raw in candidates.csv; the parsing may need fixing.
