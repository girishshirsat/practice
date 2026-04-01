"""TASK
You are given a set  and  number of other sets. These  number of sets have to perform some specific mutation operations on set .

Your task is to execute those operations and print the sum of elements from set .

Input Format

The first line contains the number of elements in set .
The second line contains the space separated list of elements in set .
The third line contains integer , the number of other sets.
The next  lines are divided into  parts containing two lines each.
The first line of each part contains the space separated entries of the operation name and the length of the other set.
The second line of each part contains space separated list of elements in the other set."""


A=int(input())
s=set(map(int,input().split()[:A]))

N=int(input())

while N!=0:
    N-=1
    operation, length=input().split()
    length=int(length)
    otherset=set(map(int,input().split()[:length]))
    if operation=="intersection_update":
        s.intersection_update(otherset)
    elif operation=="update":
        s.update(otherset)
    elif operation=="symmetric_difference_update":
        s.symmetric_difference_update(otherset)
    elif operation=="difference_update":
        s.difference_update(otherset)

print(sum(s))