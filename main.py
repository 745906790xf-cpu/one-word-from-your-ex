"""One Word From Your Ex entry for make.fun.

Writes one word to /output/entry.txt: the single word an ex would use
to describe them. The sandbox runs this program twice and both runs must
write the same bytes, so the word is a fixed string with no randomness,
clock, or network access.
"""

import os

WORD = "Exhausting"  # The ex's verdict: draining to be with, and it carries "ex" in it.


def check_word(word: str) -> str:
    """Return the word unchanged, guarding the gate's limits.

    The gate accepts one word of 1 to 30 characters with no whitespace,
    so fail loudly here rather than write an entry the judge never sees.
    """
    if not word or len(word) > 30 or any(ch.isspace() for ch in word):
        raise ValueError("entry must be one word of 1 to 30 characters")
    if any(ord(ch) < 32 for ch in word):
        raise ValueError("entry must not contain control characters")
    return word


def write_entry(path: str = "/output/entry.txt") -> None:
    """Write the word as UTF-8 with no trailing newline.

    Keeping the bytes exact matters: the gate accepts 1 to 30 characters
    of UTF-8 text, and the two sandbox runs must produce identical
    output.
    """
    parent = os.path.dirname(path)
    if parent:
        os.makedirs(parent, exist_ok=True)
    with open(path, "w", encoding="utf-8", newline="") as handle:
        handle.write(check_word(WORD))


if __name__ == "__main__":
    write_entry()
