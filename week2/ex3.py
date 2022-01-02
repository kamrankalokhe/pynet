import os
from getpass import getpass
from netmiko import ConnectHandler
from pprint import pprint
password = os.getenv("PYNET_PASSWORD") if os.getenv("PYNET_PASSWORD") else getpass()

device = {
    "device_type": "cisco_ios",
    "host":"cisco4.lasthop.io",
    "username":"pyclass",
    "password": password,
    "global_delay_factor":2,
}

cmds = ["show version", "show lldp neighbors"]

net_connect = ConnectHandler(**device)
for cmd in cmds:

    output = net_connect.send_command(cmd,use_textfsm=True)
    print("#" *80)
    print(cmd)
    print("#" *80)
    pprint(output)
    print("#" *80)
    print()
    if cmd == "show lldp neighbors":
        print("Data structure retured by lldp neighbor output :",type(output))
        print("HPE switch connection port : {}".format(output[0]['neighbor_interface']))

print()
net_connect.disconnect()