#!/usr/bin/env python3
"""Two-Sentence Horror — make.fun entry.

Writes exactly one two-sentence horror story to /output/entry.txt.

The story: a voicemail from the narrator's own number, timestamped
3 AM tonight, in which their own voice calmly lists everything they
will do this evening — and ends with the sound of their front door
opening. Sentence two reframes sentence one: what first reads as a
prank becomes a prediction that ends in intrusion. The horror is
implied, never explained; no gore, no familiar twist.
"""

import os

ENTRY = (
    "At noon, my phone buzzed with a voicemail from my own number, "
    "timestamped 3 AM tonight. It was my voice calmly listing "
    "everything I would do this evening, and it ended with the sound "
    "of my front door opening."
)

OUTPUT_PATH = "/output/entry.txt"
MAX_CHARS = 400


def main() -> None:
    if not (1 <= len(ENTRY) <= MAX_CHARS):
        raise ValueError(
            f"entry must be 1-{MAX_CHARS} characters, got {len(ENTRY)}"
        )
    if ENTRY != ENTRY.strip():
        raise ValueError("entry must not have leading or trailing whitespace")
    if ENTRY.count(".") != 2:
        raise ValueError("entry must be exactly two sentences")

    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(ENTRY)

    print(f"wrote {OUTPUT_PATH} ({len(ENTRY)} characters, 2 sentences)")


if __name__ == "__main__":
    main()
