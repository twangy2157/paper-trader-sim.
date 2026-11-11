# Paper trader summary

SIMULATION ONLY. No real trades.

Updated 2026-11-11T16:33:21Z. Bankroll cash (research-selected trades): 456.400154541351. Open positions: 19. Pools on watchlist: 53.

| group | n | win | avg | CI | P&L $ |
|---|---|---|---|---|---|
| research-picked | 16 | 25% | -33.9% | -64 to -3 | -544 |
| momentum, not picked | 1759 | 12% | -64.9% | -68 to -62 | -114330 |
| all momentum | 1775 | 12% | -64.6% | -67 to -62 | -114874 |
| control | 2522 | 5% | -17.9% | -19 to -17 | -45358 |
| dip buy | 21 | 24% | -20.0% | -47 to 7 | -422 |
| proven pools | 85 | 36% | -27.8% | -38 to -17 | -2368 |

What-if exit rules on the SAME trades. Cells: avg return (trades, win rate).

| exit rule | momentum | control | dip | proven |
|---|---|---|---|---|
| base_sl30_tp100 | -65% (1754, 12%) | -18% (2522, 5%) | -20% (21, 24%) | -28% (85, 36%) |
| wide_sl50_tp100 | -65% (1754, 13%) | -18% (2522, 6%) | -24% (21, 29%) | -29% (85, 36%) |
| sl30_tp50 | -66% (1754, 15%) | -18% (2522, 6%) | -29% (21, 24%) | -29% (85, 36%) |
| sl50_tp50 | -66% (1754, 16%) | -18% (2522, 7%) | -33% (21, 29%) | -30% (85, 36%) |
| no_stop_tp100 | -65% (1754, 14%) | -18% (2522, 6%) | -20% (21, 29%) | -29% (85, 36%) |

Verdict: NOT ENOUGH DATA (need 30+ closed filter=1 trades and a CI above zero before believing anything).

Pools seen: 63252. Outcomes:

- missed_window: 41757
- low_liquidity: 10203
- proven_liquidity_gone: 4897
- no_momentum: 2577
- research_failed: 1767
- proven_low_volume: 980
- simulated failed buy: 803
- proven_price_collapsed_or_parabolic: 109
- proven: 85
- proven_no_uptrend: 37
- dip: 21
- research_passed: 16

Warning: 537 judged pools had an unreadable mint/freeze value. Check mint_raw / freeze_raw in candidates.csv; the parsing may need fixing.
