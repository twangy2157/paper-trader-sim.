# Paper trader summary

SIMULATION ONLY. No real trades.

Updated 2026-11-27T01:21:36Z. Bankroll cash (research-selected trades): 513.2029228559132. Open positions: 29. Pools on watchlist: 50.

| group | n | win | avg | CI | P&L $ |
|---|---|---|---|---|---|
| research-picked | 24 | 33% | -20.1% | -46 to 6 | -487 |
| momentum, not picked | 3895 | 12% | -65.7% | -67 to -64 | -256095 |
| all momentum | 3919 | 12% | -65.4% | -67 to -64 | -256582 |
| control | 4676 | 6% | -19.4% | -21 to -18 | -91110 |
| dip buy | 47 | 28% | -12.8% | -30 to 4 | -606 |
| proven pools | 135 | 33% | -31.2% | -40 to -23 | -4223 |

What-if exit rules on the SAME trades. Cells: avg return (trades, win rate).

| exit rule | momentum | control | dip | proven |
|---|---|---|---|---|
| base_sl30_tp100 | -66% (3898, 12%) | -19% (4676, 6%) | -13% (47, 28%) | -31% (135, 33%) |
| wide_sl50_tp100 | -65% (3898, 13%) | -20% (4676, 6%) | -13% (47, 32%) | -32% (135, 33%) |
| sl30_tp50 | -67% (3898, 14%) | -20% (4676, 7%) | -17% (47, 34%) | -31% (135, 33%) |
| sl50_tp50 | -67% (3898, 15%) | -20% (4676, 7%) | -18% (47, 38%) | -32% (135, 33%) |
| no_stop_tp100 | -65% (3898, 14%) | -20% (4676, 7%) | -12% (47, 32%) | -33% (135, 33%) |

Verdict: NOT ENOUGH DATA (need 30+ closed filter=1 trades and a CI above zero before believing anything).

Pools seen: 125403. Outcomes:

- missed_window: 80708
- low_liquidity: 21650
- proven_liquidity_gone: 10753
- no_momentum: 4737
- research_failed: 3907
- simulated failed buy: 1608
- proven_low_volume: 1596
- proven_price_collapsed_or_parabolic: 169
- proven: 135
- proven_no_uptrend: 69
- dip: 47
- research_passed: 24

Warning: 993 judged pools had an unreadable mint/freeze value. Check mint_raw / freeze_raw in candidates.csv; the parsing may need fixing.
