#!/bin/python3

import sys

def diag_diff(ar):
	prim_diag = 0
	sec_diag = 0
	for i in range(0,len(ar)):
		for j in range(0, len(ar)):
			if i == j:
				prim_diag += ar[i][j]
			if (i+j) == (len(ar)-1):
				sec_diag += ar[i][j]

	return abs(prim_diag - sec_diag)

n = int(input().strip())
a = []
for a_i in range(n):
    a_t = [int(a_temp) for a_temp in input().strip().split(' ')]
    a.append(a_t)

print(diag_diff(a))
