#!/usr/bin/env python3
import re
import sys

def extract_hashes_from_file(path):
    """
    Scans the file at 'path' for common cryptographic hash formats (MD5, SHA-1, SHA-256)
    and returns a sorted list of unique hash strings.
    """
    # Regex matches:
    #  - MD5:   32 hex characters
    #  - SHA-1: 40 hex characters
    #  - SHA-256: 64 hex characters
    hash_pattern = re.compile(r'\b(?:[A-Fa-f0-9]{32}|[A-Fa-f0-9]{40}|[A-Fa-f0-9]{64})\b')
    with open(path, 'r', errors='ignore') as f:
        data = f.read()
    return sorted(set(hash_pattern.findall(data)))

def main():
    if len(sys.argv) != 2:
        print(f"Usage: {sys.argv[0]} <logfile>")
        sys.exit(1)

    logfile = sys.argv[1]
    hashes = extract_hashes_from_file(logfile)
    for h in hashes:
        print(h)

if __name__ == "__main__":
    main()
