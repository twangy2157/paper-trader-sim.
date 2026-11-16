# Paper trader summary

SIMULATION ONLY. No real trades.

Updated 2026-11-16T13:03:58Z. Bankroll cash (research-selected trades): 549.3536238229275. Open positions: 27. Pools on watchlist: 46.

| group | n | win | avg | CI | P&L $ |
|---|---|---|---|---|---|
| research-picked | 17 | 29% | -26.4% | -58 to 8 | -451 |
| momentum, not picked | 2693 | 12% | -66.1% | -68 to -64 | -178176 |
| all momentum | 2710 | 12% | -65.8% | -68 to -64 | -178627 |
| control | 3418 | 6% | -18.9% | -20 to -18 | -64830 |
| dip buy | 35 | 29% | -12.5% | -31 to 8 | -440 |
| proven pools | 114 | 33% | -34.3% | -43 to -25 | -3925 |

What-if exit rules on the SAME trades. Cells: avg return (trades, win rate).

| exit rule | momentum | control | dip | proven |
|---|---|---|---|---|
| base_sl30_tp100 | -66% (2689, 12%) | -19% (3418, 6%) | -13% (35, 29%) | -34% (114, 33%) |
| wide_sl50_tp100 | -66% (2689, 13%) | -19% (3418, 6%) | -15% (35, 31%) | -36% (114, 33%) |
| sl30_tp50 | -67% (2689, 14%) | -19% (3418, 7%) | -18% (35, 31%) | -34% (114, 34%) |
| sl50_tp50 | -67% (2689, 15%) | -19% (3418, 7%) | -19% (35, 37%) | -36% (114, 34%) |
| no_stop_tp100 | -66% (2689, 14%) | -19% (3418, 6%) | -13% (35, 31%) | -36% (114, 33%) |

Verdict: NOT ENOUGH DATA (need 30+ closed filter=1 trades and a CI above zero before believing anything).

Pools seen: 93081. Outcomes:

- missed_window: 61027
- low_liquidity: 15268
- proven_liquidity_gone: 7858
- no_momentum: 3475
- research_failed: 2707
- proven_low_volume: 1234
- simulated failed buy: 1143
- proven_price_collapsed_or_parabolic: 145
- proven: 114
- proven_no_uptrend: 58
- dip: 35
- research_passed: 17

Warning: 730 judged pools had an unreadable mint/freeze value. Check mint_raw / freeze_raw in candidates.csv; the parsing may need fixing.
