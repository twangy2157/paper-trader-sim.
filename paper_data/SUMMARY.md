# Paper trader summary

SIMULATION ONLY. No real trades.

Updated 2026-11-27T08:35:12Z. Bankroll cash (research-selected trades): 513.2029228559132. Open positions: 20. Pools on watchlist: 42.

| group | n | win | avg | CI | P&L $ |
|---|---|---|---|---|---|
| research-picked | 24 | 33% | -20.1% | -46 to 6 | -487 |
| momentum, not picked | 3919 | 12% | -65.5% | -67 to -64 | -256916 |
| all momentum | 3943 | 12% | -65.2% | -67 to -63 | -257403 |
| control | 4706 | 6% | -19.4% | -20 to -18 | -91741 |
| dip buy | 47 | 28% | -12.8% | -30 to 4 | -606 |
| proven pools | 135 | 33% | -31.2% | -40 to -23 | -4223 |

What-if exit rules on the SAME trades. Cells: avg return (trades, win rate).

| exit rule | momentum | control | dip | proven |
|---|---|---|---|---|
| base_sl30_tp100 | -65% (3922, 12%) | -19% (4706, 6%) | -13% (47, 28%) | -31% (135, 33%) |
| wide_sl50_tp100 | -65% (3922, 13%) | -20% (4706, 6%) | -13% (47, 32%) | -32% (135, 33%) |
| sl30_tp50 | -67% (3922, 14%) | -20% (4706, 7%) | -17% (47, 34%) | -31% (135, 33%) |
| sl50_tp50 | -67% (3922, 15%) | -20% (4706, 7%) | -18% (47, 38%) | -32% (135, 33%) |
| no_stop_tp100 | -65% (3922, 14%) | -20% (4706, 7%) | -12% (47, 32%) | -33% (135, 33%) |

Verdict: NOT ENOUGH DATA (need 30+ closed filter=1 trades and a CI above zero before believing anything).

Pools seen: 126008. Outcomes:

- missed_window: 81116
- low_liquidity: 21737
- proven_liquidity_gone: 10803
- no_momentum: 4758
- research_failed: 3931
- simulated failed buy: 1614
- proven_low_volume: 1605
- proven_price_collapsed_or_parabolic: 169
- proven: 135
- proven_no_uptrend: 69
- dip: 47
- research_passed: 24

Warning: 997 judged pools had an unreadable mint/freeze value. Check mint_raw / freeze_raw in candidates.csv; the parsing may need fixing.
