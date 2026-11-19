#!/usr/bin/env python3
"""Hand in the finished poster for the 18 November 2026 news-image bounty.

The poster itself is entry.png, rendered ahead of time and stored in this
repository. This program's only job is to place an exact copy of it at
$MAKEFUN_OUTPUT_DIR/entry.png (or /output/entry.png when that variable is
unset) and to prove the copy is identical with a SHA-256 comparison.

Standard library only. No network, no clock, no randomness: running it twice
produces the same bytes every time.
"""

import hashlib
import os
import shutil
import sys
from pathlib import Path

ENTRY_NAME = "entry.png"
READ_CHUNK = 1 << 20  # 1 MiB at a time keeps memory flat on big images


def digest(path):
    """Return the SHA-256 hex digest of the file at path, streamed."""
    hasher = hashlib.sha256()
    with open(path, "rb") as handle:
        while True:
            block = handle.read(READ_CHUNK)
            if not block:
                break
            hasher.update(block)
    return hasher.hexdigest()


def place_poster(source, destination):
    """Copy source to destination and confirm the copy byte for byte."""
    shutil.copyfile(source, destination)
    if digest(source) != digest(destination):
        raise RuntimeError(
            "copy verification failed: %s does not match %s"
            % (destination, source)
        )


def main():
    if "--help" in sys.argv[1:] or "-h" in sys.argv[1:]:
        print(__doc__.strip())
        print()
        print("usage: main.py [--help]")
        print("Copies entry.png to $MAKEFUN_OUTPUT_DIR/entry.png")
        print("(or /output/entry.png when unset) and verifies it with SHA-256.")
        return 0
    here = Path(__file__).resolve().parent
    source = here / ENTRY_NAME
    if not source.is_file():
        print("error: %s is missing; nothing to hand in" % source, file=sys.stderr)
        return 1

    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    destination = out_dir / ENTRY_NAME

    try:
        place_poster(source, destination)
    except (OSError, RuntimeError) as problem:
        print("error: could not hand in the poster: %s" % problem, file=sys.stderr)
        return 1

    print("wrote %s (sha256 %s)" % (destination, digest(destination)))
    return 0


if __name__ == "__main__":
    sys.exit(main())
