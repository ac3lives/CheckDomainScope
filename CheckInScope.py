#!/usr/bin/python3
import socket
import argparse
import ipaddress
import sys

parser = argparse.ArgumentParser(description="Check list of IPs or list of Domains if they are in the scope file")
parser.add_argument('scopefile', metavar='scopefile', help='File containing all CIDR ranges in-scope')
parser.add_argument('-dL', dest='domainlist', required=False, help='A list of domains to resolve and check if they are in-scope')
parser.add_argument('-iL', dest='iplist', required=False, help='A list of IP addresses to check against the in-scope list')
args = parser.parse_args()

scopelist = []
try:
        with open(args.scopefile) as readscope:
                for line in readscope:
                        scopelist.append(line.strip())
except:
        print("Error reading scope list:",sys.exc_info()[0])


def check_inscope(ip_to_check):
        for ranges in scopelist:
                if ipaddress.ip_address(ip_to_check) in ipaddress.ip_network(ranges):
                        return True
        return False

def check_domains():
        domain_array = []
        with open(args.domainlist) as domain_list:
                for line in domain_list:
                        domain_array.append(line)

        if domain_array:
                for domain in domain_array:
                        try:
                                ipaddress = socket.gethostbyname(domain.strip())
                                print("Hostname {0}, IPAddress {1}, in scope: {2}".format(domain.strip(), ipaddress, check_inscope(ipaddress)))
                        except:
                                print("Error resolving ", domain)
                                continue
        else:
                print("Error: No domains loaded from ", domainlist)

def check_iplist():
        ip_list = []
        with open(args.iplist) as readips:
                for line in readips:
                        ip_list.append(line)

        if ip_list:
                for ipaddr in ip_list:
                        print("IP Address {0}, in scope: {1}".format(ipaddr, check_inscope(ipaddr)))
        else:
                print("Error: No IP Addresses loaded from", iplist)

          
if args.domainlist:
        check_domains()
elif args.iplist:
        check_iplist()
else:
        print("Error: Please select from IP List (-iL) or Domain List (-dL)")
