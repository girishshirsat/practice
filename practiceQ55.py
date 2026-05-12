def calculate_pairs(n, arr):
    D = {}
    C = 0
    for i in range(n):
        for j in range(i, n):
            k = arr[i:j+1]
            v = sum(k)
            if v in D:
                prev_start, prev_end = D[v]
                
                if i > prev_end:
                    C += 1
            else:
                D[v] = (i, j)  

    return C


    

data=list(map(int,input().split()))
n = int(data[0]) 
arr = list(map(int, data[1:n+1]))  
result = calculate_pairs(n, arr)
print(result)




# def calculate_pairs(n, arr):
#     D={}
#     for i in range(n):
#         for j in range(i,n):
#             k=arr[i:j+1]
#             v=sum(k)
#             D.update({tuple(k):v})

#     print(D)

#     x=D.values()
#     y=list(x)

#     C=0

#     for i in y:
#         if y.count(i)>1:
#             C+=1

#     return C


# def calculate_pairs(n, arr):
#     D={}
#     C=0
#     for i in range(n):
#         for j in range(i,n):
#             k=arr[i:j+1]
#             v=sum(k)
#             if v in D:
#                 L=list(D[v])
#                 for i in k:
#                     if i in L:
#                         break
#                     else:
#                         C+=1
#                         D.update({v:tuple(k)})
#             else:
#                 D.update({v:tuple(k)})


#     print(D)

#     return C