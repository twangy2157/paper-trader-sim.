# Paper trader summary

SIMULATION ONLY. No real trades.

Updated 2026-11-14T11:29:20Z. Bankroll cash (research-selected trades): 456.400154541351. Open positions: 21. Pools on watchlist: 55.

| group | n | win | avg | CI | P&L $ |
|---|---|---|---|---|---|
| research-picked | 16 | 25% | -33.9% | -64 to -3 | -544 |
| momentum, not picked | 2304 | 12% | -64.9% | -67 to -62 | -149682 |
| all momentum | 2320 | 12% | -64.7% | -67 to -62 | -150225 |
| control | 3046 | 6% | -18.4% | -20 to -17 | -56246 |
| dip buy | 32 | 28% | -15.4% | -37 to 5 | -493 |
| proven pools | 107 | 35% | -33.0% | -43 to -23 | -3544 |

What-if exit rules on the SAME trades. Cells: avg return (trades, win rate).

| exit rule | momentum | control | dip | proven |
|---|---|---|---|---|
| base_sl30_tp100 | -65% (2299, 12%) | -18% (3046, 6%) | -15% (32, 28%) | -33% (107, 35%) |
| wide_sl50_tp100 | -65% (2299, 13%) | -19% (3046, 6%) | -18% (32, 31%) | -34% (107, 35%) |
| sl30_tp50 | -66% (2299, 15%) | -19% (3046, 7%) | -20% (32, 31%) | -33% (107, 36%) |
| sl50_tp50 | -66% (2299, 16%) | -19% (3046, 7%) | -23% (32, 34%) | -34% (107, 36%) |
| no_stop_tp100 | -65% (2299, 14%) | -19% (3046, 6%) | -16% (32, 31%) | -35% (107, 35%) |

Verdict: NOT ENOUGH DATA (need 30+ closed filter=1 trades and a CI above zero before believing anything).

Pools seen: 80462. Outcomes:

- missed_window: 52725
- low_liquidity: 13243
- proven_liquidity_gone: 6643
- no_momentum: 3103
- research_failed: 2312
- proven_low_volume: 1111
- simulated failed buy: 992
- proven_price_collapsed_or_parabolic: 130
- proven: 107
- proven_no_uptrend: 48
- dip: 32
- research_passed: 16

Warning: 641 judged pools had an unreadable mint/freeze value. Check mint_raw / freeze_raw in candidates.csv; the parsing may need fixing.
