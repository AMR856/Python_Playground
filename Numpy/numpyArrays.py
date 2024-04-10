#!/usr/bin/python3
import numpy as np

"""
my_array = np.array([1, 2, 3, 4, 5])
print(my_array)
print(my_array[1])
print(my_array[1:4])
"""

multi_array = np.array([[1, 2, 3],
                        [4, 5, 6],
                        [7, 8, 9]
                        ])

multi_array_1 = np.array(
    [
        [
            [1, 2, 3],
            [4, 5, 6],
            [7, 8, 9]
        ]
        ,
        [
            [1, 1, 1],
            [1, 1, 1],
            [1, 1, 1]
        ]
    ])

"""

print(multi_array_1.shape)
print(multi_array_1.ndim)
print(multi_array_1.size)
print(multi_array_1.dtype)

"""

multi_array_2 = np.array(
    [
        [1, 2, 3],
        [4, 5, 6],
        [7, "8", 9]
    ],
    dtype=np.int32
)

# We can't put the type at the end of the array when mixed

# less efficient when mixing data types like python objects

"""

print(multi_array_2.dtype)
print(multi_array_2[2][1].dtype)
print(type(multi_array_2[2][2]))

"""

array_full = np.full((2, 3, 4), 9)
print(array_full)

my_zeros = np.zeros((2, 3, 4))
my_ones = np.ones((2, 3, 4))
my_empty = np.empty((2, 3, 4))  # default values are there, only allocating
my_range = np.arange(1, 500, 2)
my_space = np.linspace(1, 1000, 500)
print(my_zeros)
print(my_ones)
print(my_empty)
print(my_range)
print(len(my_space))  # 500
