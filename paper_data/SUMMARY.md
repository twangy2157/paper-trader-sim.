# Paper trader summary

SIMULATION ONLY. No real trades.

Updated 2026-11-05T21:19:30Z. Bankroll cash (research-selected trades): 749.6403049524637. Open positions: 20. Pools on watchlist: 45.

| group | n | win | avg | CI | P&L $ |
|---|---|---|---|---|---|
| research-picked | 8 | 25% | -31.0% | -68 to 8 | -250 |
| momentum, not picked | 724 | 14% | -57.3% | -62 to -53 | -41563 |
| all momentum | 732 | 14% | -57.0% | -61 to -53 | -41814 |
| control | 865 | 7% | -19.2% | -22 to -17 | -16725 |
| dip buy | 7 | 14% | -27.3% | -65 to 10 | -191 |
| proven pools | 39 | 44% | -15.7% | -33 to 0 | -615 |

What-if exit rules on the SAME trades. Cells: avg return (trades, win rate).

| exit rule | momentum | control | dip | proven |
|---|---|---|---|---|
| base_sl30_tp100 | -58% (711, 15%) | -19% (865, 7%) | -27% (7, 14%) | -16% (39, 44%) |
| wide_sl50_tp100 | -57% (711, 16%) | -20% (865, 8%) | -32% (7, 14%) | -16% (39, 44%) |
| sl30_tp50 | -59% (711, 18%) | -20% (865, 8%) | -32% (7, 14%) | -18% (39, 44%) |
| sl50_tp50 | -58% (711, 20%) | -20% (865, 9%) | -36% (7, 14%) | -18% (39, 44%) |
| no_stop_tp100 | -57% (711, 17%) | -20% (865, 8%) | -27% (7, 14%) | -16% (39, 44%) |

Verdict: NOT ENOUGH DATA (need 30+ closed filter=1 trades and a CI above zero before believing anything).

Pools seen: 25728. Outcomes:

- missed_window: 16807
- low_liquidity: 4704
- proven_liquidity_gone: 1893
- no_momentum: 919
- research_failed: 733
- simulated failed buy: 290
- proven_low_volume: 255
- proven_price_collapsed_or_parabolic: 50
- proven: 40
- proven_no_uptrend: 22
- research_passed: 8
- dip: 7

Warning: 188 judged pools had an unreadable mint/freeze value. Check mint_raw / freeze_raw in candidates.csv; the parsing may need fixing.
