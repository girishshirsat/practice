"""You are given a string . It consists of alphanumeric characters, spaces and symbols(+,-).
Your task is to find all the substrings of  that contains  or more vowels.
Also, these substrings must lie in between  consonants and should contain vowels only."""

import re

S=input()

pattern = r"(?<=[^aeiouAEIOU\s\d])([aeiouAEIOU]{2,})(?=[^aeiouAEIOU\s\d])"
matches = re.findall(pattern, S)

if matches:
    for match in matches:
        print(match)
else:
    print("-1")