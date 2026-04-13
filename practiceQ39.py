"""You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

 """

class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

class linklist:
    def __init__(self):
        self.head=None
        self.n=0

    def insert(self,data):
        newnode=Node(data)
        if self.head is None:
            self.head=newnode 
        else:
            newnode.next=self.head
            self.head=newnode
        self.n+=1

L1=list(map(int,input().split()))
L2=list(map(int,input().split()))
x=len(L1)
y=len(L2)
A=linklist()
for i in range(0,x):
    A.insert(L1[i])

B=linklist()
for i in range(y):
    B.insert(L2[i])

L3=[]

for i in range(A.n):
    for j in range(B.n):
        if i==j:
            S=A.head.data+B.head.data
            L3.append(S)
    B.head=B.head.next
A.head=A.head.next

print(L3)