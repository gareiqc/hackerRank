#!/bin/python3

import sys

def birthdayCakeCandles(n, ar):
	candles = {}
	highest = 0
	for i in ar:
		if i > highest:
			highest = i
		if i not in candles:
			candles[i] = 1
		else:
			candles[i] += 1
	return candles[highest]

n = int(input().strip())
ar = list(map(int, input().strip().split(' ')))
result = birthdayCakeCandles(n, ar)
print(result)
