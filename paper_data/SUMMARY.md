# Paper trader summary

SIMULATION ONLY. No real trades.

Updated 2026-11-28T08:48:12Z. Bankroll cash (research-selected trades): 513.2029228559132. Open positions: 32. Pools on watchlist: 61.

| group | n | win | avg | CI | P&L $ |
|---|---|---|---|---|---|
| research-picked | 24 | 33% | -20.1% | -46 to 6 | -487 |
| momentum, not picked | 4016 | 12% | -64.9% | -67 to -63 | -260930 |
| all momentum | 4040 | 12% | -64.6% | -66 to -63 | -261417 |
| control | 4817 | 6% | -19.3% | -20 to -18 | -93463 |
| dip buy | 48 | 27% | -13.3% | -30 to 4 | -641 |
| proven pools | 143 | 31% | -32.0% | -41 to -24 | -4586 |

What-if exit rules on the SAME trades. Cells: avg return (trades, win rate).

| exit rule | momentum | control | dip | proven |
|---|---|---|---|---|
| base_sl30_tp100 | -65% (4019, 12%) | -19% (4817, 6%) | -13% (48, 27%) | -32% (143, 31%) |
| wide_sl50_tp100 | -64% (4019, 13%) | -20% (4817, 6%) | -13% (48, 31%) | -33% (143, 31%) |
| sl30_tp50 | -67% (4019, 14%) | -19% (4817, 7%) | -17% (48, 33%) | -32% (143, 31%) |
| sl50_tp50 | -66% (4019, 15%) | -20% (4817, 7%) | -18% (48, 38%) | -33% (143, 31%) |
| no_stop_tp100 | -64% (4019, 14%) | -20% (4817, 6%) | -12% (48, 31%) | -34% (143, 31%) |

Verdict: NOT ENOUGH DATA (need 30+ closed filter=1 trades and a CI above zero before believing anything).

Pools seen: 128756. Outcomes:

- missed_window: 82693
- low_liquidity: 22411
- proven_liquidity_gone: 10997
- no_momentum: 4874
- research_failed: 4035
- simulated failed buy: 1644
- proven_low_volume: 1640
- proven_price_collapsed_or_parabolic: 172
- proven: 143
- proven_no_uptrend: 75
- dip: 48
- research_passed: 24

Warning: 1014 judged pools had an unreadable mint/freeze value. Check mint_raw / freeze_raw in candidates.csv; the parsing may need fixing.
