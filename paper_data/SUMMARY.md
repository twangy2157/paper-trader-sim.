# Paper trader summary

SIMULATION ONLY. No real trades.

Updated 2026-11-05T16:19:44Z. Bankroll cash (research-selected trades): 749.6403049524637. Open positions: 14. Pools on watchlist: 44.

| group | n | win | avg | CI | P&L $ |
|---|---|---|---|---|---|
| research-picked | 8 | 25% | -31.0% | -68 to 8 | -250 |
| momentum, not picked | 682 | 15% | -56.5% | -61 to -52 | -38618 |
| all momentum | 690 | 15% | -56.2% | -61 to -52 | -38869 |
| control | 815 | 7% | -18.7% | -21 to -16 | -15331 |
| dip buy | 7 | 14% | -27.3% | -65 to 10 | -191 |
| proven pools | 38 | 42% | -17.9% | -34 to -2 | -681 |

What-if exit rules on the SAME trades. Cells: avg return (trades, win rate).

| exit rule | momentum | control | dip | proven |
|---|---|---|---|---|
| base_sl30_tp100 | -57% (669, 15%) | -19% (815, 7%) | -27% (7, 14%) | -18% (38, 42%) |
| wide_sl50_tp100 | -57% (669, 17%) | -19% (815, 8%) | -32% (7, 14%) | -18% (38, 42%) |
| sl30_tp50 | -58% (669, 19%) | -19% (815, 8%) | -32% (7, 14%) | -20% (38, 42%) |
| sl50_tp50 | -57% (669, 21%) | -19% (815, 9%) | -36% (7, 14%) | -20% (38, 42%) |
| no_stop_tp100 | -56% (669, 18%) | -19% (815, 8%) | -27% (7, 14%) | -18% (38, 42%) |

Verdict: NOT ENOUGH DATA (need 30+ closed filter=1 trades and a CI above zero before believing anything).

Pools seen: 24360. Outcomes:

- missed_window: 15919
- low_liquidity: 4478
- proven_liquidity_gone: 1766
- no_momentum: 868
- research_failed: 687
- simulated failed buy: 279
- proven_low_volume: 240
- proven_price_collapsed_or_parabolic: 48
- proven: 38
- proven_no_uptrend: 22
- research_passed: 8
- dip: 7

Warning: 182 judged pools had an unreadable mint/freeze value. Check mint_raw / freeze_raw in candidates.csv; the parsing may need fixing.
