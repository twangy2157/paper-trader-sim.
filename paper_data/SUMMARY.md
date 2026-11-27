# Paper trader summary

SIMULATION ONLY. No real trades.

Updated 2026-11-27T12:38:11Z. Bankroll cash (research-selected trades): 513.2029228559132. Open positions: 24. Pools on watchlist: 49.

| group | n | win | avg | CI | P&L $ |
|---|---|---|---|---|---|
| research-picked | 24 | 33% | -20.1% | -46 to 6 | -487 |
| momentum, not picked | 3956 | 12% | -65.2% | -67 to -63 | -258412 |
| all momentum | 3980 | 12% | -65.0% | -67 to -63 | -258899 |
| control | 4756 | 6% | -19.3% | -20 to -18 | -92262 |
| dip buy | 47 | 28% | -12.8% | -30 to 4 | -606 |
| proven pools | 135 | 33% | -31.2% | -40 to -23 | -4223 |

What-if exit rules on the SAME trades. Cells: avg return (trades, win rate).

| exit rule | momentum | control | dip | proven |
|---|---|---|---|---|
| base_sl30_tp100 | -65% (3959, 12%) | -19% (4756, 6%) | -13% (47, 28%) | -31% (135, 33%) |
| wide_sl50_tp100 | -65% (3959, 13%) | -20% (4756, 6%) | -13% (47, 32%) | -32% (135, 33%) |
| sl30_tp50 | -67% (3959, 14%) | -19% (4756, 7%) | -17% (47, 34%) | -31% (135, 33%) |
| sl50_tp50 | -67% (3959, 15%) | -20% (4756, 7%) | -18% (47, 38%) | -32% (135, 33%) |
| no_stop_tp100 | -65% (3959, 14%) | -20% (4756, 7%) | -12% (47, 32%) | -33% (135, 33%) |

Verdict: NOT ENOUGH DATA (need 30+ closed filter=1 trades and a CI above zero before believing anything).

Pools seen: 126877. Outcomes:

- missed_window: 81618
- low_liquidity: 21921
- proven_liquidity_gone: 10868
- no_momentum: 4810
- research_failed: 3965
- simulated failed buy: 1624
- proven_low_volume: 1615
- proven_price_collapsed_or_parabolic: 171
- proven: 140
- proven_no_uptrend: 74
- dip: 47
- research_passed: 24

Warning: 1004 judged pools had an unreadable mint/freeze value. Check mint_raw / freeze_raw in candidates.csv; the parsing may need fixing.
