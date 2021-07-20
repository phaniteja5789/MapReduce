#!/usr/bin/env python
import sys

dic={}
for line in sys.stdin:
	line=line.strip()
	line=line[1:-1]
	year=(line.split(',')[0])
	temp=(line.split(',')[1])
	if year in list(dic.keys()):
		dic[year]=max(dic[year],temp)
	else:
		dic[year]=temp
for i,j in dic.items():
	print(i,j)
	
	
