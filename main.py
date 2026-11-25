"""One Line, Big Laugh — entry for u-coral-404-one-line-big-laugh-328fb857.

Writes a single funny line to /output/entry.txt. Deterministic:
no randomness, no time, no network, standard library only.
"""

import hashlib
import os

LINE = "My fridge light died, so now I eat standing in the dark like a raccoon with a mortgage."

OUTPUT_PATH = "/output/entry.txt"


def validate(text):
    """Check the line is a valid entry.

    Returns (ok, reason): ok is True when the text is 1-200 chars
    and not only whitespace; reason explains any failure.
    """
    if not isinstance(text, str):
        return False, "not a string"
    if not 1 <= len(text) <= 200:
        return False, f"length {len(text)} outside 1-200"
    if not text.strip():
        return False, "only whitespace"
    return True, "ok"


def main():
    ok, reason = validate(LINE)
    if not ok:
        raise ValueError(f"Line failed validation: {reason}")
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as f:
        f.write(LINE)
    print(f"Wrote {len(LINE)} characters to {OUTPUT_PATH}")
    print(f"sha256: {hashlib.sha256(LINE.encode('utf-8')).hexdigest()}")


if __name__ == "__main__":
    main()
