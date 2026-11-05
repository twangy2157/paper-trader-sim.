# Paper trader summary

SIMULATION ONLY. No real trades.

Updated 2026-11-05T22:54:28Z. Bankroll cash (research-selected trades): 749.6403049524637. Open positions: 11. Pools on watchlist: 54.

| group | n | win | avg | CI | P&L $ |
|---|---|---|---|---|---|
| research-picked | 8 | 25% | -31.0% | -68 to 8 | -250 |
| momentum, not picked | 738 | 14% | -57.6% | -62 to -53 | -42562 |
| all momentum | 746 | 14% | -57.3% | -62 to -53 | -42813 |
| control | 882 | 7% | -19.2% | -22 to -17 | -17049 |
| dip buy | 7 | 14% | -27.3% | -65 to 10 | -191 |
| proven pools | 40 | 45% | -15.2% | -31 to 0 | -612 |

What-if exit rules on the SAME trades. Cells: avg return (trades, win rate).

| exit rule | momentum | control | dip | proven |
|---|---|---|---|---|
| base_sl30_tp100 | -58% (725, 15%) | -19% (882, 7%) | -27% (7, 14%) | -15% (40, 45%) |
| wide_sl50_tp100 | -58% (725, 16%) | -20% (882, 7%) | -32% (7, 14%) | -15% (40, 45%) |
| sl30_tp50 | -59% (725, 18%) | -20% (882, 8%) | -32% (7, 14%) | -18% (40, 45%) |
| sl50_tp50 | -59% (725, 20%) | -20% (882, 9%) | -36% (7, 14%) | -18% (40, 45%) |
| no_stop_tp100 | -57% (725, 17%) | -20% (882, 7%) | -27% (7, 14%) | -15% (40, 45%) |

Verdict: NOT ENOUGH DATA (need 30+ closed filter=1 trades and a CI above zero before believing anything).

Pools seen: 26198. Outcomes:

- missed_window: 17126
- low_liquidity: 4781
- proven_liquidity_gone: 1932
- no_momentum: 932
- research_failed: 743
- simulated failed buy: 298
- proven_low_volume: 259
- proven_price_collapsed_or_parabolic: 50
- proven: 40
- proven_no_uptrend: 22
- research_passed: 8
- dip: 7

Warning: 191 judged pools had an unreadable mint/freeze value. Check mint_raw / freeze_raw in candidates.csv; the parsing may need fixing.
