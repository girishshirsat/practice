"""Both players are given the same string, .
Both players have to make substrings using the letters of the string .
Stuart has to make words starting with consonants.
Kevin has to make words starting with vowels.
The game ends when both players have made all possible substrings.

Scoring
A player gets +1 point for each occurrence of the substring in the string .

For Example:
String  = BANANA
Kevin's vowel beginning word = ANA
Here, ANA occurs twice in BANANA. Hence, Kevin will get 2 Points."""



def minion_game(string):
    S = string.upper()
    L = len(S)
    V = ["A", "E", "I", "O", "U"]
    Vov = []
    Cons = []
    CC = 0
    VC = 0

    for i in range(L):
        if S[i] in V:
            for j in range(i+1, L+1):  
                Curr = S[i:j]
                if Curr not in Vov:    
                    Vov.append(Curr)
                    n = S.count(Curr)
                    VC += n
        
        else:
            for j in range(i+1, L+1):  
                Curr = S[i:j]
                if Curr not in Cons:   
                    Cons.append(Curr)
                    n = S.count(Curr)
                    CC += n

    #OR###########################
    # for i in range(L):
    #     if S[i] in VOWELS:
    #         VC += L - i   # All substrings starting at i
    #     else:
    #         CC += L - i 


    if VC > CC:
        print("Kevin", VC)
    elif CC > VC:
        print("Stuart", CC)
    else:
        print("Draw")        

s = input()
minion_game(s)