#!/usr/bin/env python3
"""Office Joke Open entry: write one line of office comedy to /output/entry.txt."""

import os

JOKE = "My calendar is so full the only free slot is titled 'Focus Time' — which my boss just booked to ask why I never have any focus time."

def main():
    if not 1 <= len(JOKE) <= 200:
        raise SystemExit("joke must be 1-200 characters")
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(JOKE)
    print(JOKE)

if __name__ == "__main__":
    main()
