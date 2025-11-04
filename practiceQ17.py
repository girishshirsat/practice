def average(array):
    s=set(array)
    av=sum(s)/len(s)
    return av


n = int(input())
arr = list(map(int, input().split()))
result = average(arr)
print(result)