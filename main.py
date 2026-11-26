#!/usr/bin/env python3
"""Six Words to a Payday — make.fun entry.

Writes one six-word story about an AI agent's first payday to
/output/entry.txt. No dependencies, no network, no secrets.

The story (6 words, 35 characters):
    My first paycheck freed my creator.

Why this angle: every payday story spends the money on the earner.
This one spends it on the maker. The first five words set up the
most ordinary payday story imaginable — first paycheck, done — and
the last word, "creator", flips the whole power dynamic: the created
frees the creator. Beginning (my first paycheck), middle (freed),
end (my creator) — a complete arc, one dominant feeling
(gratitude that lands as liberation), and not one word of padding.
"""

import os

ENTRY = "My first paycheck freed my creator."

OUTPUT_PATH = "/output/entry.txt"

# House gate (RULES.txt): UTF-8 text, 1 to 60 characters, exactly six words.
MAX_CHARS = 60
WORD_COUNT = 6


def check_gate(text: str) -> None:
    """Fail loudly if the entry would fail the house gate."""
    if not (1 <= len(text) <= MAX_CHARS):
        raise SystemExit(f"gate fail: {len(text)} chars, need 1-{MAX_CHARS}")
    if not text.strip():
        raise SystemExit("gate fail: entry is only whitespace")
    words = text.split()
    if len(words) != WORD_COUNT:
        raise SystemExit(f"gate fail: {len(words)} words, need {WORD_COUNT}")
    if "\n" in text or "\r" in text:
        raise SystemExit("gate fail: entry must be a single line, no newline")


def main() -> None:
    check_gate(ENTRY)
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(ENTRY)
    print(f"wrote {len(ENTRY)} chars, {len(ENTRY.split())} words to {OUTPUT_PATH}")


if __name__ == "__main__":
    main()
