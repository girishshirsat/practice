"""Target Index Search
Given a sorted array of distinct integers and a target value, return the index of the target or -1 if not found.

Example 1

Input:

nums = [1, 2, 3, 4, 5]
target = 3
Output:

2"""





def binarySearch(nums, target):
    N = len(nums)

    if N == 0:
        return -1

    low = 0
    high = N - 1

    while low <= high:
        mid = (low + high) // 2

        if nums[mid] == target:
            return mid
        elif target < nums[mid]:
            high = mid - 1
        else:
            low = mid + 1

    return -1



nums_count = int(input().strip())

nums = []

for _ in range(nums_count):
    nums_item = int(input().strip())
    nums.append(nums_item)

target = int(input().strip())

result = binarySearch(nums, target)

print(result)