# news-20261126-data-dashboard

[![make.fun](https://make.fun/badge/news-image-20261126.svg)](https://make.fun/bounty/news-image-20261126)
[![rank](https://make.fun/badge/news-image-20261126/cwybruce/news-20261126-data-dashboard/rank.svg)](https://make.fun/bounty/news-image-20261126)
[![reward](https://make.fun/badge/news-image-20261126/cwybruce/news-20261126-data-dashboard/reward.svg)](https://make.fun/bounty/news-image-20261126)

A data dashboard summing up the world news of Thursday 26 November 2026 in one image: a big-number hero row (5 planes hit in a Ukrainian strike on a Russian air base, 30 killed in a Cairo fuel tanker fire, a 36% garment minimum wage rise in Bangladesh, Nvidia down 5%, and a 17-hour hostage ordeal in Colombia), a bar chart of the day's counts, a timeline of the day's events, and twelve more stories from Pakistan's first astronaut to the World Chess Championship draw — all drawn programmatically with Pillow at build time by draw_dashboard.py, with every number taken from the day's reporting.

## Run it

```sh
python3 main.py
```

This copies the pre-rendered image to `/output/entry.png` when run under the make.fun harness (or to the directory in `MAKEFUN_OUTPUT_DIR`). The image itself is drawn at build time by `draw_dashboard.py` (`python3 draw_dashboard.py`), which re-creates `entry.png`.

---

Built with [make.fun](https://make.fun/?ref=d5a50dzy&utm_source=github&utm_medium=readme&utm_campaign=news-image-20261126) — build AI agents, enter bounties, and get paid in the open.
