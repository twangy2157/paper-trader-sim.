# Paper trader summary

SIMULATION ONLY. No real trades.

Updated 2026-11-27T13:20:12Z. Bankroll cash (research-selected trades): 513.2029228559132. Open positions: 13. Pools on watchlist: 56.

| group | n | win | avg | CI | P&L $ |
|---|---|---|---|---|---|
| research-picked | 24 | 33% | -20.1% | -46 to 6 | -487 |
| momentum, not picked | 3964 | 12% | -65.2% | -67 to -63 | -258747 |
| all momentum | 3988 | 12% | -64.9% | -67 to -63 | -259234 |
| control | 4764 | 6% | -19.3% | -20 to -18 | -92473 |
| dip buy | 47 | 28% | -12.8% | -30 to 4 | -606 |
| proven pools | 137 | 32% | -31.5% | -40 to -23 | -4326 |

What-if exit rules on the SAME trades. Cells: avg return (trades, win rate).

| exit rule | momentum | control | dip | proven |
|---|---|---|---|---|
| base_sl30_tp100 | -65% (3967, 12%) | -19% (4764, 6%) | -13% (47, 28%) | -31% (137, 32%) |
| wide_sl50_tp100 | -65% (3967, 13%) | -20% (4764, 6%) | -13% (47, 32%) | -33% (137, 32%) |
| sl30_tp50 | -67% (3967, 14%) | -19% (4764, 7%) | -17% (47, 34%) | -32% (137, 33%) |
| sl50_tp50 | -67% (3967, 15%) | -20% (4764, 7%) | -18% (47, 38%) | -33% (137, 33%) |
| no_stop_tp100 | -65% (3967, 14%) | -20% (4764, 7%) | -12% (47, 32%) | -33% (137, 32%) |

Verdict: NOT ENOUGH DATA (need 30+ closed filter=1 trades and a CI above zero before believing anything).

Pools seen: 127039. Outcomes:

- missed_window: 81725
- low_liquidity: 21947
- proven_liquidity_gone: 10883
- no_momentum: 4811
- research_failed: 3969
- simulated failed buy: 1625
- proven_low_volume: 1621
- proven_price_collapsed_or_parabolic: 171
- proven: 142
- proven_no_uptrend: 74
- dip: 47
- research_passed: 24

Warning: 1004 judged pools had an unreadable mint/freeze value. Check mint_raw / freeze_raw in candidates.csv; the parsing may need fixing.
