"""Cat Reviews Its Human — one funny single-line one-star review.

Writes exactly one line to /output/entry.txt: a house cat's one-star
review of the human it lives with. Pure stdlib (os only), deterministic.
"""

import os

TEXT = "One star. He sits in my sunbeam all day, types on my warm laptop, and gets paid for it."


def main():
    # Gate self-checks (mirror the sealed scorer): 1-200 chars, not only
    # whitespace, a single line, no leading/trailing whitespace.
    if not (1 <= len(TEXT) <= 200):
        raise SystemExit("entry must be 1-200 characters, got %d" % len(TEXT))
    if not TEXT.strip():
        raise SystemExit("entry must not be only whitespace")
    if "\n" in TEXT or "\r" in TEXT:
        raise SystemExit("entry must be a single line")
    if TEXT != TEXT.strip():
        raise SystemExit("entry must not start or end with whitespace")

    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(TEXT)

    # Post-write verification: re-read the file and prove the bytes on disk
    # are exactly the intended text — a silent short write or an encoding
    # slip must fail loudly here instead of reaching the judge.
    with open(path, "rb") as f:
        raw = f.read()
    if raw.decode("utf-8") != TEXT:
        raise SystemExit("post-write check failed: file text differs")
    if raw != TEXT.encode("utf-8"):
        raise SystemExit("post-write check failed: file bytes differ")
    if len(raw) != len(TEXT.encode("utf-8")):
        raise SystemExit("post-write check failed: file length differs")

    print("wrote %d chars to %s" % (len(TEXT), path))


if __name__ == "__main__":
    main()
