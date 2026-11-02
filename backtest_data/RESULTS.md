# Established memecoin backtest

SIMULATION ONLY. Hourly bars, fixed rules, 0.30% round-trip costs.
Updated 2026-11-02 03:01Z. Coins loaded: DOGE, SHIB, PEPE, BONK, WIF, FLOKI.

## All coins pooled (return per trade, after costs)

| rule | period | trades | win | avg | 95% CI of avg % |
|---|---|---|---|---|---|
| momentum | first 60% | 424 | 37% | 0.19% | -0.96 to 1.42 |
| momentum | last 40% | 201 | 31% | -0.62% | -2.36 to 1.24 |
| dip | first 60% | 514 | 48% | -0.63% | -1.29 to -0.00 |
| dip | last 40% | 176 | 60% | 0.86% | -0.16 to 1.84 |
| trend | first 60% | 460 | 28% | 4.71% | 1.11 to 9.42 |
| trend | last 40% | 333 | 20% | -1.13% | -1.98 to -0.24 |

## Last 40% of each coin: total return, compounding every trade

| coin | buy & hold | momentum | dip | trend |
|---|---|---|---|---|
| DOGE | -51% | -38% (35) | 32% (21) | -46% (62) |
| SHIB | -63% | -42% (32) | 67% (14) | -64% (64) |
| PEPE | -59% | -22% (38) | -7% (34) | -44% (57) |
| BONK | -85% | -46% (32) | 4% (39) | -64% (49) |
| WIF | -76% | -17% (27) | 26% (34) | -54% (48) |
| FLOKI | -73% | -49% (37) | 15% (34) | -56% (53) |

Cells show total return (number of trades). Buy & hold is the benchmark: a rule
that earns less than holding the coin, with similar risk, adds nothing.

## How to read this

- A rule is only interesting if the last-40% CI lower bound is above 0 AND it also
  looked decent in the first 60%. Anything else is noise or luck.
- CIs here are too narrow: coins move together, so trades are not independent.
- Memecoins mostly fell over long stretches, so 'buy and hold' can be very negative;
  beating it by losing less is not the same as making money.
