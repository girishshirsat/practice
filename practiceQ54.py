"""There is a collection of input strings and a collection of query strings. For each query string, determine how many times it occurs in the list of input strings. Return an array of the results."""
def matchingStrings(stringList, queries):
    L1=stringList
    L2=queries
    count=[]
   
    for j in L2:
        if j in L1:
            C=L1.count(j)
            count.append(C)
        else:
            count.append(0)

    return count



fptr = open(os.environ['OUTPUT_PATH'], 'w')

stringList_count = int(input().strip())

stringList = []

for _ in range(stringList_count):
    stringList_item = input()
    stringList.append(stringList_item)

queries_count = int(input().strip())

queries = []

for _ in range(queries_count):
    queries_item = input()
    queries.append(queries_item)

res = matchingStrings(stringList, queries)

fptr.write('\n'.join(map(str, res)))
fptr.write('\n')

fptr.close()
