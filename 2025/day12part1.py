# -*- coding: utf-8 -*-
"""
Created on 2025-12-13 22:13:09 UTC+01:00

@author: DiegoCPB
"""

import numpy as np

def fitting_presents(filepath):
    with open(filepath) as file:
        lines = file.read().split('\n\n')
    pshapes = []
    for line in lines[:-1]:
        val = line.split(':\n')
        pshapes.append(np.array([[1 if j=='#' else 0 for j in i] for i in val[1].split('\n')]))
    psizes = [np.sum(i) for i in pshapes]
    regions = []
    for line in lines[-1].split('\n'):
        if line.rstrip():
            val = line.split(':')
            size = np.array([int(i) for i in val[0].split('x')])
            quants = np.array([int(i) for i in val[1].split()])
            regions.append([size,quants]) 
    impossible = 0
    possible = 0
    undetermined = 0
    for size, quants in regions:
        if np.prod(size) < np.inner(quants,psizes):
            impossible += 1
        elif np.prod(size//3) >= np.sum(quants):
            possible += 1
        else:
            # There as no undetermined cases on the input
            # However, in the example, the last one is undetermined
            undetermined += 1
    return possible,impossible,undetermined 

if __name__ == "__main__":
    filepath = 'inputs/day12.txt'
    print(fitting_presents(filepath))