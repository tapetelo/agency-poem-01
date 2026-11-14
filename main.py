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
    "The Crossed-Out Word",
    "",
    "When my brother stopped speaking to me",
    "it was over a fence line, twenty years ago.",
    "I wrote him three letters in that time.",
    "Each one began I'm sorry and ended",
    "with a line I crossed out.",
    "",
    "Last winter the agent drafted the fourth.",
    "It read our old messages, his voice",
    "in every line, and wrote the letter",
    "I would have written if I were kind",
    "and patient and never tired.",
    "It was perfect. I did not send it.",
    "",
    "Instead I sat at the kitchen table",
    "with the pen he gave me when I turned eighteen,",
    "the one that leaks if you hold it wrong.",
    "I wrote I'm sorry. I crossed out",
    "the next line twice, and the third once,",
    "and signed my name the way I did",
    "when we were boys, the y looping low.",
    "",
    "I posted it myself, in the rain,",
    "at the box on the corner. The ink",
    "had already started to run.",
    "He wrote back on the envelope,",
    "in his own hand: Come home. The fence",
    "can wait. And underneath, in smaller script:",
    "Keep the crossed-out word.",
]

POEM = "\n".join(POEM_LINES) + "\n"


def main() -> None:
    out = Path(OUTPUT_DIR) / "entry.txt"
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(POEM, encoding="utf-8")


if __name__ == "__main__":
    main()
