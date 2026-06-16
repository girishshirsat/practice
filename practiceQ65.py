"""Validate Properly Nested Brackets
Given a string, check if all brackets ('()', '{}', '[]') are properly matched and nested. Return 1 if valid, otherwise return 0.

Example

Input

code_snippet = if (a[0] > b[1]) { doSomething(); }
Output

1
Explanation

All brackets are properly matched: '(' with ')', '[' with ']', and '{' with '}'. No mismatches or improper nesting.
Input Format

The function takes a single parameter, code_snippet, which is a STRING.
Constraints

0 <= code_snippet.length <= 1000
code_snippet consists of printable ASCII characters (character codes 32 to 126 inclusive)
code_snippet may contain any combination of '(', ')', '{', '}', '[', ']', letters, digits, symbols, and whitespace
code_snippet may be empty
Output Format

The function returns a BOOLEAN value, 1 for True and 0 for False.
Sample Input 0

int x = 42; // no brackets here
Sample Output 0

1
Sample Input 1

() {} []
Sample Output 1

1"""







def areBracketsProperlyMatched(code_snippet):
    paranthesis = []

    for i in code_snippet:
        if i=="(" or i==")" or i=="[" or i=="]" or i=="{" or i=="}":
            paranthesis.append(i)

    if len(paranthesis)==0:
        return 1

    stak=[]

    for i in paranthesis:
        if i=="(" or i=="[" or i=="{":
            stak.append(i)
        else:
            if len(stak)==0:
                return 0

            element = stak.pop()

            if i == ")" and element != "(":
                return 0
            if i == "]" and element != "[":
                return 0
            if i == "}" and element != "{":
                return 0

    if len(stak)==0:
        return 1
    else:
        return 0

code_snippet = input()

result = areBracketsProperlyMatched(code_snippet)

print(int(result))