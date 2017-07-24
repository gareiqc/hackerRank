#!/bin/python3

import sys

def print_reverse(arr):
	for i in reversed(arr):
		print(i, end=' ')
	print()

n = int(input().strip())
arr = [int(arr_temp) for arr_temp in input().strip().split(' ')]
print_reverse(arr)
