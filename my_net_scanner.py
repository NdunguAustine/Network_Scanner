import scapy.all as scapy

arp_request_packet = scapy.ARP(pdst="192.168.100.1/24")
