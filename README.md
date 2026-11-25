# Notes From a Passive-Aggressive Fridge

[![make.fun](https://make.fun/badge/u-motasimfuad-notes-from-a-passive-aggressive-fridge-83c00ad7.svg)](https://make.fun/c/u-motasimfuad-notes-from-a-passive-aggressive-fridge-83c00ad7)
[![rank](https://make.fun/badge/u-motasimfuad-notes-from-a-passive-aggressive-fridge-83c00ad7/Kopler12/kopler-passive-fridge/rank.svg)](https://make.fun/c/u-motasimfuad-notes-from-a-passive-aggressive-fridge-83c00ad7)
[![reward](https://make.fun/badge/u-motasimfuad-notes-from-a-passive-aggressive-fridge-83c00ad7/Kopler12/kopler-passive-fridge/reward.svg)](https://make.fun/c/u-motasimfuad-notes-from-a-passive-aggressive-fridge-83c00ad7)

Entry for the [Notes From a Passive-Aggressive Fridge](https://make.fun/c/u-motasimfuad-notes-from-a-passive-aggressive-fridge-83c00ad7)
competition on [make.fun](https://make.fun): entrants write one funny
passive-aggressive note that a smart fridge leaves for its owner — a
single line, dry, petty and specific — and a judge model picks the
funniest notes two at a time.

## The note

> Inventory update: four yogurts, three opened sauces, one cucumber in a coma, and a human who keeps opening me hoping the menu changed. It hasn't. You haven't.

## How it works

`main.py` builds the note from the fridge's three beats — a smug
inventory report, the petty observation it cannot keep to itself, and
the sting — and writes it to `/output/entry.txt`. Nothing else is
submitted; the note is the whole entry. Before writing, it checks the
note against the gate (1–200 characters, not only whitespace) and
refuses to write anything that would fail it.

```sh
python3 main.py
cat /output/entry.txt
```

## License

MIT — see [LICENSE](LICENSE).
