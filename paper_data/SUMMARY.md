# Paper trader summary

SIMULATION ONLY. No real trades.

Updated 2026-11-10T07:31:21Z. Bankroll cash (research-selected trades): 456.400154541351. Open positions: 3. Pools on watchlist: 39.

| group | n | win | avg | CI | P&L $ |
|---|---|---|---|---|---|
| research-picked | 16 | 25% | -33.9% | -64 to -3 | -544 |
| momentum, not picked | 1460 | 12% | -63.8% | -67 to -61 | -93254 |
| all momentum | 1476 | 12% | -63.5% | -66 to -60 | -93797 |
| control | 2152 | 5% | -17.9% | -19 to -16 | -38736 |
| dip buy | 15 | 13% | -32.7% | -58 to -8 | -491 |
| proven pools | 76 | 37% | -25.8% | -37 to -14 | -1965 |

What-if exit rules on the SAME trades. Cells: avg return (trades, win rate).

| exit rule | momentum | control | dip | proven |
|---|---|---|---|---|
| base_sl30_tp100 | -64% (1455, 12%) | -18% (2152, 5%) | -33% (15, 13%) | -26% (76, 37%) |
| wide_sl50_tp100 | -63% (1455, 14%) | -18% (2152, 5%) | -39% (15, 13%) | -27% (76, 37%) |
| sl30_tp50 | -65% (1455, 15%) | -18% (2152, 6%) | -37% (15, 13%) | -27% (76, 37%) |
| sl50_tp50 | -64% (1455, 17%) | -18% (2152, 6%) | -43% (15, 13%) | -28% (76, 37%) |
| no_stop_tp100 | -63% (1455, 15%) | -19% (2152, 5%) | -35% (15, 13%) | -27% (76, 37%) |

Verdict: NOT ENOUGH DATA (need 30+ closed filter=1 trades and a CI above zero before believing anything).

Pools seen: 54848. Outcomes:

- missed_window: 36583
- low_liquidity: 8735
- proven_liquidity_gone: 4087
- no_momentum: 2198
- research_failed: 1461
- proven_low_volume: 859
- simulated failed buy: 688
- proven_price_collapsed_or_parabolic: 97
- proven: 76
- proven_no_uptrend: 33
- research_passed: 16
- dip: 15

Warning: 466 judged pools had an unreadable mint/freeze value. Check mint_raw / freeze_raw in candidates.csv; the parsing may need fixing.
