#!/bin/python3
import sys

def compute_sum(arr):
	max_sum = 0
	sum = 0
	start = 0
	end = 3
	while(True):
		for i in range(start, end):
			for j in range(start, end):
				if (i == start + 1 and j == start) or (i == start + 1 and j == end - 1):
					continue
				sum += arr[i][j]
				if sum > max_sum:
					max_sum = sum
		if start 
			start += 1
		if end += 1 > arr(len):
			break
		end += 1

arr = []
for arr_i in range(6):
   arr_t = [int(arr_temp) for arr_temp in input().strip().split(' ')]
   arr.append(arr_t)
print(compute_sum(arr))
