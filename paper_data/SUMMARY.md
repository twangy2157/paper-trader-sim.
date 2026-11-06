# Paper trader summary

SIMULATION ONLY. No real trades.

Updated 2026-11-06T09:38:09Z. Bankroll cash (research-selected trades): 649.8381952860861. Open positions: 14. Pools on watchlist: 48.

| group | n | win | avg | CI | P&L $ |
|---|---|---|---|---|---|
| research-picked | 9 | 22% | -38.7% | -74 to -0 | -350 |
| momentum, not picked | 827 | 14% | -58.9% | -63 to -55 | -48824 |
| all momentum | 836 | 14% | -58.7% | -63 to -55 | -49174 |
| control | 978 | 7% | -20.0% | -22 to -18 | -19692 |
| dip buy | 8 | 12% | -36.3% | -72 to 3 | -290 |
| proven pools | 41 | 46% | -14.7% | -30 to 0 | -607 |

What-if exit rules on the SAME trades. Cells: avg return (trades, win rate).

| exit rule | momentum | control | dip | proven |
|---|---|---|---|---|
| base_sl30_tp100 | -59% (815, 14%) | -20% (978, 7%) | -36% (8, 12%) | -15% (41, 46%) |
| wide_sl50_tp100 | -59% (815, 16%) | -21% (978, 7%) | -40% (8, 12%) | -15% (41, 46%) |
| sl30_tp50 | -61% (815, 17%) | -20% (978, 8%) | -40% (8, 12%) | -17% (41, 46%) |
| sl50_tp50 | -60% (815, 19%) | -21% (978, 8%) | -44% (8, 12%) | -17% (41, 46%) |
| no_stop_tp100 | -59% (815, 17%) | -21% (978, 7%) | -36% (8, 12%) | -15% (41, 46%) |

Verdict: NOT ENOUGH DATA (need 30+ closed filter=1 trades and a CI above zero before believing anything).

Pools seen: 29021. Outcomes:

- missed_window: 18901
- low_liquidity: 5289
- proven_liquidity_gone: 2210
- no_momentum: 1031
- research_failed: 832
- simulated failed buy: 342
- proven_low_volume: 282
- proven_price_collapsed_or_parabolic: 54
- proven: 41
- proven_no_uptrend: 22
- research_passed: 9
- dip: 8

Warning: 219 judged pools had an unreadable mint/freeze value. Check mint_raw / freeze_raw in candidates.csv; the parsing may need fixing.
