"""Task

You are given a string .
Your task is to find out if the string  contains: alphanumeric characters, alphabetical characters, digits, lowercase and uppercase characters.

Input Format

A single line containing a string .

Constraints


Output Format

In the first line, print True if  has any alphanumeric characters. Otherwise, print False.
In the second line, print True if  has any alphabetical characters. Otherwise, print False.
In the third line, print True if  has any digits. Otherwise, print False.
In the fourth line, print True if  has any lowercase characters. Otherwise, print False.
In the fifth line, print True if  has any uppercase characters. Otherwise, print False."""

s = input()


l1=[]
for i in s:
    if i.isalnum():
        l1.append(True)
    else:
        l1.append(False)
if True in l1:
    print(True)
else:
    print(False)

l2=[]
for i in s:
    if i.isalpha():
        l2.append(True)
    else:
        l2.append(False)
    
if True in l2:
    print(True)
else:
    print(False)

l3=[]
for i in s:
    if i.isdigit():
        l3.append(True)
    else:
        l3.append(False)

if True in l3:
    print(True)
else:
    print(False)

l4=[]
for i in s:
    if i.islower():
        l4.append(True)
    else:
        l4.append(False)

if True in l4:
    print(True)
else:
    print(False)

l5=[]
for i in s:
    if i.isupper():
        l5.append(True)
    else:
        l5.append(False)
if True in l5:
    print(True)
else:
    print(False)