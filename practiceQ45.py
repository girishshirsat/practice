"""Given a string s, return the longest palindromic substring in s.
Example 1:

Input: s = "babad"
Output: "bab"
Explanation: "aba" is also a valid answer."""

s="aacabdkacaa"
def longestPalindrome(s: str) -> str:
        l = []
    
        def check_pal(s):
            for i in range(len(s)):        
                for j in range((i+1), len(s)):
                    if s[i] == s[j]:
                        temp_l = s[i:j+1]
                        if temp_l == temp_l[::-1]:
                            l.append(temp_l)

        if s == s[::-1]:
            return s
        elif s != s[::-1]:
            check_pal(s)

        if not l:
            return s[0]
    
    
        l.sort(key=len, reverse=True)
     
    
        st = str(max(l, key=len))
        return st

print(longestPalindrome(s))