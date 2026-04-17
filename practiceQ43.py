"""Task

 is a shoe shop owner. His shop has  number of shoes.
He has a list containing the size of each shoe he has in his shop.
There are  number of customers who are willing to pay  amount of money only if they get the shoe of their desired size.

Your task is to compute how much money  earned."""

from collections import Counter
N=int(input())

L=list(map(int,input().split()))

A=Counter(L)

keys=Counter(L).keys()


M=int(input())
Amt=[]

for i in range(M):
    X,Y=list(map(int,input().split()))
    if X not in keys:
        continue
    elif A[X]==0:
        continue
    else:
        A[X]=A[X]-1
        Amt.append(Y)

S=sum(Amt)
print(S)

        

        




