# Paper trader summary

SIMULATION ONLY. No real trades.

Updated 2026-11-18T05:27:11Z. Bankroll cash (research-selected trades): 549.3536238229275. Open positions: 24. Pools on watchlist: 60.

| group | n | win | avg | CI | P&L $ |
|---|---|---|---|---|---|
| research-picked | 17 | 29% | -26.4% | -58 to 8 | -451 |
| momentum, not picked | 3035 | 11% | -66.5% | -68 to -65 | -202038 |
| all momentum | 3052 | 12% | -66.3% | -68 to -64 | -202488 |
| control | 3771 | 6% | -19.2% | -20 to -18 | -72609 |
| dip buy | 40 | 25% | -14.5% | -31 to 3 | -583 |
| proven pools | 117 | 32% | -33.8% | -43 to -24 | -3969 |

What-if exit rules on the SAME trades. Cells: avg return (trades, win rate).

| exit rule | momentum | control | dip | proven |
|---|---|---|---|---|
| base_sl30_tp100 | -66% (3031, 12%) | -19% (3771, 6%) | -15% (40, 25%) | -34% (117, 32%) |
| wide_sl50_tp100 | -66% (3031, 13%) | -19% (3771, 6%) | -17% (40, 28%) | -35% (117, 32%) |
| sl30_tp50 | -68% (3031, 14%) | -19% (3771, 7%) | -19% (40, 28%) | -34% (117, 33%) |
| sl50_tp50 | -67% (3031, 15%) | -20% (3771, 7%) | -21% (40, 32%) | -35% (117, 33%) |
| no_stop_tp100 | -66% (3031, 13%) | -20% (3771, 6%) | -15% (40, 28%) | -36% (117, 32%) |

Verdict: NOT ENOUGH DATA (need 30+ closed filter=1 trades and a CI above zero before believing anything).

Pools seen: 101503. Outcomes:

- missed_window: 66017
- low_liquidity: 16873
- proven_liquidity_gone: 8748
- no_momentum: 3824
- research_failed: 3048
- proven_low_volume: 1334
- simulated failed buy: 1270
- proven_price_collapsed_or_parabolic: 153
- proven: 119
- proven_no_uptrend: 60
- dip: 40
- research_passed: 17

Warning: 802 judged pools had an unreadable mint/freeze value. Check mint_raw / freeze_raw in candidates.csv; the parsing may need fixing.
