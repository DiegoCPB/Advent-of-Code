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
                b = np.array([1 if s=='#' else 0 for s in list(blocks[0][1:-1])])
                nb,ns = len(b),len(blocks)-2
                M = np.zeros((nb,ns))
                for i in range(ns):
                    pos = [int(s) for s in blocks[i+1][1:-1].split(',')]
                    M[np.ix_(pos,[i])] = 1
                M = np.hstack([M,-2*np.eye(nb)])
                c = np.hstack([np.ones(ns),np.zeros(nb)])
                constraints = LinearConstraint(M, b, b)
                integrality = np.ones_like(c)
                res = milp(c=c, constraints=constraints, integrality=integrality)
                print(res.x[:ns])
                counter += np.sum(res.x[:ns])
    return counter

if __name__ == "__main__":
    filepath = 'inputs/day10.txt'
    print(button_presses(filepath))