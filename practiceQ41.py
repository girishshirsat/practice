"""Task

You are given two integer arrays of size X and X ( &  are rows, and  is the column). Your task is to concatenate the arrays along axis .

Input Format

The first line contains space separated integers ,  and .
The next  lines contains the space separated elements of the  columns.
After that, the next  lines contains the space separated elements of the  columns.

Output Format

Print the concatenated array of size X."""

import numpy



N,M,P=list(map(int,input().split()))

C=[]
for i in range(N):
    L=list(map(int,input().split()))
    if len(L)<=P:
        C.append(L[:P])
    
D=[]
for i in range(M):
    L=list(map(int,input().split()))
    if len(L)<=P:
        D.append(L[:P])
    
E=numpy.concatenate((C,D),axis=0)

print(E)