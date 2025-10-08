"""In this challenge, the user enters a string and a substring. You have to print the number of times that the substring occurs in the given string. String traversal will take place from left to right, not from right to left.

String letters are case-sensitive.

Input Format

The first line of input contains the original string. The next line contains the substring.

Constraints


Each character in the string is an ascii character.

Output Format

Output the integer number indicating the total number of occurrences of the substring in the original string.

Sample Input

ABCDCDC
CDC
Sample Output

2"""



def count_substring(string, sub_string):
    count=0
    l=len(string)
    while l!=0:
        if sub_string in string:
            occurence=string.find(sub_string)
            if occurence==-1:
                break
            else:
                count+=1

        if sub_string in string:
            string=string[occurence+1:]
        else:
            l=0
    return count



string = input().strip()
sub_string = input().strip()
    
count = count_substring(string, sub_string)
print(count)