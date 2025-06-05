#!/usr/bin/env python3
from Evtx.Evtx import Evtx
import re
import sys

def extract_ips_from_evtx(evtx_path):
    # same IPv4 regex as before
    ip_pattern = re.compile(r'\b(?:[0-9]{1,3}\.){3}[0-9]{1,3}\b')
    ips = set()

    with Evtx(evtx_path) as log:
        for record in log.records():
            xml = record.xml()                 # raw XML string of one event
            for match in ip_pattern.findall(xml):
                ips.add(match)

    return sorted(ips)

def main():
    if len(sys.argv) != 2:
        print(f"Usage: {sys.argv[0]} <path_to_evtx>")
        sys.exit(1)

    ips = extract_ips_from_evtx(sys.argv[1])
    for ip in ips:
        print(ip)

if __name__ == "__main__":
    main()
