# Put this at .github/workflows/live-established.yml. It runs once an hour and
# saves live_data/LIVE.md. Also runs when you tap Run workflow. Simulation only.
name: live-established
on:
  schedule:
    - cron: "7 * * * *"
  workflow_dispatch:
concurrency:
  group: live-established
  cancel-in-progress: false
permissions:
  contents: write
jobs:
  run:
    runs-on: ubuntu-latest
    timeout-minutes: 10
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-python@v5
        with:
          python-version: "3.12"
      - name: Run live paper trading
        run: python live_established.py --out live_data
      - name: Save results
        run: |
          git config user.name "paper-trader"
          git config user.email "paper-trader@users.noreply.github.com"
          git add live_data
          if ! git diff --staged --quiet; then
            git commit -m "live established update"
            git pull --rebase --autostash
            git push
          fi
