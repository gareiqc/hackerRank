#!/bin/python3

import sys

def lcm(a, b):
	return (a*b) // gcd(a, b)

def getTotalX(a, b):
	num_btn = 0
	for x in a:
		
	return num_btn

n, m = input().strip().split(' ')
n, m = [int(n), int(m)]
a = list(map(int, input().strip().split(' ')))
b = list(map(int, input().strip().split(' ')))
total = getTotalX(a, b)
print(total)
