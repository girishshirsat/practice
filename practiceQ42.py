"""You are given the shape of the array in the form of space-separated integers, each integer representing the size of different dimensions, your task is to print an array of the given shape and integer type using the tools numpy.zeros and numpy.ones."""


import numpy



A,B,C=list(map(int,input().split()))

for i in range(C):
    print(numpy.zeros((A,B), dtype = int))
    print()
    
for i in range(C):
    print(numpy.ones((A,B), dtype = int))    
    print()

# import numpy as np


# shape = tuple(map(int, input().split()))


# zeros_array = np.zeros(shape, dtype=int)
# ones_array = np.ones(shape, dtype=int)


# print(zeros_array)
# print(ones_array)