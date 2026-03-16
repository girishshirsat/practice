"""Sample Input

STDIN                                       Function
-----                                       --------
10                                          arr[] size N = 10
161 182 161 154 176 170 167 171 170 174     arr = [161, 181, ..., 174]
Sample Output

169.375"""


def average(array):
    s=set(array)
    av=sum(s)/len(s)
    return av


n = int(input())
arr = list(map(int, input().split()))
result = average(arr)
print(result)
