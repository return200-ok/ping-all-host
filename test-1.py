from concurrent.futures import ThreadPoolExecutor as tpe, as_completed
from subprocess import check_output
import re 

first_octets = '192.168.3.'

def ping(last_octests):
    ping_output = check_output(f'ping -c1 {first_octets}{last_octests}', shell=True).decode("utf-8") 
    line = ping_output.split('\n')[1]
    if 'ttl' in line:
        ttl = re.search('ttl=(.*)\stime', line).group(1)
        x = int(ttl)
        if 1 <= x <= 64:
            result = 'Linux'
        if 65 <= x <= 128:
            result = 'Windows'
        if 129 <= x <= 255:
            result = 'AIX'
    return f'{first_octets}{last_octests} is {result}'

# with tpe(50) as exec:
#     for result in exec.map(ping, range(255)):
#         print(result)
print(ping(56))