# -*- coding: utf-8 -*-
"""
Created on 2025-12-12 01:44:53 UTC+01:00

@author: DiegoCPB
"""

# -*- coding: utf-8 -*-
"""
Created on 2025-12-11 18:49:33 UTC+01:00

@author: DiegoCPB
"""

import numpy as np
from scipy.optimize import milp, LinearConstraint

def button_presses(filepath):
    counter = 0
    with open(filepath,'r') as file:
        for line in file:
            if line.rstrip():
                blocks = line.split()
                jl = np.array([int(s) for s in blocks[-1][1:-1].split(',')])
                njl,ns = len(jl),len(blocks)-2
                M = np.zeros((njl,ns))
                for i in range(ns):
                    pos = [int(s) for s in blocks[i+1][1:-1].split(',')]
                    M[np.ix_(pos,[i])] = 1
                c = np.ones(ns)
                constraints = LinearConstraint(M, jl, jl)
                integrality = np.ones_like(c)
                res = milp(c=c, constraints=constraints, integrality=integrality)
                print(res.x[:ns])
                counter += np.sum(res.x[:ns])
    return counter

if __name__ == "__main__":
    filepath = 'inputs/day10.txt'
    print(button_presses(filepath))