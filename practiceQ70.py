"""Count Number Pairs
Given a sorted array of positive integers and a target value, count the number of pairs (i, j) where i < j and array[i] + array[j] <= target.

Example

Input:

prices = [1, 2, 3, 4, 5]
budget = 7
Output:

8"""

def countAffordablePairs(prices, budget):
    count=0
    n=len(prices)
    
    for i in range(n):
        for j in range(i+1,n):
            if prices[i]+prices[j]<=budget:
                count+=1
    return count


prices_count = int(input().strip())

prices = []

for _ in range(prices_count):
    prices_item = int(input().strip())
    prices.append(prices_item)

budget = int(input().strip())

result = countAffordablePairs(prices, budget)

print(result)