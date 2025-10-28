'''You are given a string  and width .
Your task is to wrap the string into a paragraph of width .

Function Description

Complete the wrap function in the editor below.

wrap has the following parameters:

string string: a long string
int max_width: the width to wrap to
Returns

string: a single string with newline where the breaks should be




Sample Input 0

ABCDEFGHIJKLIMNOQRSTUVWXYZ
4
Sample Output 0

ABCD
EFGH
IJKL
IMNO
QRST
UVWX
YZ
'''


s=input()
w=int(input())
l=[]

def wrap(s,w):
    for i in s:
        if len(l)==4:
            s=s[w:]
            break
        else:
            l.append(i)

    ns="".join(l)
    l.clear()
    print(ns)
    if len(s)==0:
        pass
    elif len(s)<w:
        print(s)
    else:
        wrap(s,w)


wrap(s,w)



