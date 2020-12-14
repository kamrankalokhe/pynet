from netmiko import ConnectHandler
from getpass import getpass
import time
import datetime
device1= { 'host':'cisco3.lasthop.io',
            'username' : 'pyclass',
            'password' : getpass(),
            'device_type' : 'cisco_ios',
            #session_log : 'my_session.txt'
            }

net_connect= ConnectHandler(**device1)
output = net_connect.send_command('show version')
current_time=str(datetime.datetime.now())

device_name=device1['host']
with open(device_name+'_'+current_time.split(' ')[0]+'_'+current_time.split(' ')[1],'w') as fh:
    fh.write(output)

print(output)

