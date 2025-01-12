#!/usr/bin/env python3
import subprocess
import argparse
import re

def change_mac(interface, new_mac):
    # Bring the interface down
    subprocess.call(["sudo", "ip", "link", "set", "dev", interface, "down"])
    
    # Change the MAC address
    subprocess.call(["sudo", "ip", "link", "set", "dev", interface, "address", new_mac])
    
    # Bring the interface up
    subprocess.call(["sudo", "ip", "link", "set", "dev", interface, "up"])

def get_current_mac(interface):
    result = subprocess.check_output(["ip", "link", "show", interface])
    mac_address_search = re.search(r"(\w\w:\w\w:\w\w:\w\w:\w\w:\w\w)", str(result))
    
    if mac_address_search:
        return mac_address_search.group(0)
    else:
        return None

def main():
    parser = argparse.ArgumentParser(description="Change MAC address of a Linux computer.")
    parser.add_argument("-i", "--interface", required=True, help="Network interface to change the MAC address of.")
    parser.add_argument("-m", "--mac", required=True, help="New MAC address.")
    
    args = parser.parse_args()
    
    current_mac = get_current_mac(args.interface)
    print(f"Current MAC address: {current_mac}")
    
    change_mac(args.interface, args.mac)
    
    updated_mac = get_current_mac(args.interface)
    print(f"Updated MAC address: {updated_mac}")
    
    if current_mac != updated_mac:
        print("MAC address was successfully changed.")
    else:
        print("Failed to change the MAC address.")

if __name__ == "__main__":
    main()
