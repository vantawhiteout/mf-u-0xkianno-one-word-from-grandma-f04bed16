#!/usr/bin/env python3
"""One Word From Grandma -- write the entry.

The whole entry is a single word: the one thing grandma would text about
"AI". She would not type the brand name neatly; she would text it the way
she says it, phonetically, with a little bafflement:

    chatgippity

One word, lowercase, no punctuation, well under the 30-character gate.
"""

from pathlib import Path

# The word grandma would actually text. One token, nothing else.
ENTRY_WORD = "chatgippity"

# The grader reads this exact path.
OUTPUT_PATH = Path("/output/entry.txt")


def validate_word(word: str) -> str:
    """Guard the sealed scorer's gate: UTF-8 text, 1-30 chars, one word."""
    if not isinstance(word, str):
        raise TypeError("entry must be text")
    if not 1 <= len(word) <= 30:
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
