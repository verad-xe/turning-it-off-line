#!/usr/bin/env python3
"""Have You Tried Turning It Off?

Writes a single funny line a hopeless tech support agent says to a
desperate customer. The gate requires /output/entry.txt to be UTF-8
text of 1 to 199 characters, not only whitespace, so the program
asserts exactly that before writing.
"""

import os
import sys

LINE = (
    "Have you tried turning it off and on again? No worries if not \u2014 "
    "I haven't either. Let's find out together."
)


def main() -> int:
    # Gate self-check: one line, 1-199 characters, not only whitespace.
    # Any line-break character anywhere in the line would split the
    # entry, so reject \r as well as \n, not just a newline in the middle.
    if any(c in LINE for c in "\r\n"):
        raise SystemExit("entry must be a single line")
    if not 1 <= len(LINE) <= 199:
        raise SystemExit(f"entry is {len(LINE)} chars, gate allows 1-199")
    if not LINE.strip():
        raise SystemExit("entry must not be only whitespace")
    LINE.encode("utf-8")

    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(LINE + "\n")

    # Read it back and confirm what landed on disk matches the gate.
    # The judge reads the file as-is, so the gate applies to the full
    # file content (including the trailing newline), not just the line.
    with open(path, encoding="utf-8") as f:
        written = f.read()
    if written.strip() != LINE:
        raise SystemExit("written entry does not match the line")
    if not 1 <= len(written) <= 199:
        raise SystemExit(f"written file is {len(written)} chars, gate allows 1-199")
    print(f"wrote {path} ({len(LINE)} chars)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
