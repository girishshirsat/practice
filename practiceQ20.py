"""
Problem Statement
You wish to help Ashish, who possesses a collection of N strings, some of which may be duplicated, and has been assigned the task of finding the kth unique string.

If the number of unique strings is less than k, he needs to display -1. Considering you are Ashish's best friend can you assist him with this challenge?


Sample Testcase 1
Testcase Input
3
dac
ba
a
1 
Testcase Output
dac
Explanation
As all the strings are unique we have the strings in the order: 
dac, ba, a

Now, as we can see the value of k=1 therefore, the string returned is the 1st unique string = dac."""



N=int(input())


List_Of_Strings=[]
for i in range(N):
    List_Of_Strings.append(input())

unique_strings=[]

count=0
for i in List_Of_Strings:
        count=List_Of_Strings.count(i)
        if count<=1:
            unique_strings.append(i)
            count=0

k=int(input())

if len(unique_strings)<k:
    print(-1)
else:
    print(unique_strings[k-1]) 


