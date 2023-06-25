import os
import time
from pydhcplib.dhcp_packet import *
from pydhcplib.dhcp_network import *

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
class MyDhcpApp(DhcpNetworkApp):
    def __init__(self):
        DhcpNetworkApp.__init__(self, "dhcp.conf")

    def handleDhcpDiscover(self, packet):
        print("DHCP Discover received")
        print(f"Client MAC: {packet.GetHardwareAddress()}")
        print("Sending DHCP Offer")

        dhcp_offer = DhcpPacketOffer()
        dhcp_offer.SetOption('server_id', '192.168.1.1')
        dhcp_offer.SetOption('lease_time', 86400)
        dhcp_offer.SetOption('subnet_mask', '255.255.255.0')
        dhcp_offer.SetOption('router', '192.168.1.1')
        dhcp_offer.SetOption('domain_name_server', '8.8.8.8')

        self.SendDhcpPacket(dhcp_offer)

    def handleDhcpRequest(self, packet):
        print("DHCP Request received")
        print(f"Client MAC: {packet.GetHardwareAddress()}")
        print(f"Offered IP: {packet.GetOptionValue('requested_ip')}")
        print("Sending DHCP Ack")

        dhcp_ack = DhcpPacketAck()
        dhcp_ack.SetOption('server_id', '192.168.1.1')
        dhcp_ack.SetOption('lease_time', 86400)
        dhcp_ack.SetOption('subnet_mask', '255.255.255.0')
        dhcp_ack.SetOption('router', '192.168.1.1')
        dhcp_ack.SetOption('domain_name_server', '8.8.8.8')

        self.SendDhcpPacket(dhcp_ack)


def start_dhcp_server():
    print("Starting DHCP server...")
    my_dhcp_app = MyDhcpApp()
    my_dhcp_app.Start()
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        print("Stopping DHCP server...")
        my_dhcp_app.Stop()


# Main Program
def main():
    # Replace 'x.x.x.x' with the desired DNS server IP address
    dns_server = 'x.x.x.x'
    set_dns(dns_server)

    start_dhcp_server()


if __name__ == '__main__':
    main()
