"""Consider a list (list = []). You can perform the following commands:

insert i e: Insert integer  at position .
print: Print the list.
remove e: Delete the first occurrence of integer .
append e: Insert integer  at the end of the list.
sort: Sort the list.
pop: Pop the last element from the list.
reverse: Reverse the list.
Initialize your list and read in the value of  followed by  lines of commands where each command will be of the  types listed above. Iterate through each command in order and perform the corresponding operation on your list."""

N=int(input())
li=[]

for i in range(N):
    cmd = input().split()

    if cmd[0] == "insert":
        index = int(cmd[1])
        try:
            value = int(cmd[2])
        except ValueError:
            print("Enter numeric value")
        else:
            li.insert(index, value)
    elif cmd[0]=="append":
        try:
            value = int(cmd[1])
        except ValueError:
            print("Enter numeric value")
        else:
            li.append(value)
    elif cmd[0]=="print":
        print(li)
    elif cmd[0]=="remove":
        try:
            value = int(cmd[1])
        except ValueError:
            print("Enter numeric value")
        else:
            li.remove(value)
    elif cmd[0]=="sort":
        li.sort()
    elif cmd[0]=="reverse":
        li.reverse()
    elif cmd[0]=="pop":
        li.pop()
        


    

