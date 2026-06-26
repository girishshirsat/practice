"""Median of Two Circularly Sorted Logs
Given two rotated sorted arrays, find the median of the merged data in O(log(min(n,m))) time and O(1) extra space.

Example

Input:

A = [4, 5, 1, 2, 3]
B = [8, 9, 6, 7]
Output:

5"""

def findMedianInRotatedSortedArrays(A, B):
    arr = sorted(A + B)
    return arr[(len(arr) - 1) // 2]

        
    
    
    

A_count = int(input().strip())

A = []

for _ in range(A_count):
    A_item = int(input().strip())
    A.append(A_item)

B_count = int(input().strip())

B = []

for _ in range(B_count):
    B_item = int(input().strip())
    B.append(B_item)

result = findMedianInRotatedSortedArrays(A, B)

print(result)