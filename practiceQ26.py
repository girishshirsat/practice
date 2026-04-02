"""You are given a set  and  other sets.
Your job is to find whether set  is a strict superset of each of the  sets.

Print True, if  is a strict superset of each of the  sets. Otherwise, print False.

A strict superset has at least one element that does not exist in its subset."""


N=int(input())
Aset=set(list(map(int,input().split())))

o=[]


for i in range(N,0,-1):

    Bset=set(list(map(int,input().split())))

    if Aset.issubset(Bset) and len(Bset)>len(Aset):
        o.append("True")
    else:
        o.append("False")

if o.count("False")>0:
    print("False")
else:
    print("True")