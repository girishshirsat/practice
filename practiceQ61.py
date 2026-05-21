"""Smallest Substring Containing All Patterns
Given a string S and an array of patterns, find the smallest substring window [l, r] such that each pattern appears at least once within S[l..r]. Return the pair of indices or [-1, -1] if no such window exists.

Example

Input

S = xyzabcabczyx
patterns = ['abc', 'zyx']
Output

[6,11]"""

#optimal and best 15/15 testcase using this func
def findSmallestSubstringWindow(patterns, S):

    occ = []

    for p in range(len(patterns)):

        sub = patterns[p]

        found = False

        for i in range(len(S) - len(sub) + 1):

            if S[i:i+len(sub)] == sub:

                F = i
                E = i + len(sub) - 1

                occ.append((F, E, p))

                found = True

        if found == False:
            return [-1, -1]

    occ.sort()

    left = 0

    freq = {}

    formed = 0

    need = len(patterns)

    best = float('inf')

    ans = [-1, -1]

    for right in range(len(occ)):

        p = occ[right][2]

        freq[p] = freq.get(p, 0) + 1

        if freq[p] == 1:
            formed += 1

        while formed == need:

            start = occ[left][0]
            end = occ[right][1]

            if end - start + 1 < best:

                best = end - start + 1

                ans = [start, end]

            lp = occ[left][2]

            freq[lp] -= 1

            if freq[lp] == 0:
                formed -= 1

            left += 1

    return ans



patterns_count = int(input().strip())

patterns = []

for _ in range(patterns_count):
    patterns_item = input()
    patterns.append(patterns_item)

S = input()

result = findSmallestSubstringWindow(patterns, S)

print('\n'.join(map(str, result)))


"""Not best and optimal but solving 11/15 testcases"""

# def findSmallestSubstringWindow(patterns, S):
#     def check(sub):
        
        
#         for i in range(len(S) - len(sub) + 1):
#             if S[i:i+len(sub)] == sub:
#                 F = i
#                 E = i + len(sub) - 1
#         return F,E

#     L=[]
#     H=[]
#     for i in patterns:
#         if i in S:
#             F,E=check(i)
#             L.append(F)
#             H.append(E)
#         else:
#             return(list([-1,-1]))
#     M=list([min(L),max(H)])

#     return(M)