"""You are given two sets,  and .
Your job is to find whether set  is a subset of set .

If set  is subset of set , print True.
If set  is not a subset of set , print False."""
N=int(input())


o=[]

for i in range(N,0,-1):
    
    A=int(input())
    Aset=set(list(map(int,input().split()[:A])))

    B=int(input())
    Bset=set(list(map(int,input().split()[:B])))

    if Aset.issubset(Bset):
        o.append("True")
    else:
        o.append("False")

for i in o:
    print(i)