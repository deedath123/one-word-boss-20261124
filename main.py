"""One Word for the Boss — make.fun entry.

Writes the single entry word MEETINGHOLIC to entry.txt.
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
