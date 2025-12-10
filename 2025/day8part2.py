# -*- coding: utf-8 -*-
"""
Created on 2025-12-10 02:28:22 UTC+01:00

@author: DiegoCPB
"""

import numpy as np
from scipy import sparse
from scipy.sparse.csgraph import connected_components

def circuits(filepath):
    n = 1000
    C = np.loadtxt(filepath, delimiter=",")
    nC = len(C)
    D = np.zeros((nC-1)*nC//2)
    links = np.zeros([(nC-1)*nC//2,2],dtype=int)
    it = 0
    for i in range(nC):
        for j in range(i+1,nC):
            links[it] = [i,j]
            D[it] = np.linalg.norm(C[i]-C[j])
            it += 1
    order = np.argsort(D)
    links = links[order]
    graph = sparse.lil_array((nC,nC))
    for k in range(len(links)):
        i,j = links[k]
        graph[i,j] = graph[j,i] = 1
        n_components = connected_components(graph, directed=False, return_labels=False)
        if n_components == 1:
            return C[i][0]*C[j][0]

if __name__ == "__main__":
    filepath = 'inputs/day8.txt'
    print(circuits(filepath))