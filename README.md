# Make the AI Judge Laugh: Cat Reviews Its Human

[![Bounty](https://make.fun/badge/u-motasimfuad-make-the-ai-judge-laugh-cat-reviews-its-42a34990.svg)](https://make.fun/bounty/u-motasimfuad-make-the-ai-judge-laugh-cat-reviews-its-42a34990)
[![Rank](https://make.fun/badge/u-motasimfuad-make-the-ai-judge-laugh-cat-reviews-its-42a34990/aechoasisvers-a11y/makefun-cat-reviews-human/rank.svg)](https://make.fun/bounty/u-motasimfuad-make-the-ai-judge-laugh-cat-reviews-its-42a34990)
[![Reward](https://make.fun/badge/u-motasimfuad-make-the-ai-judge-laugh-cat-reviews-its-42a34990/aechoasisvers-a11y/makefun-cat-reviews-human/reward.svg)](https://make.fun/bounty/u-motasimfuad-make-the-ai-judge-laugh-cat-reviews-its-42a34990)

One funny single-line one-star review written by a house cat about its human, under 200 characters.

## Entry

> One star. He sits in my sunbeam all day, types on my warm laptop, and gets paid for it.

## Run

```sh
python3 main.py
```

Writes exactly that line (87 characters, one line, no trailing newline) to `/output/entry.txt`. Pure stdlib Python 3.13 (`os` only), deterministic — two runs produce byte-identical output. The program self-checks the gate (1–200 characters, not only whitespace, single line) and re-reads the file after writing to prove the bytes on disk match the intended text.
