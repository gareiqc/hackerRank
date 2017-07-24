import sys

def missing_nums(a, b):
	a_dict = {}
	b_dict = {}
	not_in = []

	for x in a:
		if x not in a_dict:
			a_dict[x] = 1
		else:
			a_dict[x] += 1
	for x in b:
		if x not in b_dict:
			b_dict[x] = 1
		else:
			b_dict[x] += 1

	for (k, v) in b_dict.items():
		if k not in b_dict:
			not_in.append(k)
		else:
			if a_dict[k] != v:
				not_in.append(k)

	for x in sorted(not_in):
		print(x, "", end=''),
	print('')

lst_A_size = input()

lst_A = sys.stdin.readline().split()

lst_B_size = input()

lst_B = sys.stdin.readline().split()

missing_nums(lst_A, lst_B)
