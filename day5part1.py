# -*- coding: utf-8 -*-
"""
Created on 2025-12-05 18:53:18 UTC+01:00

@author: DiegoCPB
"""

def fresh_ingredients(filepath):
    rngs = []
    IDs = []
    with open(filepath) as file:
        read_rngs = True
        for line in file:
            if not line.rstrip():
                read_rngs = False
            elif read_rngs:
                rng = [int(i) for i in line.split('-')]
                rngs.append(rng)
            else:
                IDs.append(int(line))
    func = lambda x: any(r0 <= x <= r1 for r0, r1 in rngs)
    counter = 0
    for ID in IDs:
        counter += func(ID)
    return counter

if __name__ == "__main__":
    filepath = 'tests/day5.txt'
    print(fresh_ingredients(filepath))
