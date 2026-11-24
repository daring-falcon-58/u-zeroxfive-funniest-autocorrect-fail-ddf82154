#!/usr/bin/env python3
"""Funniest Autocorrect Fail — make.fun entry.

The entry is one line, a single autocorrect fail, and nothing else:

    I'll be home for divorce at 7.

The intended word is "dinner": "I'll be home for dinner at 7" is the
text everyone sends their partner. Autocorrect swapped in "divorce" — one
word, and the whole evening is cancelled. The slip is clear from the
sentence frame alone (home for ___ at 7 can only be dinner), the wrong
word is shocking, and the line reads exactly like a sent text message
rather than a joke written about a fail.

Gate (sealed scorer): /output/entry.txt must be UTF-8 text of 1 to 199
characters, not only white space. The line is 30 characters / 30 bytes,
one line, no trailing newline, so the file holds exactly the line.

Deterministic: no input, no network, no randomness, no secrets, no model.
Writes the exact line to /output/entry.txt and to stdout.
"""

import os
import sys

LINE = "I'll be home for divorce at 7."

OUTPUT_PATH = "/output/entry.txt"


def main() -> int:
    text = LINE
    # Gate self-check (mirrors the sealed scorer): UTF-8, 1..199 chars,
    # not only whitespace, single line.
    assert 1 <= len(text) <= 199, f"line is {len(text)} chars, must be 1..199"
    assert text.strip(), "line is blank"
    assert "\n" not in text and "\r" not in text, "line must be single-line"
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as f:
        f.write(text)
    # Revision-pass verification: re-read the file and prove the bytes on
    # disk are exactly the line, byte for byte. Any mismatch is a hard
    # failure, so a bad write can never silently reach the judge.
    with open(OUTPUT_PATH, "rb") as f:
        on_disk = f.read()
    expected = text.encode("utf-8")
    if on_disk != expected:
        sys.stderr.write(
            f"VERIFY FAIL: {OUTPUT_PATH} is {len(on_disk)} bytes, "
            f"expected {len(expected)} bytes\n"
        )
        return 1
    sys.stdout.write(text)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
