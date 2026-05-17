def isAlphabeticPalindrome(code):
    s1="".join(c for c in code if c.isalpha())

    if s1==s1[::-1]:
        return 1
    else: 
        return 0




code = input()
result = isAlphabeticPalindrome(code)
print(int(result))

