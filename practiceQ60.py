"""Max Unique Substring Length in a Session
Given a string of lowercase letters with sessions separated by '' characters, find the maximum length of a substring with all distinct letters within any single session.

Example

Input

sessionString = abcabcbb
Output

3"""
def maxDistinctSubstringLengthInSessions(sessionString):

    s=sessionString.lower()
    L=""
    M=0
    for i in range(len(s)):
        for j in range(i,len(s)):
            if s[j] not in L and s[j].isalpha():
                L+=s[j]
                A=len(L)
                if A>M:
                    M=A 
            else:   
                break
        print(L)
        L="" 

    return M


sessionString = input()

result = maxDistinctSubstringLengthInSessions(sessionString)

print(result)

