# -*- coding: utf-8 -*-
"""
Created on 2025-12-03 23:42:26 UTC+01:00

@author: DiegoCPB
"""

def check_ID(filepath):
    counter = 0
    with open(filepath,'r') as file:
        ID_ranges = file.read().rstrip().split(',')
    for ID_range in ID_ranges:
        ID0,ID1 = ID_range.split('-') 
        for i in range(int(ID0),int(ID1)+1):
            ID = str(i)
            n = len(ID)
            for j in range(1,n//2+1):
                if (n%j) == 0:
                    if ID[:j]*(n//j) == ID:
                        counter += i
                        break   
    return counter

if __name__ == "__main__":
    filepath = 'inputs/day2.txt'
    print(check_ID(filepath))
    

