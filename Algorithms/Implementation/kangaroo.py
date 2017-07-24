#!/bin/python3

import sys

#x1 is starting position of kangaroo 1
#v1 is rate of distance of kangaroo 1
#x2 is starting position of kangaroo 2
#v2 is starting position of kangaroo 2

def kangaroo(x1, v1, x2, v2):
	answer = "NO"
	#x1 + v1i = x2 + v2i
	#x1 - x2 = (v2-v1)*i
	#i = x1 - x2 / (v2 - v1)
	i = -1.0
	#if i is whole number, they meet at the same distance
	if (v2 - v1) != 0:
		i = (x1 - x2) / (v2 - v1)
	if i.is_integer() and i >= 0:
		answer = "YES"
	return answer



x1, v1, x2, v2 = input().strip().split(' ')
x1, v1, x2, v2 = [int(x1), int(v1), int(x2), int(v2)]
result = kangaroo(x1, v1, x2, v2)
print(result)
