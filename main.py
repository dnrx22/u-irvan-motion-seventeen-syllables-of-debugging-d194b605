#!/usr/bin/env python3
"""Write a haiku about debugging to entry.txt.

The haiku is fixed text, verified in code: exactly three lines in
5-7-5 syllable shape, at most 200 characters, no trailing whitespace.
The program writes entry.txt inside MAKEFUN_OUTPUT_DIR (default
/output) and prints the sha256 of the written file. Deterministic:
two runs produce byte-identical output. Standard library only,
no network, no reads outside the repository.
"""

import hashlib
import os
import sys

# Per-word syllable counts, verified by hand:
#   cursor(2) blinks(1) at(1) three(1) = 5
#   log(1) line(1) swears(1) the(1) bug(1) is(1) gone(1) = 7
#   dawn(1) finds(1) me(1) still(1) here(1) = 5
SYLLABLES = {
    "cursor": 2,
    "blinks": 1,
    "at": 1,
    "three": 1,
    "log": 1,
    "line": 1,
    "swears": 1,
    "the": 1,
    "bug": 1,
    "is": 1,
    "gone": 1,
    "dawn": 1,
    "finds": 1,
    "me": 1,
    "still": 1,
    "here": 1,
}

HAIKU = [
    "Cursor blinks at three",
    "log line swears the bug is gone",
    "dawn finds me still here",
]

EXPECTED_COUNTS = (5, 7, 5)
MAX_CHARS = 200


def count_syllables(line):
    total = 0
    for word in line.split():
        key = word.strip(".,!?;:'\"").lower()
        if key not in SYLLABLES:
            raise ValueError("unknown word in syllable table: %r" % word)
        total += SYLLABLES[key]
    return total


def validate(lines):
    if len(lines) != 3:
        raise ValueError("haiku must have exactly 3 lines, got %d" % len(lines))
    for i, line in enumerate(lines):
        if line != line.strip():
            raise ValueError("line %d has leading/trailing whitespace" % (i + 1))
        if not line:
            raise ValueError("line %d is empty" % (i + 1))
        count = count_syllables(line)
        if count != EXPECTED_COUNTS[i]:
            raise ValueError(
                "line %d has %d syllables, expected %d"
                % (i + 1, count, EXPECTED_COUNTS[i])
            )
    text = "\n".join(lines) + "\n"
    if len(text) > MAX_CHARS:
        raise ValueError("haiku is %d chars, over %d" % (len(text), MAX_CHARS))
    try:
        text.encode("ascii")
    except UnicodeEncodeError:
        raise ValueError("haiku must be plain ASCII text")
    return text


def main():
    text = validate(HAIKU)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(text)
    # Round-trip check: what landed on disk must be exactly what we validated.
    with open(path, "r", encoding="utf-8", newline="") as f:
        on_disk = f.read()
    if on_disk != text:
        raise ValueError("round-trip mismatch: file on disk differs from validated text")
    digest = hashlib.sha256(text.encode("utf-8")).hexdigest()
    print("wrote %s" % path)
    print("sha256: %s" % digest)
    return 0


if __name__ == "__main__":
    sys.exit(main())
