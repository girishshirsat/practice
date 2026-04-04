T = int(input())

for i in range(T):
    try:
        A, B = map(int, input().split())  
        print(A // B)

    except ZeroDivisionError:
        print("Error Code: integer division or modulo by zero")

    except ValueError as e:
        print("Error Code:", e)