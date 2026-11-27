# Paper trader summary

SIMULATION ONLY. No real trades.

Updated 2026-11-27T02:04:16Z. Bankroll cash (research-selected trades): 513.2029228559132. Open positions: 17. Pools on watchlist: 57.

| group | n | win | avg | CI | P&L $ |
|---|---|---|---|---|---|
| research-picked | 24 | 33% | -20.1% | -46 to 6 | -487 |
| momentum, not picked | 3904 | 12% | -65.5% | -67 to -64 | -256140 |
| all momentum | 3928 | 12% | -65.2% | -67 to -63 | -256626 |
| control | 4687 | 6% | -19.4% | -20 to -18 | -91344 |
| dip buy | 47 | 28% | -12.8% | -30 to 4 | -606 |
| proven pools | 135 | 33% | -31.2% | -40 to -23 | -4223 |

What-if exit rules on the SAME trades. Cells: avg return (trades, win rate).

| exit rule | momentum | control | dip | proven |
|---|---|---|---|---|
| base_sl30_tp100 | -65% (3907, 12%) | -19% (4687, 6%) | -13% (47, 28%) | -31% (135, 33%) |
| wide_sl50_tp100 | -65% (3907, 13%) | -20% (4687, 6%) | -13% (47, 32%) | -32% (135, 33%) |
| sl30_tp50 | -67% (3907, 14%) | -20% (4687, 7%) | -17% (47, 34%) | -31% (135, 33%) |
| sl50_tp50 | -67% (3907, 15%) | -20% (4687, 7%) | -18% (47, 38%) | -32% (135, 33%) |
| no_stop_tp100 | -65% (3907, 14%) | -20% (4687, 7%) | -12% (47, 32%) | -33% (135, 33%) |

Verdict: NOT ENOUGH DATA (need 30+ closed filter=1 trades and a CI above zero before believing anything).

Pools seen: 125610. Outcomes:

- missed_window: 80855
- low_liquidity: 21674
- proven_liquidity_gone: 10777
- no_momentum: 4741
- research_failed: 3911
- simulated failed buy: 1611
- proven_low_volume: 1597
- proven_price_collapsed_or_parabolic: 169
- proven: 135
- proven_no_uptrend: 69
- dip: 47
- research_passed: 24

Warning: 995 judged pools had an unreadable mint/freeze value. Check mint_raw / freeze_raw in candidates.csv; the parsing may need fixing.
