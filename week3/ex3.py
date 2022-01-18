import json
from pprint import pprint

ipv4_list = []
ipv6_list = []
filename= 'data.json'
with open(filename,'r') as fh:
    output_data = json.load(fh)

for key in output_data.keys():
    data = output_data[key]
    for key in data.keys():
        if key == 'ipv4' or key == 'ipv6':
            ipv4_data = data[key]
            for k,v in ipv4_data.items():
                ip = k
                prefix_length= v['prefix_length']
                if key == "ipv4":
                    ipv4_list.append("{}/{}".format(ip,prefix_length))
                if key == "ipv6":
                    ipv6_list.append("{}/{}".format(ip,prefix_length))

print("\nIPv4 Addresses: {}\n".format(ipv4_list))
print("\nIPv6 Addresses: {}\n".format(ipv6_list))


            