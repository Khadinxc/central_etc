#!/bin/bash
#
#Created for TCM Academy Practical Ethical Hacker course

for ip in $(cat ips.txt); do nmap $ip; done >portscanner.txt