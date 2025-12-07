# -*- coding: utf-8 -*-
"""
Created on 2025-12-06 10:32:46 UTC+01:00

@author: DiegoCPB
"""

def math_homework(filepath):
    with open(filepath) as file:
        table = [line.strip('\n').split() for line in file]
    oper = table[-1]
    table = list(zip(*table[:-1])) # zip(*table) => transposes table
    res = 0
    for i in range(len(table)):
        res += eval(oper[i].join(table[i]))
    return res

if __name__ == "__main__":
    filepath = 'inputs/day6.txt'
    print(math_homework(filepath))
