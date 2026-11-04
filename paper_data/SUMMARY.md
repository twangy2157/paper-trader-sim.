# Paper trader summary

SIMULATION ONLY. No real trades.

Updated 2026-11-04T23:13:05Z. Bankroll cash (research-selected trades): 816.8065461812329. Open positions: 33. Pools on watchlist: 0.

| group | n | win | avg | CI | P&L $ |
|---|---|---|---|---|---|
| research-picked | 5 | 20% | -36.3% | - | -183 |
| momentum, not picked | 548 | 16% | -53.5% | -59 to -48 | -29351 |
| all momentum | 553 | 16% | -53.3% | -58 to -48 | -29534 |
| control | 661 | 8% | -18.5% | -21 to -16 | -12303 |
| dip buy | 4 | 25% | -13.1% | - | -52 |
| proven pools | 30 | 43% | -17.6% | -36 to -1 | -530 |

What-if exit rules on the SAME trades. Cells: avg return (trades, win rate).

| exit rule | momentum | control | dip | proven |
|---|---|---|---|---|
| base_sl30_tp100 | -54% (532, 16%) | -19% (661, 8%) | -13% (4, 25%) | -18% (30, 43%) |
| wide_sl50_tp100 | -54% (532, 18%) | -19% (661, 8%) | -13% (4, 25%) | -18% (30, 43%) |
| sl30_tp50 | -55% (532, 20%) | -19% (661, 8%) | -22% (4, 25%) | -19% (30, 43%) |
| sl50_tp50 | -55% (532, 23%) | -19% (661, 9%) | -22% (4, 25%) | -19% (30, 43%) |
| no_stop_tp100 | -53% (532, 19%) | -19% (661, 8%) | -13% (4, 25%) | -18% (30, 43%) |

Verdict: NOT ENOUGH DATA (need 30+ closed filter=1 trades and a CI above zero before believing anything).

Pools seen: 20246. Outcomes:

- missed_window: 13345
- low_liquidity: 3750
- proven_liquidity_gone: 1344
- no_momentum: 729
- research_failed: 555
- simulated failed buy: 229
- proven_low_volume: 193
- proven_price_collapsed_or_parabolic: 40
- proven: 32
- proven_no_uptrend: 20
- research_passed: 5
- dip: 4

Warning: 153 judged pools had an unreadable mint/freeze value. Check mint_raw / freeze_raw in candidates.csv; the parsing may need fixing.
