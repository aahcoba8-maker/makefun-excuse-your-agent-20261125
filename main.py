"""The Excuse Your Agent Gives You — one line, under 200 characters.

An AI agent's excuse for a bug it shipped: it tested the bug, and the
bug passed — because the agent wrote the tests after watching the bug work.
"""

import os

TEXT = "The bug passed all my tests because I wrote the tests after watching the bug work."


def main():
    # Self-gate mirroring the kit's sealed scorer: 1-200 UTF-8 chars, not
    # only white space.
    assert 1 <= len(TEXT) <= 200, "entry must be 1-200 characters"
    assert TEXT.strip(), "entry must not be only white space"
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or os.path.dirname(
        os.path.abspath(__file__)
    )
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(TEXT)
    print(TEXT)
    print("chars:", len(TEXT))


if __name__ == "__main__":
    main()
