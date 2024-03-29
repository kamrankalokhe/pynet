from netmiko import ConnectHandler
from getpass import getpass

device1 = {
    "host":'cisco3.lasthop.io',
    "username":"pyclass",
    "password":getpass(),
    "device_type":"cisco_ios",
    #"global_delay_factor": 2
}

net_connect=ConnectHandler(**device1)
print(net_connect.find_prompt())

output = net_connect.send_command("show ip interface brief", delay_factor=5)
print(output)

net_connect.disconnect()
