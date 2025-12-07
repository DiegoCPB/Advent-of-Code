# -*- coding: utf-8 -*-
"""
Created on 2025-12-04 20:37:55 UTC+01:00

@author: DiegoCPB
"""

import numpy as np
from scipy import signal

def count_rolls(filepath):
    k = np.array([[1,1,1],[1,0,1],[1,1,1]])
    with open(filepath,'r') as file:
        M = np.array([list(line.rstrip()) for line in file if line.rstrip()])
    M = (M=='@').astype(int)
    R = np.zeros(M.shape,dtype=int)
    while True:
        conv = signal.convolve2d(M,k,mode='same')
        Ri = (conv<4)*M
        if np.any(Ri!=0):
            R += Ri
            M -= Ri
        else:
            break
    return np.sum(R)

if __name__ == "__main__":
    filepath = 'inputs/day4.txt'
    print(count_rolls(filepath))