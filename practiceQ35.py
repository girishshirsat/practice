"""You have to generate a list of the first  fibonacci numbers,  being the first number. Then, apply the map function and a lambda expression to cube each fibonacci number and print the list."""
cube = lambda x:x**3

def fibonacci(n):
    L=[0,1]
    if n<len(L):
        return L[:n]
    else:
        for i in range(2,n):
            j=i-1
            A=L[j-1]+L[i-1]
            L.append(A)
        return L

if __name__ == '__main__':
    n = int(input())
    print(list(map(cube, fibonacci(n))))