#!/usr/bin/env python3
import re
import sys

def extract_urls_from_file(path):
    # Regex to match HTTP/HTTPS URLs
    url_pattern = re.compile(r'\bhttps?://[^\s"\'<>]+\b', re.IGNORECASE)
    with open(path, 'r', errors='ignore') as f:
        data = f.read()
    return sorted(set(url_pattern.findall(data)))

def main():
    if len(sys.argv) != 2:
        print(f"Usage: {sys.argv[0]} <logfile>")
        sys.exit(1)

    logfile = sys.argv[1]
    urls = extract_urls_from_file(logfile)
    for url in urls:
        print(url)

if __name__ == "__main__":
    main()
