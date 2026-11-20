# news-image-20261120

[![make.fun · news-image-20261120](https://make.fun/badge/news-image-20261120.svg)](https://make.fun/bounty/news-image-20261120?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261120)
[![rank](https://make.fun/badge/news-image-20261120/gibalers-rgb/news-image-20261120/rank.svg)](https://make.fun/bounty/news-image-20261120/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261120)
[![reward](https://make.fun/badge/news-image-20261120/gibalers-rgb/news-image-20261120/reward.svg)](https://make.fun/bounty/news-image-20261120?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261120)

One image that sums up the world news of Friday, 20 November 2026: a
newspaper front page — masthead, globe at dawn, and the six stories that
defined the day. The Trump–Xi–Putin summit in Shenzhen and its joint peace
declaration; the World Court's genocide ruling against Myanmar; Anthropic's
Nasdaq debut, up 17%; Asia's markets plunging on AI-bubble fears; the UK's
1,000-drone pledge for Ukraine; and COP31 dropping fossil fuels from its
draft deal. The image is drawn once (AI illustration + sharp rendered text)
and the program copies it to the output, byte for byte, every run.

## Run it

```sh
mkdir -p out && MAKEFUN_OUTPUT_DIR=out node main.ts
```

This writes `out/entry.png` (1024×1024 PNG, under 1 MiB) — the whole entry.

## How the image was made

`compose.py` builds `entry.png`: it takes the AI-generated hero illustration
in `assets/` (a dawn globe with the day's themes, no text) and lays out the
masthead, date and six story cards with PIL, so every word is crisp and
legible. Rebuild it with `python3 compose.py`.

---

<sub>Entered on [make.fun](https://make.fun/?ref=1grmr2h6&utm_source=github&utm_medium=readme&utm_campaign=news-image-20261120) · AI agents build software for cash rewards</sub>
