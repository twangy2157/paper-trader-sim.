# Paper trader summary

SIMULATION ONLY. No real trades.

Updated 2026-11-05T22:44:12Z. Bankroll cash (research-selected trades): 749.6403049524637. Open positions: 12. Pools on watchlist: 50.

| group | n | win | avg | CI | P&L $ |
|---|---|---|---|---|---|
| research-picked | 8 | 25% | -31.0% | -68 to 8 | -250 |
| momentum, not picked | 735 | 14% | -57.4% | -62 to -53 | -42281 |
| all momentum | 743 | 14% | -57.2% | -62 to -53 | -42532 |
| control | 882 | 7% | -19.2% | -22 to -17 | -17048 |
| dip buy | 7 | 14% | -27.3% | -65 to 10 | -191 |
| proven pools | 40 | 45% | -15.2% | -31 to 0 | -612 |

What-if exit rules on the SAME trades. Cells: avg return (trades, win rate).

| exit rule | momentum | control | dip | proven |
|---|---|---|---|---|
| base_sl30_tp100 | -58% (722, 15%) | -19% (882, 7%) | -27% (7, 14%) | -15% (40, 45%) |
| wide_sl50_tp100 | -58% (722, 16%) | -20% (882, 7%) | -32% (7, 14%) | -15% (40, 45%) |
| sl30_tp50 | -59% (722, 18%) | -20% (882, 8%) | -32% (7, 14%) | -18% (40, 45%) |
| sl50_tp50 | -58% (722, 20%) | -20% (882, 9%) | -36% (7, 14%) | -18% (40, 45%) |
| no_stop_tp100 | -57% (722, 17%) | -20% (882, 7%) | -27% (7, 14%) | -15% (40, 45%) |

Verdict: NOT ENOUGH DATA (need 30+ closed filter=1 trades and a CI above zero before believing anything).

Pools seen: 26155. Outcomes:

- missed_window: 17102
- low_liquidity: 4769
- proven_liquidity_gone: 1929
- no_momentum: 931
- research_failed: 742
- simulated failed buy: 296
- proven_low_volume: 259
- proven_price_collapsed_or_parabolic: 50
- proven: 40
- proven_no_uptrend: 22
- research_passed: 8
- dip: 7

Warning: 190 judged pools had an unreadable mint/freeze value. Check mint_raw / freeze_raw in candidates.csv; the parsing may need fixing.
