#!/bin/python3

import sys

def min_max_sum(a):
	_min = 0
	_max = 0
	a = sorted(a)
	for i in range(0, 4):
		_min += a[i]
	for i in range(len(a)-4, len(a)):
		_max += a[i]
	return str(_min) + " " + str(_max)

arr = list(map(int, input().strip().split(' ')))

print(min_max_sum(arr))
