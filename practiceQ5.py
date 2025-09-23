n = int(input())
student_marks = {}
for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
query_name = str(input())

print(student_marks)

if query_name in student_marks:
    li=list(student_marks[query_name])
    average=round(sum(li)/len(li),2)
    print(average)
else:
    print("Enter valid name")
            
