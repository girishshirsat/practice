"""You are given a X integer array matrix with space separated elements ( = rows and  = columns).
Your task is to print the transpose and flatten results."""

import numpy as np 

A,B=list(map(int,input().split()))

C=[]


for i in range(A):
    L=list(map(int,input().split()))
    C.append(L)
    
D=np.array(C,int) 
E=np.transpose(D)
F=D.flatten()
print(E)
print(F)