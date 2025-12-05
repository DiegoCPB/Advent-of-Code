# -*- coding: utf-8 -*-
"""
Created on 2025-12-05 18:53:13 UTC+01:00

@author: DiegoCPB
"""

def fresh_ingredients(filepath):
    rngs = []
    vals = []
    with open(filepath) as file:
        read_rngs = True
        for line in file:
            if not line.rstrip():
                read_rngs = False
            elif read_rngs:
                rng = [int(i) for i in line.split('-')]
                rngs.append(rng)
                vals += rng
    vals = sorted(list(set(vals)))
    func = lambda x: any([(x>=rng[0])*(x<=rng[1]) for rng in rngs])
    counter = 0
    for i in range(len(vals)-1):
        inter_val = (vals[i+1]+vals[i])//2
        n_between = vals[i+1]-vals[i]-1
        counter += func(inter_val)*n_between
    return counter+len(vals)

if __name__ == "__main__":
    filepath = 'inputs/day5.txt'
    print(fresh_ingredients(filepath))