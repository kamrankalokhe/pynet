import yaml
from pprint import pprint

#device_name, host (i.e. FQDN), username, and password
dev1 = {'device_name':'cisco3','host':"cisco3.lasthop.io"}
dev2 = {'device_name':'cisco4','host': "cisco4.lasthop.io"}
dev3 = {'device_name': "arista1",'host': "arista1.lasthop.io"}
dev4 = {'device_name': "arista2",'host': "arista2.lasthop.io"}

devices = [dev1,dev2,dev3,dev4]

for device in devices:
    device['username'] = 'admin'
    device["password"] = 'cisco123'

print()
pprint(devices)
print()

with open('my_devices1.yml', 'w') as f:
    yaml.dump(devices,f, default_flow_style=False)