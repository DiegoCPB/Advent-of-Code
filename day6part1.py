# -*- coding: utf-8 -*-
"""
Created on 2025-12-06 10:32:46 UTC+01:00

@author: DiegoCPB
"""

def math_homework(filepath):
    table = []
    with open(filepath) as file:
        for line in file:
            table.append(line.rstrip().split())
    oper = table[-1]
    res = table[0]
    for i in range(1,len(table)-1):
        for j in range(len(oper)):
            res[j] = eval(f'{res[j]}{oper[j]}{table[i][j]}')
    return sum(res)

if __name__ == "__main__":
    filepath = 'inputs/day6.txt'
    print(math_homework(filepath))
