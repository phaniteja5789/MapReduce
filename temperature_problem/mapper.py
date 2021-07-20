#!/usr/bin/env python

import sys

for line in sys.stdin:
	line = line.strip()
	words = line.split(',')
	date_year=words[0]
	ids=words[1]
	temp=words[2]
	year=date_year.split('-')[-1]
	print (year, temp)
