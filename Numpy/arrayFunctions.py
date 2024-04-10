import numpy as np

"""
my_array = np.array([1, 2, 3])
print(np.append(my_array, [4, 5, 6]))
print(my_array)
new_array = np.append(my_array, [4, 5, 6])
print(new_array)
new_array_2 = np.insert(new_array, 6, [8, 9, 10])
print(new_array_2.dtype)
"""

my_array_1 = np.array([[1, 2, 3],
                      [4, 5, 6]])

"""
    The third parameter is the axis 
    0 -> row
    1 -> column
"""
print(np.delete(my_array_1, 0, 1))