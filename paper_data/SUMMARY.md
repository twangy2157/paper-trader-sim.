# Paper trader summary

SIMULATION ONLY. No real trades.

Updated 2026-11-28T10:13:46Z. Bankroll cash (research-selected trades): 513.2029228559132. Open positions: 17. Pools on watchlist: 71.

| group | n | win | avg | CI | P&L $ |
|---|---|---|---|---|---|
| research-picked | 24 | 33% | -20.1% | -46 to 6 | -487 |
| momentum, not picked | 4040 | 12% | -64.9% | -67 to -63 | -262417 |
| all momentum | 4064 | 12% | -64.6% | -66 to -63 | -262903 |
| control | 4831 | 6% | -19.4% | -20 to -18 | -93991 |
| dip buy | 48 | 27% | -13.3% | -30 to 4 | -641 |
| proven pools | 143 | 31% | -32.0% | -41 to -24 | -4586 |

What-if exit rules on the SAME trades. Cells: avg return (trades, win rate).

| exit rule | momentum | control | dip | proven |
|---|---|---|---|---|
| base_sl30_tp100 | -65% (4043, 12%) | -19% (4831, 6%) | -13% (48, 27%) | -32% (143, 31%) |
| wide_sl50_tp100 | -64% (4043, 13%) | -20% (4831, 6%) | -13% (48, 31%) | -33% (143, 31%) |
| sl30_tp50 | -67% (4043, 14%) | -19% (4831, 7%) | -17% (48, 33%) | -32% (143, 31%) |
| sl50_tp50 | -66% (4043, 15%) | -20% (4831, 7%) | -18% (48, 38%) | -33% (143, 31%) |
| no_stop_tp100 | -64% (4043, 14%) | -20% (4831, 7%) | -12% (48, 31%) | -34% (143, 31%) |

Verdict: NOT ENOUGH DATA (need 30+ closed filter=1 trades and a CI above zero before believing anything).

Pools seen: 129104. Outcomes:

- missed_window: 82921
- low_liquidity: 22478
- proven_liquidity_gone: 11023
- no_momentum: 4886
- research_failed: 4045
- simulated failed buy: 1646
- proven_low_volume: 1642
- proven_price_collapsed_or_parabolic: 172
- proven: 144
- proven_no_uptrend: 75
- dip: 48
- research_passed: 24

Warning: 1018 judged pools had an unreadable mint/freeze value. Check mint_raw / freeze_raw in candidates.csv; the parsing may need fixing.
