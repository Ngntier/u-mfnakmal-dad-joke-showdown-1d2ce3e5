"""Dad Joke Showdown — u-mfnakmal-dad-joke-showdown-1d2ce3e5.

Writes one original dad joke to /output/entry.txt (or
$MAKEFUN_OUTPUT_DIR/entry.txt). The joke is validated against the
competition gate before it is written: UTF-8 text, 1-200 characters,
not only whitespace, single line.
"""

import os

JOKE = (
    "I asked my son for the screwdriver, and he said, "
    "'Flathead or Phillips?' I said, 'Surprise me. Either way, "
    "I'm just trying to turn this conversation around.'"
)

MAX_CHARS = 200


def validate(text):
    """Check the entry against the competition gate."""
    if not isinstance(text, str):
        raise ValueError("entry must be text")
    if not (1 <= len(text) <= MAX_CHARS):
        raise ValueError(
            "entry must be 1-200 characters, got %d" % len(text)
        )
    if not text.strip():
        raise ValueError("entry must not be only whitespace")
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be a single line")
    text.encode("utf-8")  # raises if not valid UTF-8
    return text


def entry_path():
    """Resolve the output file path from the environment."""
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    return os.path.join(out_dir, "entry.txt")


def main():
    joke = validate(JOKE)
    path = entry_path()
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(joke)
    print("wrote %s (%d chars)" % (path, len(joke)))


if __name__ == "__main__":
    main()
