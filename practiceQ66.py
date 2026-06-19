"""Max Area Under Histogram After Removing One Bar
Given an integer array heights, find the maximum rectangle area under the histogram after optionally removing at most one element.

Example

Input

heights = [5, 5, 1, 5, 5]
Output

20"""
def computeMaxRectangleAreaWithOneRemoval(heights):
    n = len(heights)

    if n == 0:
        return 0


    L1 = [-1] * n
    stack = []
    for i in range(n):
        while stack and heights[stack[-1]] >= heights[i]:
            stack.pop()
        L1[i] = stack[-1] if stack else -1
        stack.append(i)

  
    R1 = [n] * n
    stack = []
    for i in range(n - 1, -1, -1):
        while stack and heights[stack[-1]] >= heights[i]:
            stack.pop()
        R1[i] = stack[-1] if stack else n
        stack.append(i)

   
    L2 = [-1] * n
    for i in range(n):
        if L1[i] != -1:
            L2[i] = L1[L1[i]]

    
    R2 = [n] * n
    for i in range(n):
        if R1[i] != n:
            R2[i] = R1[R1[i]]

    ans = 0

    for i in range(n):
        h = heights[i]

       
        width = R1[i] - L1[i] - 1
        ans = max(ans, h * width)

        
        width = R2[i] - L1[i] - 2
        if width > 0:
            ans = max(ans, h * width)

       
        width = R1[i] - L2[i] - 2
        if width > 0:
            ans = max(ans, h * width)

    return ans



heights_count = int(input().strip())

heights = []

for _ in range(heights_count):
    heights_item = int(input().strip())
    heights.append(heights_item)

result = computeMaxRectangleAreaWithOneRemoval(heights)

print(result)


"""    l=len(heights)
    if l==1:
        return heights[0]
    else:
        ST=[]
        def calcA(heights):
            Ar=0
            W=1
            for i in range(0,l-1):
                if i==0:
                    A=heights[i]*W
                    if A>Ar:
                        Ar=A
                else:
                    if heights[i-1]<heights[i]:
                        A=heights[i-1]*W

                        if A>Ar:
                            Ar=A
                W+=1
            ST.append(Ar)

        
        calcA(heights)
        mn=min(heights)
        heights.remove(mn)
        calcA(heights)

        Mx=max(ST)
        return Mx"""