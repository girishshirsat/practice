"""You are given a string .
Your task is to find out whether  is a valid regex or not.

Input Format

The first line contains integer , the number of test cases.
The next  lines contains the string .

Constraints


Output Format

Print "True" or "False" for each test case without quotes."""

import re
import sys

input = sys.stdin.readline

T = int(input())
for _ in range(T):
    s = input().strip()
    try:
        re.compile(s)
        print("True")
    except re.error:
        print("False")