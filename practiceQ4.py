"""Given the names and grades for each student in a class of  students, store them in a nested list and print the name(s) of any student(s) having the second lowest grade.

Note: If there are multiple students with the second lowest grade, order their names alphabetically and print each name on a new line."""
l1=[]
all_score=[]


for _ in range(int(input())):
        name = input()
        score = float(input())
        all_score.append(score)
        li=[name,score]
        l1.append(li)

print(l1)

sortset=list(set(all_score))
sortset.sort()
second_lovest=sortset[1]


name_0f_lovest=[]
for i in l1:
        if i[1]==second_lovest:
                name_0f_lovest.append(i[0])

name_0f_lovest.sort()
for i in name_0f_lovest:
        print(i)