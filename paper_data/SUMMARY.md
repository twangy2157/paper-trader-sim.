# Paper trader summary

SIMULATION ONLY. No real trades.

Updated 2026-11-27T12:17:00Z. Bankroll cash (research-selected trades): 513.2029228559132. Open positions: 30. Pools on watchlist: 31.

| group | n | win | avg | CI | P&L $ |
|---|---|---|---|---|---|
| research-picked | 24 | 33% | -20.1% | -46 to 6 | -487 |
| momentum, not picked | 3954 | 12% | -65.3% | -67 to -64 | -258551 |
| all momentum | 3978 | 12% | -65.0% | -67 to -63 | -259037 |
| control | 4748 | 6% | -19.3% | -20 to -18 | -91935 |
| dip buy | 47 | 28% | -12.8% | -30 to 4 | -606 |
| proven pools | 135 | 33% | -31.2% | -40 to -23 | -4223 |

What-if exit rules on the SAME trades. Cells: avg return (trades, win rate).

| exit rule | momentum | control | dip | proven |
|---|---|---|---|---|
| base_sl30_tp100 | -65% (3957, 12%) | -19% (4748, 6%) | -13% (47, 28%) | -31% (135, 33%) |
| wide_sl50_tp100 | -65% (3957, 13%) | -20% (4748, 6%) | -13% (47, 32%) | -32% (135, 33%) |
| sl30_tp50 | -67% (3957, 14%) | -19% (4748, 7%) | -17% (47, 34%) | -31% (135, 33%) |
| sl50_tp50 | -67% (3957, 15%) | -20% (4748, 7%) | -18% (47, 38%) | -32% (135, 33%) |
| no_stop_tp100 | -65% (3957, 14%) | -20% (4748, 7%) | -12% (47, 32%) | -33% (135, 33%) |

Verdict: NOT ENOUGH DATA (need 30+ closed filter=1 trades and a CI above zero before believing anything).

Pools seen: 126807. Outcomes:

- missed_window: 81577
- low_liquidity: 21909
- proven_liquidity_gone: 10858
- no_momentum: 4808
- research_failed: 3964
- simulated failed buy: 1624
- proven_low_volume: 1612
- proven_price_collapsed_or_parabolic: 171
- proven: 139
- proven_no_uptrend: 74
- dip: 47
- research_passed: 24

Warning: 1004 judged pools had an unreadable mint/freeze value. Check mint_raw / freeze_raw in candidates.csv; the parsing may need fixing.
