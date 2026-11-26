"""The Absurd Clause Contest — a make.fun bounty entry.

This program ships a single absurd clause, written to read like
deadpan terms-of-service boilerplate until the absurdity lands:
the Company's mascot, a goose named Legal, holds a right of
entry to inspect your home for compliance. Running it writes
the clause to /output/entry.txt.
"""

import os

# The clause itself: one sentence, 172 characters, under the 200 cap.
ENTRY = "Section 22.4: the user acknowledges that the Company's mascot, a goose named Legal, may enter the user's home at any reasonable hour to inspect compliance with these terms."


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
