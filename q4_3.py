#!usr/bin/python3

import nmap
import os

# Perform an IPv6 network scan using Nmap
target_network = "103.25.231.122"
nm = nmap.PortScanner()
nm.scan(hosts=target_network, arguments='-6')

# Parse the Nmap results to identify open ports
c = 0
for host in nm.all_hosts():
    print('host:' + str(host))
    all_ports = nm[host]['tcp']
    for port in all_ports.keys():
        d = (all_ports[port])
        if d['state'] == 'open':
            print('For host {}, found open port: {}'.format(host, port))

if(c==0):
    print("no ipv6 device found")

# Scan for other vulnerabilities:

# For demo purposes using ipv4:
print("for ipv4 device: ")
target_network = "127.0.0.1"

# Perform an IPv6 network scan using Nmap
nm = nmap.PortScanner()
nm.scan(hosts=target_network)

# Parse the Nmap results to identify open ports
for host in nm.all_hosts():
    print('host:' + str(host))
    all_ports = nm[host]['tcp']
    for port in all_ports.keys():
        d = (all_ports[port])
        if d['state'] == 'open':
            print('For host {}, found open port: {}'.format(host, port))

print(os.system('nmap -6 localhost'))

print(os.system('nmap -sV -6 --script vulners localhost'))

print(os.system('nmap -sV -6 --script=vulscan/vulscan.nse localhost'))