#!/usr/bin/env python3
"""Writes one line of honest error copy to /output/entry.txt.

The auth bug: the user's password is correct, but the server lost the
session / misplaced the credentials. The error confesses the system is
at fault, not the user.
"""

import os

LINE = (
    "Your password was right. We lost it. "
    "Somewhere between the database and the login button, our server "
    "misplaced your session \u2014 please sign in again while we check "
    "behind the couch cushions."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
