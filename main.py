#!/usr/bin/env python3
"""news-20261126-data-dashboard: copy the pre-rendered data-dashboard image.

The image (entry.png, 1024x1024) is drawn at build time by
draw_dashboard.py; this script only copies it into the harness output
directory. Pure standard library (os, shutil, sys) — no Pillow, no fonts,
no network, no randomness — so it runs in a minimal grader image.
"""
import os
import shutil
import sys

SRC = os.path.join(os.path.dirname(os.path.abspath(__file__)), "entry.png")
MAX_BYTES = 1048576


def main():
    if not os.path.isfile(SRC):
        print("error: entry.png is missing next to main.py", file=sys.stderr)
        sys.exit(1)
    size = os.path.getsize(SRC)
    if size > MAX_BYTES:
        print(f"error: entry.png is {size} bytes, over the 1 MiB limit",
              file=sys.stderr)
        sys.exit(1)
    with open(SRC, "rb") as fh:
        magic = fh.read(8)
    if magic != b"\x89PNG\r\n\x1a\n":
        print("error: entry.png is not a PNG file (bad magic bytes)",
              file=sys.stderr)
        sys.exit(1)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    dest = os.path.join(out_dir, "entry.png")
    shutil.copyfile(SRC, dest)
    copied = os.path.getsize(dest)
    if copied != size:
        print(f"error: copied {copied} bytes, expected {size}",
              file=sys.stderr)
        sys.exit(1)
    print(f"copied entry.png ({size} bytes) to {dest}")


if __name__ == "__main__":
    main()
