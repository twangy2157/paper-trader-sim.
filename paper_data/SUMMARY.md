# Paper trader summary

SIMULATION ONLY. No real trades.

Updated 2026-11-28T09:31:33Z. Bankroll cash (research-selected trades): 513.2029228559132. Open positions: 19. Pools on watchlist: 34.

| group | n | win | avg | CI | P&L $ |
|---|---|---|---|---|---|
| research-picked | 24 | 33% | -20.1% | -46 to 6 | -487 |
| momentum, not picked | 4031 | 12% | -64.9% | -67 to -63 | -261804 |
| all momentum | 4055 | 12% | -64.6% | -66 to -63 | -262291 |
| control | 4825 | 6% | -19.4% | -20 to -18 | -93817 |
| dip buy | 48 | 27% | -13.3% | -30 to 4 | -641 |
| proven pools | 143 | 31% | -32.0% | -41 to -24 | -4586 |

What-if exit rules on the SAME trades. Cells: avg return (trades, win rate).

| exit rule | momentum | control | dip | proven |
|---|---|---|---|---|
| base_sl30_tp100 | -65% (4034, 12%) | -19% (4825, 6%) | -13% (48, 27%) | -32% (143, 31%) |
| wide_sl50_tp100 | -64% (4034, 13%) | -20% (4825, 6%) | -13% (48, 31%) | -33% (143, 31%) |
| sl30_tp50 | -67% (4034, 14%) | -19% (4825, 7%) | -17% (48, 33%) | -32% (143, 31%) |
| sl50_tp50 | -66% (4034, 15%) | -20% (4825, 7%) | -18% (48, 38%) | -33% (143, 31%) |
| no_stop_tp100 | -64% (4034, 14%) | -20% (4825, 7%) | -12% (48, 31%) | -34% (143, 31%) |

Verdict: NOT ENOUGH DATA (need 30+ closed filter=1 trades and a CI above zero before believing anything).

Pools seen: 128940. Outcomes:

- missed_window: 82826
- low_liquidity: 22446
- proven_liquidity_gone: 11001
- no_momentum: 4878
- research_failed: 4041
- simulated failed buy: 1645
- proven_low_volume: 1641
- proven_price_collapsed_or_parabolic: 172
- proven: 143
- proven_no_uptrend: 75
- dip: 48
- research_passed: 24

Warning: 1016 judged pools had an unreadable mint/freeze value. Check mint_raw / freeze_raw in candidates.csv; the parsing may need fixing.
