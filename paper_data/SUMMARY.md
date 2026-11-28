# Paper trader summary

SIMULATION ONLY. No real trades.

Updated 2026-11-28T00:44:24Z. Bankroll cash (research-selected trades): 513.2029228559132. Open positions: 17. Pools on watchlist: 32.

| group | n | win | avg | CI | P&L $ |
|---|---|---|---|---|---|
| research-picked | 24 | 33% | -20.1% | -46 to 6 | -487 |
| momentum, not picked | 3986 | 12% | -65.0% | -67 to -63 | -259470 |
| all momentum | 4010 | 12% | -64.7% | -66 to -63 | -259956 |
| control | 4793 | 6% | -19.3% | -20 to -18 | -92810 |
| dip buy | 48 | 27% | -13.3% | -30 to 4 | -641 |
| proven pools | 142 | 31% | -31.9% | -41 to -23 | -4543 |

What-if exit rules on the SAME trades. Cells: avg return (trades, win rate).

| exit rule | momentum | control | dip | proven |
|---|---|---|---|---|
| base_sl30_tp100 | -65% (3989, 12%) | -19% (4793, 6%) | -13% (48, 27%) | -32% (142, 31%) |
| wide_sl50_tp100 | -65% (3989, 13%) | -20% (4793, 6%) | -13% (48, 31%) | -33% (142, 31%) |
| sl30_tp50 | -67% (3989, 14%) | -19% (4793, 7%) | -17% (48, 33%) | -32% (142, 32%) |
| sl50_tp50 | -66% (3989, 15%) | -20% (4793, 7%) | -18% (48, 38%) | -33% (142, 32%) |
| no_stop_tp100 | -65% (3989, 14%) | -20% (4793, 7%) | -12% (48, 31%) | -33% (142, 31%) |

Verdict: NOT ENOUGH DATA (need 30+ closed filter=1 trades and a CI above zero before believing anything).

Pools seen: 128011. Outcomes:

- missed_window: 82270
- low_liquidity: 22232
- proven_liquidity_gone: 10940
- no_momentum: 4840
- research_failed: 3999
- simulated failed buy: 1638
- proven_low_volume: 1632
- proven_price_collapsed_or_parabolic: 171
- proven: 143
- proven_no_uptrend: 74
- dip: 48
- research_passed: 24

Warning: 1009 judged pools had an unreadable mint/freeze value. Check mint_raw / freeze_raw in candidates.csv; the parsing may need fixing.
