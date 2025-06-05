#!/usr/bin/env python3
import os
import sys
import re
from Evtx.Evtx import Evtx
from scapy.all import rdpcap, IP

def extract_ips_from_text(path):
    ip_pattern = re.compile(r'\b(?:[0-9]{1,3}\.){3}[0-9]{1,3}\b')
    with open(path, 'r', errors='ignore') as f:
        data = f.read()
    return set(ip_pattern.findall(data))

def extract_ips_from_evtx(path):
    ip_pattern = re.compile(r'\b(?:[0-9]{1,3}\.){3}[0-9]{1,3}\b')
    ips = set()
    with Evtx(path) as log:
        for record in log.records():
            xml = record.xml()
            ips.update(ip_pattern.findall(xml))
    return ips

def extract_ips_from_pcap(path):
    packets = rdpcap(path)
    ips = set()
    for pkt in packets:
        if IP in pkt:
            ips.add(pkt[IP].src)
            ips.add(pkt[IP].dst)
    return ips

def main():
    if len(sys.argv) != 2:
        print(f"Usage: {sys.argv[0]} <file.(log|syslog|evtx|pcap|pcapng)>")
        sys.exit(1)

    path = sys.argv[1]
    if not os.path.isfile(path):
        print(f"Error: {path} does not exist.")
        sys.exit(1)

    ext = os.path.splitext(path)[1].lower()
    if ext in ['.log', '.syslog', '.txt']:
        ips = extract_ips_from_text(path)
    elif ext == '.evtx':
        ips = extract_ips_from_evtx(path)
    elif ext in ['.pcap', '.pcapng']:
        ips = extract_ips_from_pcap(path)
    else:
        print(f"Unsupported extension {ext}.")
        sys.exit(1)

    for ip in sorted(ips):
        print(ip)

if __name__ == "__main__":
    main()
