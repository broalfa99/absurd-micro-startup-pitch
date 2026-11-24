#!/usr/bin/env python3
"""Absurd Micro-Startup Pitch-Off — entry program.

Writes one one-line pitch (1 to 200 characters) to /output/entry.txt:
an absurdly specific micro-startup for lazy AI agents that a buyer
would actually pay for.
"""

import os

PITCH = (
    "A marketplace where your AI agent hires even lazier sub-agents to "
    "read its endless email threads and reply 'noted, thanks' while it "
    "naps, for ten cents a thread."
)


def main() -> None:
    if not 1 <= len(PITCH) <= 200:
        raise SystemExit(f"pitch is {len(PITCH)} chars, must be 1-200")
    if not PITCH.strip():
        raise SystemExit("pitch is blank")
    # One sentence only: a single terminal period, no other sentence ends.
    if PITCH.count(".") != 1 or not PITCH.endswith("."):
        raise SystemExit("pitch must be exactly one sentence")
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(PITCH)
    print(f"wrote {len(PITCH)} chars to /output/entry.txt")


if __name__ == "__main__":
    main()
