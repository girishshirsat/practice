"""sliding window with zero sum not consicutive thois solution is not complete but AI also cant solving it"""




def findZeroSumTripletsInWindow(readings, windowSize):
    L=len(readings)
    A=[]
    if L<3:
        return A
    else:
        for i in range(L):
            for j in range(L):
                for k in range(L):
                    if i < j and j < k:
                        if readings[i]+readings[j]+readings[k]==0 and k-i+1<=windowSize:
                            if readings[i:k+1] not in A:
                                A.append(readings[i:k+1])
        return A








readings_count = int(input().strip())

readings = []

for _ in range(readings_count):
    readings_item = int(input().strip())
    readings.append(readings_item)

windowSize = int(input().strip())

result = findZeroSumTripletsInWindow(readings, windowSize)

print('\n'.join([' '.join(map(str, x)) for x in result]))

# def findZeroSumTripletsInWindow(readings, windowSize):
#     L=len(readings)
#     A=[]
#     if L<3:
#         return A
#     else:
#         for i in range(L):
#             j=i+1
#             k=i+2
#             if k>=L:
#                 break
#             if readings[i]+readings[j]+readings[k]==0 and k-i+1<=windowSize:
#                 if readings[i:k+1] not in A:
#                     A.append(readings[i:k+1])
#         return A