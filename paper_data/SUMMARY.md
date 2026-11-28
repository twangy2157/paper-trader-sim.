# Paper trader summary

SIMULATION ONLY. No real trades.

Updated 2026-11-28T09:20:12Z. Bankroll cash (research-selected trades): 513.2029228559132. Open positions: 23. Pools on watchlist: 61.

| group | n | win | avg | CI | P&L $ |
|---|---|---|---|---|---|
| research-picked | 24 | 33% | -20.1% | -46 to 6 | -487 |
| momentum, not picked | 4027 | 12% | -64.9% | -67 to -63 | -261557 |
| all momentum | 4051 | 12% | -64.6% | -66 to -63 | -262044 |
| control | 4823 | 6% | -19.3% | -20 to -18 | -93616 |
| dip buy | 48 | 27% | -13.3% | -30 to 4 | -641 |
| proven pools | 143 | 31% | -32.0% | -41 to -24 | -4586 |

What-if exit rules on the SAME trades. Cells: avg return (trades, win rate).

| exit rule | momentum | control | dip | proven |
|---|---|---|---|---|
| base_sl30_tp100 | -65% (4030, 12%) | -19% (4823, 6%) | -13% (48, 27%) | -32% (143, 31%) |
| wide_sl50_tp100 | -64% (4030, 13%) | -20% (4823, 6%) | -13% (48, 31%) | -33% (143, 31%) |
| sl30_tp50 | -67% (4030, 14%) | -19% (4823, 7%) | -17% (48, 33%) | -32% (143, 31%) |
| sl50_tp50 | -66% (4030, 15%) | -20% (4823, 7%) | -18% (48, 38%) | -33% (143, 31%) |
| no_stop_tp100 | -64% (4030, 14%) | -20% (4823, 7%) | -12% (48, 31%) | -34% (143, 31%) |

Verdict: NOT ENOUGH DATA (need 30+ closed filter=1 trades and a CI above zero before believing anything).

Pools seen: 128887. Outcomes:

- missed_window: 82785
- low_liquidity: 22441
- proven_liquidity_gone: 10997
- no_momentum: 4877
- research_failed: 4040
- simulated failed buy: 1645
- proven_low_volume: 1640
- proven_price_collapsed_or_parabolic: 172
- proven: 143
- proven_no_uptrend: 75
- dip: 48
- research_passed: 24

Warning: 1015 judged pools had an unreadable mint/freeze value. Check mint_raw / freeze_raw in candidates.csv; the parsing may need fixing.
