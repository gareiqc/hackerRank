#!/bin/python3

import sys

def staircase(n):
        symbol_pos = n
        i = 0
        stair_line = ""
        while(symbol_pos != 0):
                for i in range(1, n+1):
                        if i < symbol_pos:
                                stair_line += " "
                        else:
                                stair_line += "#"
                        if i == n:
                                print(stair_line)
                                stair_line = ""
                                symbol_pos -= 1

n = int(input().strip())
staircase(n)
