""""There is an array of  integers. There are also  disjoint sets,  and , each containing  integers. 
You like all the integers in set  and dislike all the integers in set . 
Your initial happiness is . 
For each  integer in the array, if , you add  to your happiness. 
If , you add  to your happiness. Otherwise, your happiness does not change. 
Output your final happiness at the end.

Note: Since  and  are sets, they have no repeated elements. However, the array might contain duplicate elements."""




n,m= list(map(int,input().split()))
arr=list(map(int,input().split()))
A=set(map(int,input().split()))
B=set(map(int,input().split()))

happy=0


for i in range(len(arr)):
    if arr[i] in A:
        happy=happy+1
    elif arr[i] in B:
        happy=happy-1
    else:
        pass
       

print(happy)




# s=set(arr)
# I=len(list(s.intersection(A)))
# happy=happy+I


# arr=list(s.difference(A))


# for i in range(len(arr)):
#     if arr[i] in B:
#         happy=happy-1
