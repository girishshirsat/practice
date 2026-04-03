"""Task

You are given a string .
Your task is to print all possible permutations of size  of the string in lexicographic sorted order.

Input Format

A single line containing the space separated string  and the integer value ."""

A=list(map(str,input().split()))


from itertools import permutations

S=A[0].upper()
B=list(permutations(S,int(A[1])))


C=[]
for i in B:
   C.append(list(i))

D=[]
for i in C:
    D.append("".join(i))

E=sorted(D)

for i in E:
    print(i)
