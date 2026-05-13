"""Longest Arithmetic Subsequence with Given Difference
Given an array of integers and a positive integer k, find the length of the longest arithmetic progression with common difference k. Ignore duplicates.

Example

Input

arr = [8, 1, -1, 0, 3, 6, 2, 4, 5, 7, 9]
k = 2
Output 6"""

def findLongestArithmeticProgression(arr, k):
    if len(arr)==0:
        return 0
    elif len(arr)==0:
        return 1
    else:
        arr=sorted(arr)
        arr=set(arr) 
        MAX=0
        Cont=0
        for i in arr:
            if (i-k) in arr:
                continue
            else:
                j=i+k
                Cont=1
                while j in arr:
                    Cont+=1
                    j+=k
                if Cont>MAX:
                    MAX=Cont
            Cont=0
        return MAX


arr_count = int(input().strip())

arr = []

for _ in range(arr_count):
    arr_item = int(input().strip())
    arr.append(arr_item)

k = int(input().strip())

result = findLongestArithmeticProgression(arr, k)

print(result)

