#! /usr/bin/python
import subprocess
from collections import Counter

f1 = open("balancer-access.log","r")
lines = f1.readlines()
f1.close()

ips = []
for line in lines:
  if "click?pi" in line:
     ips.append(line.split()[0])				
			 
ips.sort()
top = Counter(ips).most_common(1)
print("IP with the most click events is:  " + top[0][0])
