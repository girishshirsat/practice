"""In this challenge, you will be given  integers,  and . There are  words, which might repeat, in word group . There are  words belonging to word group . For each  words, check whether the word has appeared in group  or not. Print the indices of each occurrence of  in group . If it does not appear, print .

Example

Group A contains 'a', 'b', 'a' Group B contains 'a', 'c'

For the first word in group B, 'a', it appears at positions  and  in group A. The second word, 'c', does not appear in group A, so print .

Expected output:

1 3
-1"""


from collections import defaultdict
n,m=list(map(int,input().split()))

d=defaultdict(list)

for i in range(n):
    A=input()
    d[A].append(str(i + 1))

C=[]
for i in range(m):
    B = input()
    if B in d:
        C.append(" ".join(d[B]))
    else:
        C.append(-1)

for result in C:
    print(result)

# for i in range(m):
#     B=input()
#     d["B"].append(str(B))



# for i in range(1,m):
#     for j in range(n):
#             if d["B"][i]==d["A"][j]:
#                 print(d["A"].index(j)+1,end=" ")
#             else:
#                 print(-1)
# print()
