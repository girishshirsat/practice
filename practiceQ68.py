"""Given a sorted array of unique integers that has been rotated at an unknown pivot, find the index of a target value or return -1 if not found.

Example

Input:

nums = [1609466400, 1609470000, 1609473600, 1609459200, 1609462800]
target = 1609459200
Output:

3"""


def searchRotatedTimestamps(nums, target):
    n = len(nums)

    low = 0
    high = n - 1

    while low <= high:
        mid = (low + high) // 2

        if nums[mid] == target:
            return mid

       
        if nums[low] <= nums[mid]:
            if nums[low] <= target < nums[mid]:
                high = mid - 1
            else:
                low = mid + 1

       
        else:
            if nums[mid] < target <= nums[high]:
                low = mid + 1
            else:
                high = mid - 1

    return -1

nums_count = int(input().strip())

nums = []

for _ in range(nums_count):
    nums_item = int(input().strip())
    nums.append(nums_item)

target = int(input().strip())

result = searchRotatedTimestamps(nums, target)

print(result)