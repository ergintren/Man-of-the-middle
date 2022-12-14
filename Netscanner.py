import scapy.all as scapy
from scapy_http import http
import optparse

def user_input():
    parse = optparse.OptionParser()
    parse.add_option("-i","--ip",dest="ip",help="Network scanner")
    (user_input,argumetnts) = parse.parse_args()
    return user_input


def Scan(ip):
    arp_request = scapy.ARP(pdst=ip)
    brodcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
    combined = brodcast/arp_request
    (answered,unanswered) = scapy.srp(combined,timeout=1)
    answered.summary()

ip_adres = user_input
Scan(user_input.ip)