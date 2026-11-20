# Paper trader summary

SIMULATION ONLY. No real trades.

Updated 2026-11-20T00:41:54Z. Bankroll cash (research-selected trades): 663.3425766779495. Open positions: 11. Pools on watchlist: 32.

| group | n | win | avg | CI | P&L $ |
|---|---|---|---|---|---|
| research-picked | 19 | 37% | -17.6% | -48 to 14 | -337 |
| momentum, not picked | 3212 | 11% | -67.1% | -69 to -65 | -215802 |
| all momentum | 3231 | 11% | -66.8% | -69 to -65 | -216138 |
| control | 3929 | 6% | -19.2% | -20 to -18 | -75713 |
| dip buy | 41 | 27% | -12.0% | -29 to 6 | -494 |
| proven pools | 123 | 33% | -31.5% | -41 to -22 | -3883 |

What-if exit rules on the SAME trades. Cells: avg return (trades, win rate).

| exit rule | momentum | control | dip | proven |
|---|---|---|---|---|
| base_sl30_tp100 | -67% (3210, 11%) | -19% (3929, 6%) | -12% (41, 27%) | -31% (123, 33%) |
| wide_sl50_tp100 | -67% (3210, 13%) | -19% (3929, 7%) | -15% (41, 29%) | -32% (123, 33%) |
| sl30_tp50 | -68% (3210, 14%) | -19% (3929, 7%) | -18% (41, 29%) | -32% (123, 34%) |
| sl50_tp50 | -68% (3210, 15%) | -20% (3929, 8%) | -19% (41, 34%) | -33% (123, 34%) |
| no_stop_tp100 | -67% (3210, 13%) | -20% (3929, 7%) | -13% (41, 29%) | -33% (123, 33%) |

Verdict: NOT ENOUGH DATA (need 30+ closed filter=1 trades and a CI above zero before believing anything).

Pools seen: 106396. Outcomes:

- missed_window: 69153
- low_liquidity: 17777
- proven_liquidity_gone: 9165
- no_momentum: 3983
- research_failed: 3213
- proven_low_volume: 1371
- simulated failed buy: 1331
- proven_price_collapsed_or_parabolic: 158
- proven: 123
- proven_no_uptrend: 62
- dip: 41
- research_passed: 19

Warning: 839 judged pools had an unreadable mint/freeze value. Check mint_raw / freeze_raw in candidates.csv; the parsing may need fixing.
