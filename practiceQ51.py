"""Count Elements Greater Than Previous Average
Given an array of positive integers, return the number of elements that are strictly greater than the average of all previous elements. Skip the first element.

Example

Input

responseTimes = [100, 200, 150,300]
Output

2"""


def countResponseTimeRegressions(responseTimes):
    arr=responseTimes
    if len(arr)<2:
        return 0
    total = arr[0]
    count = 0
    
    for i in range(1, len(arr)):
        if arr[i] * i > total:
            count += 1
        total += arr[i]
    
    return count
            


responseTimes_count = int(input().strip())

responseTimes = []

for _ in range(responseTimes_count):
    responseTimes_item = int(input().strip())
    responseTimes.append(responseTimes_item)

result = countResponseTimeRegressions(responseTimes)

print(result)