# Paper trader summary

SIMULATION ONLY. No real trades.

Updated 2026-11-28T02:20:10Z. Bankroll cash (research-selected trades): 513.2029228559132. Open positions: 17. Pools on watchlist: 55.

| group | n | win | avg | CI | P&L $ |
|---|---|---|---|---|---|
| research-picked | 24 | 33% | -20.1% | -46 to 6 | -487 |
| momentum, not picked | 4004 | 12% | -64.8% | -67 to -63 | -260029 |
| all momentum | 4028 | 12% | -64.6% | -66 to -63 | -260516 |
| control | 4803 | 6% | -19.3% | -20 to -18 | -92974 |
| dip buy | 48 | 27% | -13.3% | -30 to 4 | -641 |
| proven pools | 142 | 31% | -31.9% | -41 to -23 | -4543 |

What-if exit rules on the SAME trades. Cells: avg return (trades, win rate).

| exit rule | momentum | control | dip | proven |
|---|---|---|---|---|
| base_sl30_tp100 | -65% (4007, 12%) | -19% (4803, 6%) | -13% (48, 27%) | -32% (142, 31%) |
| wide_sl50_tp100 | -64% (4007, 13%) | -20% (4803, 6%) | -13% (48, 31%) | -33% (142, 31%) |
| sl30_tp50 | -67% (4007, 14%) | -19% (4803, 7%) | -17% (48, 33%) | -32% (142, 32%) |
| sl50_tp50 | -66% (4007, 15%) | -20% (4803, 7%) | -18% (48, 38%) | -33% (142, 32%) |
| no_stop_tp100 | -64% (4007, 14%) | -20% (4803, 7%) | -12% (48, 31%) | -33% (142, 31%) |

Verdict: NOT ENOUGH DATA (need 30+ closed filter=1 trades and a CI above zero before believing anything).

Pools seen: 128385. Outcomes:

- missed_window: 82481
- low_liquidity: 22314
- proven_liquidity_gone: 10983
- no_momentum: 4856
- research_failed: 4011
- simulated failed buy: 1640
- proven_low_volume: 1639
- proven_price_collapsed_or_parabolic: 171
- proven: 143
- proven_no_uptrend: 75
- dip: 48
- research_passed: 24

Warning: 1010 judged pools had an unreadable mint/freeze value. Check mint_raw / freeze_raw in candidates.csv; the parsing may need fixing.
