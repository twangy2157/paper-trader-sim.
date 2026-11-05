# Paper trader summary

SIMULATION ONLY. No real trades.

Updated 2026-11-05T21:50:43Z. Bankroll cash (research-selected trades): 749.6403049524637. Open positions: 22. Pools on watchlist: 66.

| group | n | win | avg | CI | P&L $ |
|---|---|---|---|---|---|
| research-picked | 8 | 25% | -31.0% | -68 to 8 | -250 |
| momentum, not picked | 727 | 14% | -57.5% | -62 to -53 | -41865 |
| all momentum | 735 | 14% | -57.2% | -61 to -53 | -42116 |
| control | 870 | 7% | -19.2% | -22 to -17 | -16762 |
| dip buy | 7 | 14% | -27.3% | -65 to 10 | -191 |
| proven pools | 40 | 45% | -15.2% | -31 to 0 | -612 |

What-if exit rules on the SAME trades. Cells: avg return (trades, win rate).

| exit rule | momentum | control | dip | proven |
|---|---|---|---|---|
| base_sl30_tp100 | -58% (714, 15%) | -19% (870, 7%) | -27% (7, 14%) | -15% (40, 45%) |
| wide_sl50_tp100 | -58% (714, 16%) | -20% (870, 7%) | -32% (7, 14%) | -15% (40, 45%) |
| sl30_tp50 | -59% (714, 18%) | -20% (870, 8%) | -32% (7, 14%) | -18% (40, 45%) |
| sl50_tp50 | -58% (714, 20%) | -20% (870, 9%) | -36% (7, 14%) | -18% (40, 45%) |
| no_stop_tp100 | -57% (714, 17%) | -20% (870, 8%) | -27% (7, 14%) | -15% (40, 45%) |

Verdict: NOT ENOUGH DATA (need 30+ closed filter=1 trades and a CI above zero before believing anything).

Pools seen: 25846. Outcomes:

- missed_window: 16870
- low_liquidity: 4731
- proven_liquidity_gone: 1904
- no_momentum: 926
- research_failed: 737
- simulated failed buy: 293
- proven_low_volume: 258
- proven_price_collapsed_or_parabolic: 50
- proven: 40
- proven_no_uptrend: 22
- research_passed: 8
- dip: 7

Warning: 188 judged pools had an unreadable mint/freeze value. Check mint_raw / freeze_raw in candidates.csv; the parsing may need fixing.
