"""Two Sum
Given an array of positive integers and a target integer, return the indices of two elements that sum to the target or [-1, -1] if no such pair exists.

Example 1

Input:

taskDurations = [2, 7, 11, 15]
slotLength = 9
Output:

[0, 1]"""

def findTaskPairForSlot(taskDurations, slotLength):
    n = len(taskDurations)
    if n < 2:
        return [-1, -1]
    
    seen = {}  
    
    for j in range(n):
        need = slotLength - taskDurations[j]
        if need in seen:
            return [seen[need], j]
        seen[taskDurations[j]] = j
    
    return [-1, -1]
if __name__ == '__main__':
    taskDurations_count = int(input().strip())

    taskDurations = []

    for _ in range(taskDurations_count):
        taskDurations_item = int(input().strip())
        taskDurations.append(taskDurations_item)

    slotLength = int(input().strip())

    result = findTaskPairForSlot(taskDurations, slotLength)

    print('\n'.join(map(str, result)))