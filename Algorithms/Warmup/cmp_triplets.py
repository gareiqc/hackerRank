#!/bin/python3

import sys

def solve(a0, a1, a2, b0, b1, b2):
	cmp = [a0-b0, a1-b1, a2-b2]
	alice_score = 0
	bob_score = 0
	for s in cmp:
		if s > 0:
			alice_score += 1
		elif s < 0:
			bob_score += 1

	return str(alice_score) + str(bob_score)

a0, a1, a2 = input().strip().split(' ')
a0, a1, a2 = [int(a0), int(a1), int(a2)]
b0, b1, b2 = input().strip().split(' ')
b0, b1, b2 = [int(b0), int(b1), int(b2)]
result = solve(a0, a1, a2, b0, b1, b2)
print (" ".join(map(str, result)))
