# -*- coding: utf-8 -*-
"""
Created on 2025-12-07 12:23:13 UTC+01:00

@author: DiegoCPB
"""

def beam_splits(filepath):
    with open(filepath) as file:
        table = [list(line.strip('\n')) for line in file]
    counter = 0
    for i in range(1,len(table)):
        for j in range(len(table[0])):
            if table[i][j] == '.' and (table[i-1][j] == '|' or table[i-1][j] == 'S'):
                table[i][j] = '|'
            elif table[i][j] == '^'and table[i-1][j] == '|':
                table[i][j-1] = '|'
                table[i][j+1] = '|'
                counter += 1
    return counter

if __name__ == "__main__":
    filepath = 'inputs/day7.txt'
    print(beam_splits(filepath))