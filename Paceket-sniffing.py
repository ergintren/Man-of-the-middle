import scapy.all as sc
from scapy_http import http
import optparse as op

def user_input():
    parse = op.OptionParser()
    parse.add_option("-i","--iface",dest="iface")
    (user_inputs,arguments) = parse.parse_args()
    return user_inputs

def listen_packet(interface):
    sc.sniff(iface=interface,store=False,prn=packet_analyz)

def packet_analyz(packet):
    #packet.show()
    if packet.haslayer(http.HTTPRequest):
        if packet.haslayer(sc.Raw):
            print(packet[sc.Raw].load)

user_inputs = user_input()
listen_packet(user_inputs.iface)

