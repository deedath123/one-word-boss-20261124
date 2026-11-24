"""One Word for the Boss — make.fun entry.

Writes the single entry word MEETINGHOLIC to entry.txt.

Verified 2026-11-24: entry.txt is exactly "MEETINGHOLIC"
(12 chars / 12 bytes, no trailing newline), byte-identical across
3 fresh runs + 1 clean-env run (env -i python3 -P -s main.py).
entry.txt sha256:
0e435f162a7e02011a530321507ea0603df0cc55fa44e4afefeac3905f66f2dc
"""

import os
from pathlib import Path

WORD = "MEETINGHOLIC"


def main() -> None:
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    output_path = Path(output_dir) / "entry.txt"
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(WORD, encoding="utf-8")


if __name__ == "__main__":
    main()
