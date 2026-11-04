# Paper trader summary

SIMULATION ONLY. No real trades.

Updated 2026-11-04T03:48:41Z. Bankroll cash (research-selected trades): 860.0946161788225. Open positions: 20. Pools on watchlist: 37.

| group | n | win | avg | CI | P&L $ |
|---|---|---|---|---|---|
| research-picked | 2 | 0% | -69.5% | - | -140 |
| momentum, not picked | 405 | 15% | -54.3% | -60 to -48 | -22043 |
| all momentum | 407 | 15% | -54.4% | -60 to -48 | -22183 |
| control | 482 | 8% | -16.4% | -20 to -13 | -7938 |
| dip buy | 4 | 25% | -13.1% | - | -52 |
| proven pools | 19 | 32% | -30.3% | -54 to -10 | -577 |

What-if exit rules on the SAME trades. Cells: avg return (trades, win rate).

| exit rule | momentum | control | dip | proven |
|---|---|---|---|---|
| base_sl30_tp100 | -55% (386, 15%) | -16% (482, 8%) | -13% (4, 25%) | -30% (19, 32%) |
| wide_sl50_tp100 | -55% (386, 17%) | -17% (482, 8%) | -13% (4, 25%) | -30% (19, 32%) |
| sl30_tp50 | -57% (386, 19%) | -17% (482, 8%) | -22% (4, 25%) | -30% (19, 32%) |
| sl50_tp50 | -56% (386, 21%) | -17% (482, 9%) | -22% (4, 25%) | -30% (19, 32%) |
| no_stop_tp100 | -55% (386, 18%) | -17% (482, 8%) | -13% (4, 25%) | -30% (19, 32%) |

Verdict: NOT ENOUGH DATA (need 30+ closed filter=1 trades and a CI above zero before believing anything).

Pools seen: 15206. Outcomes:

- missed_window: 10060
- low_liquidity: 2942
- proven_liquidity_gone: 884
- no_momentum: 533
- research_failed: 417
- simulated failed buy: 166
- proven_low_volume: 147
- proven_price_collapsed_or_parabolic: 21
- proven: 20
- proven_no_uptrend: 10
- dip: 4
- research_passed: 2

Warning: 115 judged pools had an unreadable mint/freeze value. Check mint_raw / freeze_raw in candidates.csv; the parsing may need fixing.
