#!/bin/python3

def pairs(a, k):
	num_set = set()
	add_set = set()
	for i in a:
		num_set.add(i)
		add_set.add(i+k)
	seen = add_set & num_set
	return len(seen)

if __name__ == '__main__':
	a = input().strip()
	a = list(map(int, a.split(' ')))
	_a_size = a[0]
	_k = a[1]
	b = input().strip()
	b = list(map(int, b.split(' ')))
	print(pairs(b,_k))
