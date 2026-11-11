# Paper trader summary

SIMULATION ONLY. No real trades.

Updated 2026-11-11T20:26:42Z. Bankroll cash (research-selected trades): 456.400154541351. Open positions: 17. Pools on watchlist: 54.

| group | n | win | avg | CI | P&L $ |
|---|---|---|---|---|---|
| research-picked | 16 | 25% | -33.9% | -64 to -3 | -544 |
| momentum, not picked | 1785 | 12% | -64.9% | -68 to -62 | -115969 |
| all momentum | 1801 | 12% | -64.6% | -67 to -62 | -116513 |
| control | 2563 | 5% | -18.0% | -19 to -17 | -46404 |
| dip buy | 21 | 24% | -20.0% | -47 to 7 | -422 |
| proven pools | 86 | 36% | -28.6% | -40 to -18 | -2469 |

What-if exit rules on the SAME trades. Cells: avg return (trades, win rate).

| exit rule | momentum | control | dip | proven |
|---|---|---|---|---|
| base_sl30_tp100 | -65% (1780, 12%) | -18% (2563, 5%) | -20% (21, 24%) | -29% (86, 36%) |
| wide_sl50_tp100 | -65% (1780, 13%) | -18% (2563, 6%) | -24% (21, 29%) | -30% (86, 36%) |
| sl30_tp50 | -66% (1780, 15%) | -18% (2563, 6%) | -29% (21, 24%) | -30% (86, 36%) |
| sl50_tp50 | -66% (1780, 16%) | -18% (2563, 6%) | -33% (21, 29%) | -31% (86, 36%) |
| no_stop_tp100 | -65% (1780, 14%) | -19% (2563, 6%) | -20% (21, 29%) | -30% (86, 36%) |

Verdict: NOT ENOUGH DATA (need 30+ closed filter=1 trades and a CI above zero before believing anything).

Pools seen: 64443. Outcomes:

- missed_window: 42603
- low_liquidity: 10356
- proven_liquidity_gone: 4989
- no_momentum: 2614
- research_failed: 1794
- proven_low_volume: 995
- simulated failed buy: 819
- proven_price_collapsed_or_parabolic: 112
- proven: 87
- proven_no_uptrend: 37
- dip: 21
- research_passed: 16

Warning: 545 judged pools had an unreadable mint/freeze value. Check mint_raw / freeze_raw in candidates.csv; the parsing may need fixing.
