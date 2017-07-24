#!/bin/python3

import sys

def solve(grades):
	final_grades = []
	final_grade = 0
	for i in grades:
		next_mult = i
		final_grade = i
		if i % 5 != 0:
			while(next_mult % 5 != 0):
				next_mult += 1
			if next_mult - i < 3 and i >= 38:
				final_grade = next_mult
		final_grades.append(final_grade)

	return final_grades

n = int(input().strip())
grades = []
grades_i = 0
for grades_i in range(n):
   grades_t = int(input().strip())
   grades.append(grades_t)
result = solve(grades)
print ("\n".join(map(str, result)))
