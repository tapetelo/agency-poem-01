"""Write one fixed poem about agency to /output/entry.txt.

Outside the grader's container, MAKEFUN_OUTPUT_DIR stands in for /output:
    mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py

The program is deterministic: it writes the same bytes on every run.
Standard library only; no network.
"""

import os
from pathlib import Path

OUTPUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")

POEM_LINES = [
    "The Braid",
    "",
    "My mother braided my hair every morning",
    "before school, her fingers quick and sure,",
    "the part straight as a ruler, the braid tight",
    "enough to last the whole day through.",
    "I sat still for it. I hated sitting still.",
    "",
    "She is gone now. My daughter is seven.",
    "The mornings are a rush of shoes and toast,",
    "and the agent braids her hair instead.",
    "It parts it straight. It plaits it tight.",
    "It does not pull. She sits still for it.",
    "",
    "This morning I told it to wait.",
    "I took the brush. My part wandered.",
    "The braid came loose halfway down,",
    "the way mine always did at seven.",
    "It offered to fix it. I said, No.",
    "She turned in the chair. She looked in the mirror.",
    "She said, Again. Like Grandma used to.",
    "",
    "I did it again, slower, my fingers",
    "remembering what my mother's knew.",
    "The part wandered. The braid slipped.",
    "She sat still for it, the way I never could.",
]

POEM = "\n".join(POEM_LINES) + "\n"


def main() -> None:
    out = Path(OUTPUT_DIR) / "entry.txt"
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(POEM, encoding="utf-8")


if __name__ == "__main__":
    main()
