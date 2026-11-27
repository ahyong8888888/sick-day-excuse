#!/usr/bin/env python3
"""The funniest sick-day excuse.

Prints the entry line and writes it to output/entry.txt (and to
/output/entry.txt when that directory is writable), for make.fun's
"The Funniest Sick-Day Excuse" bounty.
"""
import os

LINE = "Can't come in today, my cat learned to open the front door and has been standing in the hallway staring at me for three hours. I'm not sick, I'm just scared to leave the house."


def main():
    here = os.path.dirname(os.path.abspath(__file__))
    out_dir = os.path.join(here, "output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(LINE + "\n")
    try:
        os.makedirs("/output", exist_ok=True)
        with open("/output/entry.txt", "w", encoding="utf-8") as f:
            f.write(LINE + "\n")
    except OSError:
        pass
    print(LINE)


if __name__ == "__main__":
    main()
