import os
import time
from scapy.all import *

# DNS Configuration
def set_dns(server):
    # Determine the operating system
    if os.name == 'nt':
        # Windows
        command = f'netsh interface ip set dns name="Wi-Fi" static {server} primary'
    else:
        # Linux/macOS
        command = f'networksetup -setdnsservers Wi-Fi {server}'

    # Execute the command
    os.system(command)
    print(f'DNS server set to {server}')


# DHCP Configuration
class DhcpPacketHandler:
    def handle_dhcp_packet(self, packet):
        if DHCP in packet and packet[DHCP].options[0][1] == 1:  # Check DHCP message type (1 for DHCP Discover)
            print("DHCP Discover received")
            print(f"Client MAC: {packet[Ether].src}")
            # Extract VLAN ID from 802.1Q tag if present
            vlan_id = None
            if Dot1Q in packet:
                vlan_id = packet[Dot1Q].vlan

            # Check if the packet is from the specific VLAN
            if vlan_id == 100:
                print("DHCP request from VLAN 100 detected!")
                # Add your custom actions here
                # For example, send a DHCP Offer packet or perform other operations


def start_dhcp_listener():
    print("Starting DHCP listener...")
    dhcp_handler = DhcpPacketHandler()
    sniff(filter="udp and (port 67 or port 68)", prn=dhcp_handler.handle_dhcp_packet, store=0)


# Main Program
def main():
    # Replace 'x.x.x.x' with the desired DNS server IP address
    dns_server = 'x.x.x.x'
    set_dns(dns_server)

    start_dhcp_listener()


if __name__ == '__main__':
    main()
