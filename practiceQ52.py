"""Merge and Sort Intervals
Given an array of intervals [startTime, endTime], merge all overlapping intervals and return a sorted array of non-overlapping intervals.

Example

Input

intervals = [[1, 3], [2, 6], [8, 10], [15, 18]]
Output

[[1, 6], [8, 10], [15, 18]]
Explanation

- Step 1: Sort intervals by start time (already sorted). 
- Step 2: Initialize merged list with first interval [1,3]. 
- Step 3: Compare [2,6] with last merged [1,3]. They overlap (2 ≤ 3), so merge into [1,6]. Step 4: Compare [8,10] with last merged [1,6]. No overlap (8 > 6), append [8,10]. 
- Step 5: Compare [15,18] with last merged [8,10]. No overlap (15 > 10), append [15,18]. 

Result: [[1,6],[8,10],[15,18]]."""



def mergeHighDefinitionIntervals(intervals):
   
    intervals.sort()

    merged = []

    for interval in intervals:
       
        if not merged or merged[-1][1] < interval[0]:
            merged.append(interval)
        else:
           
            merged[-1][1] = max(merged[-1][1], interval[1])

    return merged

    

intervals_rows = int(input().strip())
intervals_columns = int(input().strip())

intervals = []

for _ in range(intervals_rows):
    intervals.append(list(map(int, input().rstrip().split())))

result = mergeHighDefinitionIntervals(intervals)

print('\n'.join([' '.join(map(str, x)) for x in result]))






# def mergeHighDefinitionIntervals(intervals):
#     L=len(intervals)-1
#     List=intervals

#     for i in range(L):
#         if i<L-1:
#             L1=List[i]
#             L1=sorted(L1)
#             A=i+1
#             L2=List[A]
#             L2=sorted(L2)
#             if L1[len(L1)-1]>L2[0]:
#                 L3=[L1[0],L2[len(L2)-1]]
#                 List.remove(L1)
#                 List.remove(L2)
#                 List.insert(0,L3)
        
#     return intervals