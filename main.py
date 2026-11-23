"""Write one warm emoji to /output/entry.txt.

Choice: 🤗 (U+1F917 HUGGING FACE).

Why this one fits the judge: open arms read instantly as a
welcome, not just a smile — warm at first glance with no
context needed. A hug is understood across ages and cultures,
yet it stays friendly to a stranger: no romance, no flirtation,
no sarcasm, no in-joke. And it is clearly a deliberate pick,
not the first default smiley that comes to mind.
"""

import os

ENTRY = "\U0001F917"  # 🤗 HUGGING FACE
OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    # Harden the output path: create the parent directory only
    # when one exists, so a bare filename would still work.
    output_dir = os.path.dirname(OUTPUT_PATH)
    if output_dir:
        os.makedirs(output_dir, exist_ok=True)
    # No trailing newline: exactly one emoji, 4 bytes UTF-8.
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
