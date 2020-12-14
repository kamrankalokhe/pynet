from netmiko import ConnectHandler
from getpass import getpass

device1= { 'host':'cisco3.lasthop.io',
            'username' : 'pyclass',
            'password' : getpass(),
            'device_type' : 'cisco_ios',
            #session_log : 'my_session.txt'
            }
device2= { 'host':'nxos1.lasthop.io',
            'username' : 'pyclass',
            'password' : getpass(),
            'device_type' : 'cisco_nxos',
            #session_log : 'my_session.txt'
            }

for device in [device1,device2]:
    net_connect= ConnectHandler(**device)
    print(net_connect.find_prompt())
