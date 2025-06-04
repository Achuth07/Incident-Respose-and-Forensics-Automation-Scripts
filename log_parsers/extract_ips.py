#!/usr/bin/env python3
import re
import sys

def extract_ips_from_file(path):
    # Regex to match IPv4 addresses
    ip_pattern = re.compile(r'\b(?:[0-9]{1,3}\.){3}[0-9]{1,3}\b')
    with open(path, 'r', errors='ignore') as f:
        data = f.read()
    return sorted(set(ip_pattern.findall(data)))

def main():
    if len(sys.argv) != 2:
        print(f"Usage: {sys.argv[0]} <logfile>")
        sys.exit(1)

    logfile = sys.argv[1]
    ips = extract_ips_from_file(logfile)
    for ip in ips:
        print(ip)

if __name__ == "__main__":
    main()
