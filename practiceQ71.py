"""Counting Stable Performance Intervals
Given an integer array of length n and an integer k, return the number of contiguous subarrays where max - min <= k. Constraint: n <= 100000.

Example

Input:

n = 3
a = [1, 2, 3]
k = 2
Output:

6"""


def log2_floor(n):
    k = 0
    while (1 << k) <= n:
        k += 1
    return k - 1

def build_sparse(a, n):
    LOG = log2_floor(n) + 1 if n > 0 else 1
    sp_max = [[0]*n for _ in range(LOG)]
    sp_min = [[0]*n for _ in range(LOG)]
    sp_max[0] = a[:]
    sp_min[0] = a[:]
    for j in range(1, LOG):
        for i in range(n - (1 << j) + 1):
            half = 1 << (j - 1)
            sp_max[j][i] = sp_max[j-1][i] if sp_max[j-1][i] > sp_max[j-1][i+half] else sp_max[j-1][i+half]
            sp_min[j][i] = sp_min[j-1][i] if sp_min[j-1][i] < sp_min[j-1][i+half] else sp_min[j-1][i+half]
    return sp_max, sp_min

def query(sp_max, sp_min, l, r):
    length = r - l + 1
    j = log2_floor(length)
    a = sp_max[j][l]
    b = sp_max[j][r - (1 << j) + 1]
    mx = a if a > b else b
    a = sp_min[j][l]
    b = sp_min[j][r - (1 << j) + 1]
    mn = a if a < b else b
    return mx - mn

def countValidSubarrays(n, a, k):
    if n == 0:
        return 0
    sp_max, sp_min = build_sparse(a, n)
    count = 0
    for l in range(n):
        lo, hi, best = l, n - 1, l - 1
        while lo <= hi:
            mid = (lo + hi) // 2
            if query(sp_max, sp_min, l, mid) <= k:
                best = mid
                lo = mid + 1
            else:
                hi = mid - 1
        if best >= l:
            count += best - l + 1
    return count
            

if __name__ == '__main__':
    n = int(input().strip())

    a_count = int(input().strip())

    a = []

    for _ in range(a_count):
        a_item = int(input().strip())
        a.append(a_item)

    k = int(input().strip())

    result = countValidSubarrays(n, a, k)

    print(result)