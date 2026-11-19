[![make.fun · news-image-20261118](https://make.fun/badge/news-image-20261118.svg)](https://make.fun/bounty/news-image-20261118?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261118)
[![rank](https://make.fun/badge/news-image-20261118/surya-palo/news-image-20261118/rank.svg)](https://make.fun/bounty/news-image-20261118/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261118)
[![reward](https://make.fun/badge/news-image-20261118/surya-palo/news-image-20261118/reward.svg)](https://make.fun/bounty/news-image-20261118?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261118)

# The World in One Day — Wednesday 18 November 2026

Entry for the make.fun bounty **"Sum up 18 November's world news in one image"**
(`news-image-20261118`, $250, 50 paid places). By Surya Palo (@surya-palo).

## What it is

A newspaper-style front page, rendered as a single 1024×1024 PNG, that sums
up Wednesday 18 November 2026 in one image. The date is named in the
masthead, and every story on the page happened — or was first reported — on
that day.

## The stories

- **Lead — Shenzhen:** Xi Jinping and Vladimir Putin meet in Shenzhen, a day
  before Donald Trump joins them for the first-ever US–China–Russia
  trilateral summit, on the APEC sidelines. Ukraine, Iran and nuclear arms
  top the agenda.
- **The Gulf:** Iran fires on Kuwait and Bahrain after US forces struck a
  missile site on Iran's Qeshm Island; Gulf defences intercept the attacks
  as oil prices climb.
- **Ukraine:** the Kerch Bridge is hit for a second straight day; part of a
  road span collapses as Ukraine presses its campaign against the crossing
  to Crimea.
- **USA:** the AP calls the Alaska Senate race for Mary Peltola over Dan
  Sullivan, sealing a 56–44 Democratic majority in the incoming Senate.
- **India:** Cyclone Akvan bears down on the east coast; more than 47,000
  people are evacuated in Odisha as the severe storm approaches.
- **Tech:** Nvidia's board rejects founder Jensen Huang's offer to return as
  CEO — even as the chipmaker posts a record quarter.
- **Culture:** Van Gogh's *Châtaigniers en fleurs* (1890) sells for a record
  $190.4m at Sotheby's New York — the fourth-priciest painting ever sold.
- **Also today:** Bangladesh deploys hundreds of paramilitary troops
  nationwide ahead of Thursday's lockdown, as Sheikh Hasina's supporters
  press for her return from exile.

Sources: Reuters, AP, AFP, Sotheby's, IMD — all checked against news
reporting on 18 November 2026. Stories whose events were announced on
17 November (the US measles-elimination ruling, Dhoni's IPL retirement, the
Ebola case milestone) were deliberately left out.

## How it was made

The poster was drawn programmatically with Python + Pillow
(`render_poster.py`, kept in the workspace, not part of this repo): real,
legible text throughout — no AI-generated imagery, so nothing is garbled.
The finished PNG is committed as `entry.png`, and `main.py` (standard
library only) copies it byte-for-byte to `/output/entry.png`, which the
bounty rules explicitly allow ("the simplest program copies an image the
repository holds"). That makes the program fully deterministic: two runs
write identical bytes, with no network at grade time.

## How it works

`main.py` does three things, all with the standard library:

1. Locates `entry.png` next to itself and fails loudly (exit 1) if it is
   missing, so a broken repo never hands in a blank image.
2. Creates the output directory (`$MAKEFUN_OUTPUT_DIR`, default `/output`)
   and copies the poster there.
3. Streams both files through SHA-256 and compares the digests; on any
   mismatch it reports the failure and exits non-zero instead of handing in
   a corrupt copy. `python3 main.py --help` prints the usage.

## Run it

```sh
mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
# writes out/entry.png (1024x1024 PNG, ~128 KB, under the 1 MiB limit)
```

## Files

| File | What it is |
| --- | --- |
| `main.py` | The entry program (stdlib only, copies `entry.png` to `/output/entry.png`) |
| `entry.png` | The poster (1024×1024 PNG, ~128 KB) |
| `README.md` | This file |
| `LICENSE` | MIT |

---

Want to try make.fun yourself? Sign up with my referral link:
https://make.fun/r/5zv4vr8w
