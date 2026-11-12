# Paper trader summary

SIMULATION ONLY. No real trades.

Updated 2026-11-12T09:48:53Z. Bankroll cash (research-selected trades): 456.400154541351. Open positions: 25. Pools on watchlist: 61.

| group | n | win | avg | CI | P&L $ |
|---|---|---|---|---|---|
| research-picked | 16 | 25% | -33.9% | -64 to -3 | -544 |
| momentum, not picked | 1903 | 12% | -64.7% | -67 to -62 | -123209 |
| all momentum | 1919 | 12% | -64.4% | -67 to -62 | -123753 |
| control | 2669 | 6% | -18.1% | -19 to -17 | -48436 |
| dip buy | 27 | 26% | -19.9% | -44 to 4 | -539 |
| proven pools | 91 | 34% | -30.2% | -41 to -20 | -2754 |

What-if exit rules on the SAME trades. Cells: avg return (trades, win rate).

| exit rule | momentum | control | dip | proven |
|---|---|---|---|---|
| base_sl30_tp100 | -65% (1898, 12%) | -18% (2669, 6%) | -20% (27, 26%) | -30% (91, 34%) |
| wide_sl50_tp100 | -65% (1898, 13%) | -18% (2669, 6%) | -23% (27, 30%) | -32% (91, 34%) |
| sl30_tp50 | -66% (1898, 15%) | -18% (2669, 6%) | -25% (27, 30%) | -31% (91, 34%) |
| sl50_tp50 | -66% (1898, 16%) | -19% (2669, 7%) | -28% (27, 33%) | -33% (91, 34%) |
| no_stop_tp100 | -65% (1898, 14%) | -19% (2669, 6%) | -21% (27, 30%) | -33% (91, 34%) |

Verdict: NOT ENOUGH DATA (need 30+ closed filter=1 trades and a CI above zero before believing anything).

Pools seen: 67813. Outcomes:

- missed_window: 44773
- low_liquidity: 10905
- proven_liquidity_gone: 5328
- no_momentum: 2728
- research_failed: 1913
- proven_low_volume: 1028
- simulated failed buy: 848
- proven_price_collapsed_or_parabolic: 117
- proven: 91
- proven_no_uptrend: 39
- dip: 27
- research_passed: 16

Warning: 562 judged pools had an unreadable mint/freeze value. Check mint_raw / freeze_raw in candidates.csv; the parsing may need fixing.
