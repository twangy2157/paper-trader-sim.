# Paper trader summary

SIMULATION ONLY. No real trades.

Updated 2026-11-06T01:07:35Z. Bankroll cash (research-selected trades): 749.6403049524637. Open positions: 15. Pools on watchlist: 29.

| group | n | win | avg | CI | P&L $ |
|---|---|---|---|---|---|
| research-picked | 8 | 25% | -31.0% | -68 to 8 | -250 |
| momentum, not picked | 748 | 14% | -58.1% | -62 to -53 | -43527 |
| all momentum | 756 | 14% | -57.8% | -62 to -53 | -43778 |
| control | 901 | 7% | -19.0% | -21 to -16 | -17212 |
| dip buy | 7 | 14% | -27.3% | -65 to 10 | -191 |
| proven pools | 40 | 45% | -15.2% | -31 to 0 | -612 |

What-if exit rules on the SAME trades. Cells: avg return (trades, win rate).

| exit rule | momentum | control | dip | proven |
|---|---|---|---|---|
| base_sl30_tp100 | -58% (735, 14%) | -19% (901, 7%) | -27% (7, 14%) | -15% (40, 45%) |
| wide_sl50_tp100 | -58% (735, 16%) | -19% (901, 7%) | -32% (7, 14%) | -15% (40, 45%) |
| sl30_tp50 | -60% (735, 18%) | -19% (901, 8%) | -32% (7, 14%) | -18% (40, 45%) |
| sl50_tp50 | -59% (735, 20%) | -20% (901, 9%) | -36% (7, 14%) | -18% (40, 45%) |
| no_stop_tp100 | -58% (735, 17%) | -20% (901, 8%) | -27% (7, 14%) | -15% (40, 45%) |

Verdict: NOT ENOUGH DATA (need 30+ closed filter=1 trades and a CI above zero before believing anything).

Pools seen: 26717. Outcomes:

- missed_window: 17449
- low_liquidity: 4874
- proven_liquidity_gone: 1984
- no_momentum: 955
- research_failed: 752
- simulated failed buy: 310
- proven_low_volume: 264
- proven_price_collapsed_or_parabolic: 51
- proven: 40
- proven_no_uptrend: 22
- research_passed: 8
- dip: 8

Warning: 200 judged pools had an unreadable mint/freeze value. Check mint_raw / freeze_raw in candidates.csv; the parsing may need fixing.
