# -*- coding: utf-8 -*-
"""
Created on 2025-12-06 10:32:46 UTC+01:00

@author: DiegoCPB
"""

def math_homework(filepath):
    lines = []
    with open(filepath) as file:
        for line in file:
            lines.append(list(line.strip('\n')))
    oper = ''.join(lines[-1]).split()
    problems = [ [] for _ in range(len(oper)) ]
    k = 0
    for j in range(len(lines[0])):
        s = ''
        for i in range(len(lines)-1):
            s += lines[i][j]
        if s.isspace():
            k += 1
        else:
            problems[k].append(s)
    res=0
    for i in range(len(oper)):
        res += eval(oper[i].join(problems[i]))
    return res

if __name__ == "__main__":
    filepath = 'inputs/day6.txt'
    print(math_homework(filepath))