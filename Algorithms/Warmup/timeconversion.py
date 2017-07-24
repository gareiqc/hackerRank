#!/bin/python3

import sys

def timeConversion(s):
	hour, min, sec = s.split(':')
	sec = sec[0:2]
	num_hour = int(hour)
	if s[8] == 'P':
		if hour[0] == '0':
			num_hour = int(hour[1]) + 12
		if hour != '12':
			num_hour = int(hour) + 12
		time_str = str(num_hour) + ':' + min + ':' + sec
	else:
		if hour == '12':
			num_hour = int(hour) - 12
		if num_hour < 10:
			time_str = '0' + str(num_hour) + ':' + min + ':' + sec
		else:
			time_str = str(num_hour) + ':' + min + ':' + sec
	return time_str

s = input().strip()
result = timeConversion(s)
print(result)
