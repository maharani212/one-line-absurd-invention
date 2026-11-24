#!/usr/bin/env python3
"""Write one short text to /output/entry.txt.

The text is hardcoded (no network) and written deterministically,
exactly as-is, with no trailing newline.
"""

TEXT = 'A fridge light that dims itself in silent judgment when you open the door at 2am, so at least the shame is shared.'


def main() -> None:
    import os

    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()
