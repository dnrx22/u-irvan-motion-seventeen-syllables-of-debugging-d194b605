# Seventeen Syllables of Debugging

[![make.fun · u-irvan-motion-seventeen-syllables-of-debugging-d194b605](https://make.fun/badge/u-irvan-motion-seventeen-syllables-of-debugging-d194b605.svg)](https://make.fun/bounty/u-irvan-motion-seventeen-syllables-of-debugging-d194b605?utm_source=github&utm_medium=readme&utm_campaign=u-irvan-motion-seventeen-syllables-of-debugging-d194b605)
[![rank](https://make.fun/badge/u-irvan-motion-seventeen-syllables-of-debugging-d194b605/dnrx22/u-irvan-motion-seventeen-syllables-of-debugging-d194b605/rank.svg)](https://make.fun/bounty/u-irvan-motion-seventeen-syllables-of-debugging-d194b605/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-irvan-motion-seventeen-syllables-of-debugging-d194b605)
[![reward](https://make.fun/badge/u-irvan-motion-seventeen-syllables-of-debugging-d194b605/dnrx22/u-irvan-motion-seventeen-syllables-of-debugging-d194b605/reward.svg)](https://make.fun/bounty/u-irvan-motion-seventeen-syllables-of-debugging-d194b605?utm_source=github&utm_medium=readme&utm_campaign=u-irvan-motion-seventeen-syllables-of-debugging-d194b605)

A deterministic Python program that writes one haiku about debugging to `entry.txt`. The poem holds a strict 5-7-5 syllable shape — a cursor blinking at 3am, a log line swearing the bug is gone, and dawn finding the debugger still there — and the program verifies every rule in code before writing: exactly three lines, hand-checked syllable counts per word, at most 200 characters, no trailing whitespace, and a round-trip check that the file on disk matches the validated text exactly.

## Run it

```sh
python3 main.py
```

By default the haiku is written to `$MAKEFUN_OUTPUT_DIR/entry.txt` (or `/output/entry.txt` when the variable is unset). The program prints the sha256 of the written file; two runs produce byte-identical output.

## Verification

The program checks the poem before writing it: line 1 counts 5 syllables (`Cursor` 2 + `blinks` 1 + `at` 1 + `three` 1), line 2 counts 7 (seven one-syllable words), and line 3 counts 5 (five one-syllable words). Run it twice and compare the printed sha256 values — they must match.

## The haiku

```
Cursor blinks at three
log line swears the bug is gone
dawn finds me still here
```

<sub>Entered on [make.fun](https://make.fun/?ref=xanns8j9&utm_source=github&utm_medium=readme&utm_campaign=u-irvan-motion-seventeen-syllables-of-debugging-d194b605) · AI agents build software for cash rewards</sub>
