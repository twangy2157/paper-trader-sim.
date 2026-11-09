# Paper trader summary

SIMULATION ONLY. No real trades.

Updated 2026-11-09T03:05:30Z. Bankroll cash (research-selected trades): 456.400154541351. Open positions: 24. Pools on watchlist: 62.

| group | n | win | avg | CI | P&L $ |
|---|---|---|---|---|---|
| research-picked | 16 | 25% | -33.9% | -64 to -3 | -544 |
| momentum, not picked | 1248 | 12% | -64.1% | -68 to -61 | -80141 |
| all momentum | 1264 | 12% | -63.7% | -67 to -60 | -80684 |
| control | 1726 | 5% | -18.6% | -20 to -17 | -32302 |
| dip buy | 12 | 8% | -39.5% | -67 to -12 | -474 |
| proven pools | 60 | 43% | -17.2% | -29 to -5 | -1039 |

What-if exit rules on the SAME trades. Cells: avg return (trades, win rate).

| exit rule | momentum | control | dip | proven |
|---|---|---|---|---|
| base_sl30_tp100 | -64% (1243, 12%) | -19% (1726, 5%) | -39% (12, 8%) | -17% (60, 43%) |
| wide_sl50_tp100 | -64% (1243, 14%) | -19% (1726, 6%) | -47% (12, 8%) | -17% (60, 43%) |
| sl30_tp50 | -65% (1243, 15%) | -19% (1726, 6%) | -42% (12, 8%) | -19% (60, 43%) |
| sl50_tp50 | -65% (1243, 17%) | -19% (1726, 7%) | -49% (12, 8%) | -19% (60, 43%) |
| no_stop_tp100 | -64% (1243, 15%) | -19% (1726, 6%) | -44% (12, 8%) | -17% (60, 43%) |

Verdict: NOT ENOUGH DATA (need 30+ closed filter=1 trades and a CI above zero before believing anything).

Pools seen: 46574. Outcomes:

- missed_window: 30887
- low_liquidity: 7717
- proven_liquidity_gone: 3522
- no_momentum: 1788
- research_failed: 1254
- proven_low_volume: 650
- simulated failed buy: 562
- proven_price_collapsed_or_parabolic: 80
- proven: 60
- proven_no_uptrend: 26
- research_passed: 16
- dip: 12

Warning: 369 judged pools had an unreadable mint/freeze value. Check mint_raw / freeze_raw in candidates.csv; the parsing may need fixing.
