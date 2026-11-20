#!/usr/bin/env python3
"""news-image-20261120 entry: copy the front page to /output/entry.png.

The entry image is the newspaper front page this repository holds as
entry.png: "The World in One Day" for Friday, 20 November 2026, drawn
in-session for this competition (37 verified stories, dated masthead,
illustrated hero, by-the-numbers strip, sources footer).

Standard library only. The program is deterministic: it copies bytes,
so two runs write identical output.
"""
import os
import struct
import sys

PNG_SIGNATURE = b"\x89PNG\r\n\x1a\n"
MAX_BYTES = 1048576
EXPECT_W, EXPECT_H = 1024, 1024


def repo_dir():
    return os.path.dirname(os.path.abspath(__file__))


def output_dir():
    return os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")


def check_png_complete(data):
    """Walk the chunk list: every chunk must be whole, ending in IEND."""
    pos = 8
    seen_iend = False
    while pos + 8 <= len(data):
        length = struct.unpack(">I", data[pos:pos + 4])[0]
        ctype = data[pos + 4:pos + 8]
        end = pos + 12 + length
        if end > len(data):
            raise SystemExit("entry.png has a truncated %r chunk" % ctype)
        if ctype == b"IEND":
            seen_iend = True
            if end != len(data):
                raise SystemExit("entry.png has data after IEND")
            break
        pos = end
    if not seen_iend:
        raise SystemExit("entry.png has no IEND chunk")
    return True


def read_png(path):
    with open(path, "rb") as fh:
        data = fh.read()
    if len(data) > MAX_BYTES:
        raise SystemExit("entry.png exceeds 1 MiB: %d bytes" % len(data))
    if data[:8] != PNG_SIGNATURE:
        raise SystemExit("entry.png is not a PNG file")
    if len(data) < 33 or data[12:16] != b"IHDR":
        raise SystemExit("entry.png has no IHDR chunk")
    width, height = struct.unpack(">II", data[16:24])
    if (width, height) != (EXPECT_W, EXPECT_H):
        raise SystemExit("entry.png is %dx%d, expected 1024x1024" % (width, height))
    if data[24] != 8 or data[25] != 2:
        raise SystemExit("entry.png must be 8-bit RGB")
    check_png_complete(data)
    return data


def main(argv):
    src = os.path.join(repo_dir(), "entry.png")
    data = read_png(src)
    if "--check-only" in argv:
        print("entry.png OK: %d bytes, 1024x1024, valid PNG" % len(data))
        return 0
    out = output_dir()
    os.makedirs(out, exist_ok=True)
    dest = os.path.join(out, "entry.png")
    with open(dest, "wb") as fh:
        fh.write(data)
    # Verify the copy byte for byte: a run must reproduce the image exactly.
    with open(dest, "rb") as fh:
        written = fh.read()
    if written != data:
        raise SystemExit("verification failed: written bytes differ")
    print("wrote %s (%d bytes)" % (dest, len(data)))
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
