#! /usr/bin/python
import subprocess
from collections import Counter

f1 = open("balancer-access.log","r")
lines = f1.readlines()
print (lines)
f1.close()

f2 = open("click_lines", "w")
for line in lines:
  if "click" in line:
    f2.write(line)    
f2.close()


f3 = open("click_lines", "r")
clicks = f3.readlines()
f2.close()


f4 = open("ips_lines", "w")
for line in clicks:
  f4.write(line.split()[0]+'\n')
f4.close()

f5 = open("ips_lines", "r")
sorted = f5.readlines()
sorted.sort()
print "print sorted ips:"
print (sorted)

word_counts = Counter(sorted)
top = word_counts.most_common(1)
print(top)
