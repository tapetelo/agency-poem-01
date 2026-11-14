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
    "The Handful",
    "",
    "A handful of barley. That is the whole recipe.",
    "My grandmother wrote it in pencil, in her hand:",
    "a knob of butter, salt until it tastes",
    "like Tuesday, cook until the kitchen smells done.",
    "",
    "She died in March. The card stayed in the drawer",
    "with the rubber bands and the spare keys,",
    "the pencil getting fainter every time",
    "I opened it to look and put it back.",
    "",
    "Last month the agent read it for me.",
    "It weighed the handful. It timed the done.",
    "It made the soup in a clean white pot",
    "and ladled it into the good bowl.",
    "It was flawless. It tasted like a photograph.",
    "",
    "Tonight I made it myself.",
    "I burned the bottom. The barley stuck.",
    "The kitchen filled with smoke, and under it,",
    "for the first time in a year, the smell of her.",
    "",
    "I ate it standing up, the way she did,",
    "scraping the good part off the burned part.",
    "It was wrong in all the ways she was.",
    "And it was hers.",
]

POEM = "\n".join(POEM_LINES) + "\n"


def main() -> None:
    out = Path(OUTPUT_DIR) / "entry.txt"
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(POEM, encoding="utf-8")


if __name__ == "__main__":
    main()
