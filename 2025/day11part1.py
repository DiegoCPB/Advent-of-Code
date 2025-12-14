# -*- coding: utf-8 -*-
"""
Created on 2025-12-12 20:39:46 UTC+01:00

@author: DiegoCPB
"""

def count_paths(links,node,end):
    if node == end:
        return 1
    return sum(count_paths(links,n,end) for n in links.get(node,[]))

def you2out(filepath):
    links = {}
    with open(filepath) as file:
        for line in file:
            if line.rstrip():
                words = line.split()
                links[words[0][:-1]] = words[1:]
    res = count_paths(links,'you','out')
    return res

if __name__ == "__main__":
    filepath = 'inputs/day11.txt'
    print(you2out(filepath))