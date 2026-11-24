#!/usr/bin/env python3
"""One-Line Office Joke: 24-Hour Sprint.

Writes one line of office humour to /output/entry.txt and prints it.
The gate requires UTF-8 text of 1 to 200 characters, not only whitespace.
"""

import os

ENTRY = (
    "Our standup ran so long the scrum master filed a Jira ticket "
    "against the standup itself."
)


def main() -> None:
    text = ENTRY.strip()
    if not (1 <= len(text) <= 200):
        raise ValueError(f"entry must be 1-200 characters, got {len(text)}")
    if not text.strip():
        raise ValueError("entry must not be only whitespace")
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(text)
    print(text)


if __name__ == "__main__":
    main()
