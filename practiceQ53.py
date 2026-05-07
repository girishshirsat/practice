"""count the number of subarray whose continues element sum is k and the max element in that subarray is M """

def countSubarraysWithSumAndMaxAtMost(nums, k, M):
    C=0
    for i in range(len(nums)):
        A=0
        for j in range(i,len(nums)):
            if nums[j]>M:
                break
            A+=nums[j]
            if A==k:
                C+=1


    return C


nums_count = int(input().strip())

nums = []

for _ in range(nums_count):
    nums_item = int(input().strip())
    nums.append(nums_item)

k = int(input().strip())

M = int(input().strip())

result = countSubarraysWithSumAndMaxAtMost(nums, k, M)

print(result)




