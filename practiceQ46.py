"""Given an integer array nums, find the subarray with the largest sum, and return its sum.

 

Example 1:

Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
Output: 6
Explanation: The subarray [4,-1,2,1] has the largest sum 6."""

nums=list(map(int,input().split()))


  
max_sum = nums[0]      
curr_sum = nums[0]     

for num in nums[1:]:
    curr_sum = max(num, curr_sum + num)
    max_sum = max(max_sum, curr_sum)
print(max_sum)

"""Brute force"""

# Sum=[]
# for i in range(len(L)+1):
#     for j in range(i+1,len(L)+1):
#         A=L[i:j]
#         B=sum(A)
#         Sum.append(B)

# print(max(Sum))