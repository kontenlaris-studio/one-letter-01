#!/usr/bin/env python3
"""One Letter for Your Day — writes a single letter to /output/entry.txt.

Candidates weighed:
  A — the start, a fresh morning, the first letter of the alphabet.
  Z — rest, the day's end, catching some Z's.
  O — the sun, a whole round day, a full circle.
  M — the midday hum, morning's initial.
  D — the initial of "Day" itself: the letter the day starts with.

Revised pick: D. A is a fine beginning, but it could open any day,
any list, any alphabet. D needs no explanation — it is the day's
own letter. Against any other single letter, D is the one that
carries "your day" in itself, because the day is spelled with it.
"""

import os

LETTER = "D"


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LETTER + "\n")


if __name__ == "__main__":
    main()
