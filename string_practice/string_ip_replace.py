import subprocess
import re

# Fetching ip config date in window through below command.
ipconfig_output = (subprocess.getoutput('ipconfig'))

# Iterating through each line of string and taking lines having Ipv4 Ip.
for line in ipconfig_output.splitlines():
    if 'IPv4' in line:
        ip = re.search(r'(\d+){0,3}\.(\d+){0,3}\.(\d+){0,3}\.(\d+){0,3}', line)
        print('The ip of machine is {}'.format(ip.group()))
        break

# changing first octet of ips

ip_list = ['10.10.10.1', '12.12.12.1', '13.13.13.1']
for item in ip_list:
    ip_oct = item.split('.')
    ip_oct[0] = "80"
    print(ip_oct)
    (' ').join(ip_oct)

"""
string.replace(new_Str, old_str, count_nO)


"""

string1 = "this is check of replace function and result"

string2 = string1.replace('and', '&')

print('String after replacement \n{string_new}'.format(string_new=string2))
