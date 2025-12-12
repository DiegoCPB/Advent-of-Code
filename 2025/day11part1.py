# -*- coding: utf-8 -*-
"""
Created on 2025-12-12 20:39:46 UTC+01:00

@author: DiegoCPB
"""

def you2out(filepath):
    def expand_node(node):
        if node == 'out':
            return node
        else:
            return [expand_node(n) for n in links[node]]
    links = {}
    with open(filepath) as file:
        for line in file:
            if line.rstrip():
                words = line.split()
                links[words[0][:-1]] = words[1:]
    res = str(expand_node('you'))
    return len(res.split('out'))-1

if __name__ == "__main__":
    filepath = 'inputs/day11.txt'
    print(you2out(filepath))