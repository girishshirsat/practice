"""Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.

The overall run time complexity should be O(log (m+n)).
"""

nums1=list(map(int,input().split()))
nums2=list(map(int,input().split()))

n=len(nums1)
m=len(nums2)
L=n+m
nums3=nums1+nums2
print(nums3)
nums4=sorted(nums3)
if (L%2)!=0:
    N1=L//2
    M1=nums4[N1]
    print(M1)
    print(float(M1))
else:
    N2=L//2
    N3=N2-1
    M2=nums4[N2]+nums4[N3]
    M3=M2/2
    print(M3)
    print(float(M3))