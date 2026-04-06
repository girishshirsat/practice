"""Task

The National University conducts an examination of  students in  subjects.
Your task is to compute the average scores of each student.

Sample Input

5 3
89 90 78 93 80
90 91 85 88 86  
91 92 83 89 90.5
Sample Output

90.0 
91.0 
82.0 
90.0 
85.5        """


A,B=list(map(int,input().split()))

X=[]
for i in range(1,B+1):
    X+=[list(map(float,input().split()))]
    

Z=zip(*X)
for i in Z:
    T=list(i)
    avg=sum(T)/len(T)
    print(avg)