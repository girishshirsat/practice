'''representation of a chessboard.

This could be imagined as a 2D cartesian plane, with the x axis being represented by the alphabets and y axis by the numbers.

Given coordinates in the form of string, print if that cell is white or black.

Input Format
First line contains a string s.

Output Format
White or Black.

Constraints
|s|=2

Sample Testcase 0
Testcase Input
b2
Testcase Output
Black
'''



def determine_color(s):
   C={'a':1,'b':2,'c':3,'d':4,'e':5,'f':6,'g':7,'h':8}
   r=s[0]
   if (int(C[r])+int(s[1]))%2==0:
         return "Black"
   else:
        return "White"

def main():
    import sys
    
    s = list(input())

    result = determine_color(s)
    print(result)

main()    