import subprocess
import re

ping_output = subprocess.check_output(f'ping -c1 192.168.3.56', shell=True).decode("utf-8") 
# print(ping_output.split("\n"))
# ping_output = 'PING 192.168.3.56 (192.168.3.56) 56(84) bytes of data.\n64 bytes from 192.168.3.56: icmp_seq=1 ttl=62 time=2.01 ms\n\n--- 192.168.3.56 ping statistics ---\n1 packets transmitted, 1 received, 0% packet loss, time 0ms\nrtt min/avg/max/mdev = 2.006/2.006/2.006/0.000 ms\n'
if 'ttl' in ping_output:
    # print(1)
    # print(ping_output)
    ttl = re.search('ttl=(.*)\stime', ping_output).group(1)
    print(ttl)
