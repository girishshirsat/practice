"""
Task
Given  sets of integers,  and , print their symmetric difference in ascending order. The term symmetric difference indicates those values that exist in either  or  but do not exist in both."""



N=int(input())
n=map(int,input().split())
s1=set(n)


M=int(input())
m=map(int,input().split())
s2=set(m)


s3=s1.symmetric_difference(s2)
s3=sorted(s3)
for i in s3:
    print(i)
    