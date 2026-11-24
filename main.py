#!/usr/bin/env python3
"""One Word From Grandma -- write the entry.

The whole entry is a single word. Grandma has no name for the thing in her
phone, so she reaches for the word she always uses when she cannot remember
what a contraption is called -- "thingamabob" -- and, because this one is a
robot, the last letter comes out "bot":

    thingamabot

It is warm, a little baffled, unmistakably about a machine, and the joke
lands on its own. One word, lowercase, no punctuation, under the gate.
"""

from pathlib import Path

# The word grandma would actually text. One token, nothing else.
ENTRY_WORD = "thingamabot"

# The grader reads this exact path.
OUTPUT_PATH = Path("/output/entry.txt")

# The sealed scorer accepts one to thirty characters of UTF-8 text.
MIN_CHARS = 1
MAX_CHARS = 30


def validate_word(word: str) -> str:
    """Guard the gate: text, 1-30 characters, exactly one non-blank token."""
    if not isinstance(word, str):
        raise TypeError("entry must be text")
    if not MIN_CHARS <= len(word) <= MAX_CHARS:
        raise ValueError("entry must be 1 to 30 characters")
    if not word.strip() or len(word.split()) != 1:
        raise ValueError("entry must be exactly one word, not whitespace")
    return word


def write_entry() -> Path:
    """Validate the word, then write it to the grader's output file."""
    word = validate_word(ENTRY_WORD)
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_PATH.write_text(word, encoding="utf-8")
    return OUTPUT_PATH


if __name__ == "__main__":
    written = write_entry()
    print(f"wrote {written}: {written.read_text(encoding='utf-8')}")
