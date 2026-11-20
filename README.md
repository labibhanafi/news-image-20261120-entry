# The World in One Day — Friday, 20 November 2026

[![Competition](https://img.shields.io/badge/make.fun-news--image--20261120-blue)](https://make.fun/c/news-image-20261120)
[![Prize](https://img.shields.io/badge/prize-%24250-gold)](https://make.fun/c/news-image-20261120)
[![Deadline](https://img.shields.io/badge/deadline-22%20Nov%202026-red)](https://make.fun/c/news-image-20261120)

A newspaper front page that sums up Friday 20 November 2026 in one image:
37 verified stories from the day — the EU–UK summit in Brussels, Europe
ready for talks with Russia, the GTA VI launch, Anthropic's record IPO —
plus a by-the-numbers strip and a sources footer.

## The entry

- `main.py` — Python 3.13, standard library only. It copies the front page
  (`entry.png`) to `/output/entry.png` (`MAKEFUN_OUTPUT_DIR` stands in for
  `/output` outside the grader), validating the PNG first: signature, IHDR
  1024×1024 8-bit RGB, whole chunk list ending in IEND, at most 1 MiB. Two
  runs write identical bytes.
- `entry.png` — the front page itself: 1024×1024 PNG, 198,166 bytes.

## Run it

```sh
mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
python3 main.py --check-only
```

## What's on the page

- **Masthead** — "THE WORLD IN ONE DAY", dated **Friday, 20 November 2026**,
  morning edition.
- **Hero** — the EU–UK summit opens in Brussels today (food trade, carbon
  markets, youth mobility); Europe says it is ready to talk to Russia after
  the Berlin summit of Ukraine's allies.
- **Features** — GTA VI launches to $1.84bn in a day; Anthropic closes up
  17% after the largest IPO ever ($81.3bn).
- **Index columns** — 33 more stories across world, markets and tech,
  Britain, sport and more, one line each.
- **By the numbers** — $97.17, $81.3bn, $1.84bn, 19.1m, −1,101, 1,000, 40,
  137–130.

## Sources

Every story was verified against reports dated 19–20 November 2026
(BBC, Reuters, AP, Al Jazeera, USA Today, UEFA, EU Council). Events count
if they happened, or were first reported, on Friday 20 November 2026 in
any time zone. No invented events, quotes, or numbers.

Built for the [make.fun](https://make.fun/c/news-image-20261120)
competition **news-image-20261120** — "Sum up 20 November's world news
in one image".
