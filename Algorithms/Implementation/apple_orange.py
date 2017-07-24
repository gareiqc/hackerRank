#!/bin/python3

import sys

#s and t are the start,end points of house
#a is where apple tree is and b is where orange tree is
#apple is list of distances apples fall from point a
#orange is list of distances oranges fall from point b
def apple_orange(s, t, a, b, apple, orange):
	apples_hit = 0
	oranges_hit = 0
	for x in apple:
		if a+x >= s and a+x <= t:
			apples_hit += 1
	for x in orange:
		if b+x <= t and b+x >= s:
			oranges_hit += 1
	return [apples_hit, oranges_hit]

s,t = input().strip().split(' ')
s,t = [int(s),int(t)]
a,b = input().strip().split(' ')
a,b = [int(a),int(b)]
m,n = input().strip().split(' ')
m,n = [int(m),int(n)]
apple = [int(apple_temp) for apple_temp in input().strip().split(' ')]
orange = [int(orange_temp) for orange_temp in input().strip().split(' ')]
result = apple_orange(s, t, a, b, apple, orange)
print("\n".join(map(str, result)))
