# Paper trader summary

SIMULATION ONLY. No real trades.

Updated 2026-11-27T01:32:12Z. Bankroll cash (research-selected trades): 513.2029228559132. Open positions: 25. Pools on watchlist: 62.

| group | n | win | avg | CI | P&L $ |
|---|---|---|---|---|---|
| research-picked | 24 | 33% | -20.1% | -46 to 6 | -487 |
| momentum, not picked | 3900 | 12% | -65.6% | -67 to -64 | -256120 |
| all momentum | 3924 | 12% | -65.3% | -67 to -63 | -256607 |
| control | 4677 | 6% | -19.4% | -20 to -18 | -91118 |
| dip buy | 47 | 28% | -12.8% | -30 to 4 | -606 |
| proven pools | 135 | 33% | -31.2% | -40 to -23 | -4223 |

What-if exit rules on the SAME trades. Cells: avg return (trades, win rate).

| exit rule | momentum | control | dip | proven |
|---|---|---|---|---|
| base_sl30_tp100 | -65% (3903, 12%) | -19% (4677, 6%) | -13% (47, 28%) | -31% (135, 33%) |
| wide_sl50_tp100 | -65% (3903, 13%) | -20% (4677, 6%) | -13% (47, 32%) | -32% (135, 33%) |
| sl30_tp50 | -67% (3903, 14%) | -19% (4677, 7%) | -17% (47, 34%) | -31% (135, 33%) |
| sl50_tp50 | -67% (3903, 15%) | -20% (4677, 7%) | -18% (47, 38%) | -32% (135, 33%) |
| no_stop_tp100 | -65% (3903, 14%) | -20% (4677, 7%) | -12% (47, 32%) | -33% (135, 33%) |

Verdict: NOT ENOUGH DATA (need 30+ closed filter=1 trades and a CI above zero before believing anything).

Pools seen: 125448. Outcomes:

- missed_window: 80739
- low_liquidity: 21655
- proven_liquidity_gone: 10760
- no_momentum: 4739
- research_failed: 3907
- simulated failed buy: 1608
- proven_low_volume: 1596
- proven_price_collapsed_or_parabolic: 169
- proven: 135
- proven_no_uptrend: 69
- dip: 47
- research_passed: 24

Warning: 993 judged pools had an unreadable mint/freeze value. Check mint_raw / freeze_raw in candidates.csv; the parsing may need fixing.
