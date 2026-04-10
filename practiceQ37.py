"""Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order."""

nums=list(map(int,input().split()))
target=int(input())
A=[]
N=len(nums)
for i in range(N):
    for j in range(N):
        if i==j:
            continue
        if (nums[i]+nums[j])==target:
            A.append(i)
print(A) 