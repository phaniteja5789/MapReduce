#!/usr/bin/env python
import sys

dic={}
for line in sys.stdin:
	line=line.strip()
	line=line[1:-1]
	word=line.split(',')[0]
	if word in list(dic.keys()):
		dic[word]+=1
	else:
		dic[word]=1
for i,j in dic.items():
	print(i,j)
	
	
