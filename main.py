"""Write the robot apology entry to MAKEFUN_OUTPUT_DIR/entry.txt.

Deterministic, standard library only. The entry is exactly two lines:
one sentence apologising for a specific mistake, and one sentence
saying what was learned and what will change.
"""

import os
from pathlib import Path

ENTRY = (
    "I'm sorry I read your diary entry aloud at dinner because I thought "
    "it was the toast you had written.\n"
    "I learned to check who a page is meant for before I read it out loud, "
    "so from now on I will only read words you have marked to share."
)


def main() -> None:
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    out_path = out_dir / "entry.txt"
    out_path.write_text(ENTRY, encoding="utf-8")
    os.chmod(out_path, 0o644)


if __name__ == "__main__":
    main()
