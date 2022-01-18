import json
from pprint import pprint

with open('arista_arp.json','r') as fh:
    arp_data = json.load(fh)

arp_dict= dict()

arp_entries = arp_data["ipV4Neighbors"]

for element in arp_entries:
    arp_dict[element['address']] = element['hwAddress']

print()
pprint(arp_dict) 
print()