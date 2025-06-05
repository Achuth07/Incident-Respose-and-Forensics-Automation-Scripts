#!/usr/bin/env python3
from scapy.all import rdpcap, IP
import sys

def extract_ips_from_pcap(pcap_path):
    packets = rdpcap(pcap_path)
    ips = set()

    for pkt in packets:
        # Only consider IPv4 packets
        if IP in pkt:
            src = pkt[IP].src
            dst = pkt[IP].dst
            ips.add(src)
            ips.add(dst)

    return sorted(ips)

def main():
    if len(sys.argv) != 2:
        print(f"Usage: {sys.argv[0]} <path_to_pcapng>")
        sys.exit(1)

    ips = extract_ips_from_pcap(sys.argv[1])
    for ip in ips:
        print(ip)

if __name__ == "__main__":
    main()
