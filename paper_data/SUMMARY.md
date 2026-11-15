# Paper trader summary

SIMULATION ONLY. No real trades.

Updated 2026-11-15T14:41:54Z. Bankroll cash (research-selected trades): 456.400154541351. Open positions: 20. Pools on watchlist: 62.

| group | n | win | avg | CI | P&L $ |
|---|---|---|---|---|---|
| research-picked | 16 | 25% | -33.9% | -64 to -3 | -544 |
| momentum, not picked | 2535 | 12% | -65.8% | -68 to -63 | -167039 |
| all momentum | 2551 | 12% | -65.6% | -68 to -63 | -167582 |
| control | 3240 | 6% | -18.7% | -20 to -17 | -60965 |
| dip buy | 34 | 29% | -11.9% | -32 to 8 | -406 |
| proven pools | 112 | 34% | -33.2% | -43 to -23 | -3725 |

What-if exit rules on the SAME trades. Cells: avg return (trades, win rate).

| exit rule | momentum | control | dip | proven |
|---|---|---|---|---|
| base_sl30_tp100 | -66% (2530, 12%) | -19% (3240, 6%) | -12% (34, 29%) | -33% (112, 34%) |
| wide_sl50_tp100 | -66% (2530, 13%) | -19% (3240, 6%) | -15% (34, 32%) | -34% (112, 34%) |
| sl30_tp50 | -67% (2530, 14%) | -19% (3240, 7%) | -18% (34, 32%) | -33% (112, 35%) |
| sl50_tp50 | -67% (2530, 16%) | -19% (3240, 7%) | -21% (34, 35%) | -34% (112, 35%) |
| no_stop_tp100 | -66% (2530, 14%) | -19% (3240, 6%) | -13% (34, 32%) | -35% (112, 34%) |

Verdict: NOT ENOUGH DATA (need 30+ closed filter=1 trades and a CI above zero before believing anything).

Pools seen: 88090. Outcomes:

- missed_window: 57817
- low_liquidity: 14469
- proven_liquidity_gone: 7363
- no_momentum: 3295
- research_failed: 2544
- proven_low_volume: 1164
- simulated failed buy: 1087
- proven_price_collapsed_or_parabolic: 136
- proven: 112
- proven_no_uptrend: 53
- dip: 34
- research_passed: 16

Warning: 687 judged pools had an unreadable mint/freeze value. Check mint_raw / freeze_raw in candidates.csv; the parsing may need fixing.
