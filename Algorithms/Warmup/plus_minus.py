#!/bin/python3

import sys

def plus_minus(a):
	pos = 0
	neg = 0
	zer = 0
	for i in a:
		if i > 0:
			pos += 1
		elif i < 0:
			neg += 1
		else:
			zer += 1
	print( "{:.6f}".format(pos / len(a)) )
	print( "{:.6f}".format(neg / len(a)) )
	print( "{:.6f}".format(zer / len(a)) )

n = int(input().strip())
arr = [int(arr_temp) for arr_temp in input().strip().split(' ')]
plus_minus(arr)
