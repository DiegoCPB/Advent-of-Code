# -*- coding: utf-8 -*-
"""
Created on 2025-12-03 23:42:53 UTC+01:00

@author: DiegoCPB
"""

def get_password(filepath):
    pos = 50
    counter = 0
    with open(filepath,'r') as file:
        for line in file:
            if line.rstrip():
                move = int(line.replace("L","-").replace("R",""))
                sum = pos + move
                posf = sum%100
                passes = abs(sum//100) + ((posf==0)-(pos==0))*(sum<=0)
                pos = posf
                counter += passes 
    return counter

if __name__ == "__main__":
    filepath = 'inputs/day1.txt'
    print(get_password(filepath))
