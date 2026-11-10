# Paper trader summary

SIMULATION ONLY. No real trades.

Updated 2026-11-10T21:05:33Z. Bankroll cash (research-selected trades): 456.400154541351. Open positions: 34. Pools on watchlist: 61.

| group | n | win | avg | CI | P&L $ |
|---|---|---|---|---|---|
| research-picked | 16 | 25% | -33.9% | -64 to -3 | -544 |
| momentum, not picked | 1606 | 12% | -64.6% | -67 to -62 | -103830 |
| all momentum | 1622 | 12% | -64.3% | -67 to -62 | -104374 |
| control | 2330 | 5% | -18.0% | -19 to -17 | -42155 |
| dip buy | 16 | 19% | -24.9% | -52 to 4 | -400 |
| proven pools | 78 | 37% | -26.4% | -38 to -15 | -2065 |

What-if exit rules on the SAME trades. Cells: avg return (trades, win rate).

| exit rule | momentum | control | dip | proven |
|---|---|---|---|---|
| base_sl30_tp100 | -65% (1601, 12%) | -18% (2330, 5%) | -25% (16, 19%) | -26% (78, 37%) |
| wide_sl50_tp100 | -64% (1601, 14%) | -18% (2330, 5%) | -31% (16, 19%) | -27% (78, 37%) |
| sl30_tp50 | -66% (1601, 15%) | -18% (2330, 6%) | -32% (16, 19%) | -28% (78, 37%) |
| sl50_tp50 | -65% (1601, 17%) | -18% (2330, 6%) | -38% (16, 19%) | -28% (78, 37%) |
| no_stop_tp100 | -64% (1601, 14%) | -19% (2330, 5%) | -27% (16, 19%) | -27% (78, 37%) |

Verdict: NOT ENOUGH DATA (need 30+ closed filter=1 trades and a CI above zero before believing anything).

Pools seen: 58644. Outcomes:

- missed_window: 38892
- low_liquidity: 9409
- proven_liquidity_gone: 4416
- no_momentum: 2395
- research_failed: 1617
- proven_low_volume: 919
- simulated failed buy: 746
- proven_price_collapsed_or_parabolic: 102
- proven: 79
- proven_no_uptrend: 36
- dip: 17
- research_passed: 16

Warning: 499 judged pools had an unreadable mint/freeze value. Check mint_raw / freeze_raw in candidates.csv; the parsing may need fixing.
