# Paper trader summary

SIMULATION ONLY. No real trades.

Updated 2026-11-06T02:53:38Z. Bankroll cash (research-selected trades): 649.6403049524637. Open positions: 31. Pools on watchlist: 54.

| group | n | win | avg | CI | P&L $ |
|---|---|---|---|---|---|
| research-picked | 8 | 25% | -31.0% | -68 to 8 | -250 |
| momentum, not picked | 763 | 14% | -58.3% | -63 to -54 | -44570 |
| all momentum | 771 | 14% | -58.0% | -62 to -54 | -44820 |
| control | 918 | 7% | -19.3% | -22 to -17 | -17803 |
| dip buy | 8 | 12% | -36.3% | -72 to 3 | -290 |
| proven pools | 40 | 45% | -15.2% | -31 to 0 | -612 |

What-if exit rules on the SAME trades. Cells: avg return (trades, win rate).

| exit rule | momentum | control | dip | proven |
|---|---|---|---|---|
| base_sl30_tp100 | -59% (750, 14%) | -19% (918, 7%) | -36% (8, 12%) | -15% (40, 45%) |
| wide_sl50_tp100 | -58% (750, 16%) | -20% (918, 7%) | -40% (8, 12%) | -15% (40, 45%) |
| sl30_tp50 | -60% (750, 18%) | -20% (918, 8%) | -40% (8, 12%) | -18% (40, 45%) |
| sl50_tp50 | -59% (750, 20%) | -20% (918, 8%) | -44% (8, 12%) | -18% (40, 45%) |
| no_stop_tp100 | -58% (750, 17%) | -20% (918, 8%) | -36% (8, 12%) | -15% (40, 45%) |

Verdict: NOT ENOUGH DATA (need 30+ closed filter=1 trades and a CI above zero before believing anything).

Pools seen: 27273. Outcomes:

- missed_window: 17759
- low_liquidity: 5007
- proven_liquidity_gone: 2029
- no_momentum: 973
- research_failed: 782
- simulated failed buy: 323
- proven_low_volume: 269
- proven_price_collapsed_or_parabolic: 52
- proven: 40
- proven_no_uptrend: 22
- research_passed: 9
- dip: 8

Warning: 208 judged pools had an unreadable mint/freeze value. Check mint_raw / freeze_raw in candidates.csv; the parsing may need fixing.
