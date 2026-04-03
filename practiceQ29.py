"""Task

You are given a string .
Your task is to print all possible combinations, up to size , of the string in lexicographic sorted order."""



from itertools import combinations


S, K = input().split()
K = int(K)


S = sorted(S)


for i in range(1, K + 1):
    for comb in combinations(S, i):
        print(''.join(comb))
