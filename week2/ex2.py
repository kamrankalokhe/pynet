import os
from getpass import getpass
from netmiko import ConnectHandler
from datetime import datetime

password = os.getenv("PYNET_PASSWORD") if os.getenv("PYNET_PASSWORD") else getpass()
device = {
    "device_type": "cisco_nxos",
    "host": "nxos2.lasthop.io",
    "username": "pyclass",
    "password": password,
    "global_delay_factor":2,
}
net_connect = ConnectHandler(**device)
command = "show lldp neighbors detail"
start_time= datetime.now()
output= net_connect.send_command(command)
end_time= datetime.now()
print("*" * 80)
print(output)
print("*" * 80)
print("\n\n Execution Time: {}".format(end_time-start_time))

command = "show lldp neighbors detail"
start_time= datetime.now()
output= net_connect.send_command(command,delay_factor=8)
net_connect.disconnect()
end_time=datetime.now()
print("#" * 80)
print(output)
print("$" * 80)
print("\n\n Execution Time: {}".format(end_time-start_time))
print()
