''''Problem Statement
The royal family exchanges gifts at Christmas, where the youngest member receives gifts from everyone but doesn't give any gifts. Given the data for all the exchanged gifts among the family members, you need to identify the youngest member, who is the one receiving gifts from everyone but not giving any.

Note: A family member does not give more than one gift to the same member.

Input Format
The first line of the input contains two integers n and m denoting the number of family members and the number of gifts that were exchanged.

The next m lines contain two integers each. In the ith line, two integers ai, bi represent that a gift was given by ai to bi.

Output Format
Print a single integer, the number that represents the youngest member of the family.

If no such member is found, print “-1” instead.

Constraints
1 <= n <= 104

0 <= m <= 105

1 <= ai, bi, <= n

Sample Testcase 0
Testcase Input
2 1
1 2
Testcase Output
2
Explanation
Family member 1 gave a gift to family member 2. Now, we can see that 2 did not give any gift to anyone but received a gift from all other members (member 1). Hence, 2 is the youngest member.
 
 
'''


def find_youngest_member(n, m, gifts):
    """
    Write your logic here.
    Parameters:
        n (int): Number of family members
        m (int): Number of gifts exchanged
        gifts (list of tuples): List of tuples where each tuple contains two integers (a_i, b_i)
    Returns:
        int: The number that represents the youngest member of the family or -1 if no such member is found
    """
    givers=[]
    recievers=[]
    i=0
    for i in gifts:
        T=list(i)
        for e in range(len(T)):
            if e%2==0:
                givers.append(T[e])
            else:
                recievers.append(T[e])




    unique_recievers=set(recievers)
    unique_recievers1=[]
    for i in list(unique_recievers):
        if i not in givers:
            unique_recievers1.append(i)
        
   

    
    if len(unique_recievers1)==0:
        return(-1)
    else:
        return(unique_recievers1[i])


    


def main():
    import sys
    input = sys.stdin.read
    data = input().strip().split()
    
    n = int(data[0])  # Number of family members
    m = int(data[1])  # Number of gifts exchanged
    
    gifts = []
    index = 2
    for _ in range(m):
        a_i = int(data[index])
        b_i = int(data[index + 1])
        gifts.append((a_i, b_i))
        index += 2
    
    # Call user logic function and print the output
    result = find_youngest_member(n, m, gifts)
    print(result)

if __name__ == "__main__":
    main()


"""
def find_youngest_member(n, m, gifts):

    
    indegree = [0] * (n + 1)
    outdegree = [0] * (n + 1)

    for a, b in gifts:
        outdegree[a] += 1
        indegree[b] += 1

    for i in range(1, n + 1):
        if indegree[i] == n - 1 and outdegree[i] == 0:
            return i

    return -1
"""

