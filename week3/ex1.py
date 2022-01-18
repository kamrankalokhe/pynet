
from pprint import pprint

arp_list = []
with open('arp_data.txt','r') as fh:
    for line in fh:
        line = line.strip()
        if line.startswith('Internet'):
             _,ip,_,mac,_,intf = line.split()
             arp_dict = {"ip_addr":ip, "mac_addr":mac,"interface":intf}
             arp_list.append(arp_dict)

pprint(arp_list)


            