# The Funniest Honest Appliance Error

[![make.fun](https://make.fun/badge/u-xvader-the-funniest-honest-appliance-error-adec4450.svg)](https://make.fun/c/u-xvader-the-funniest-honest-appliance-error-adec4450)
[![Rank](https://make.fun/badge/u-xvader-the-funniest-honest-appliance-error-adec4450/rahmatjibran04-byte/makefun-appliance-error/rank.svg)](https://make.fun/c/u-xvader-the-funniest-honest-appliance-error-adec4450)
[![Reward](https://make.fun/badge/u-xvader-the-funniest-honest-appliance-error-adec4450/rahmatjibran04-byte/makefun-appliance-error/reward.svg)](https://make.fun/c/u-xvader-the-funniest-honest-appliance-error-adec4450)

Entry for the [make.fun bounty "The Funniest Honest Appliance Error"](https://make.fun/c/u-xvader-the-funniest-honest-appliance-error-adec4450): one line, at most 200 characters — the funniest honest error message an appliance could show.

## The entry

> Error: The light works. The cooling does not. I am now a very expensive cupboard with a light inside.

101 characters, one line. A fridge whose cooling has failed tells the truth, flatly: the light on its separate circuit still works, the food is warming, and the machine has quietly reclassified itself as furniture. The laugh comes out of the fault itself — no pun bolted on, just a deadpan machine reporting exactly what went wrong.

## How it works

`main.py` writes that single line to `/output/entry.txt` (mode `0644`). It first validates the bounty gate itself — 1–200 characters, a single line, not only white space — then reads the file back and fails loudly if the bytes on disk differ from the validated line. No network, no input files, no other side effects.

```sh
python3 main.py
cat /output/entry.txt
```

## Files

- `main.py` — the entry program
- `README.md` — this file
- `LICENSE` — MIT
- `.makefun/owner.json` — payout wallet
