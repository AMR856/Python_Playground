import numpy as np

# print(np.inf)
# print(np.nan)

l1 = [1, 2, 3, 4, 5]
l2 = [6, 7, 8, 9, 10]

a1 = np.array(l1)
a2 = np.array(l2)

"""
print(l1 * 5)
print(a1 * 5)
# print(l1 + 5)
print(a1 + 5)
print(a1 * a2)
print(a1 / a2)
"""

a3 = np.array([[1, 2, 3],
               [4, 5, 6]])
a4 = np.array([[1], [2]])

"""
print(a3 + a4)
print(a3.ndim)
print(a3.shape)
print(a4.ndim)
print(a4.shape)
"""

a5 = np.array([1, 2, 3, 4])
print(np.sqrt(a5))
print(np.sin(a5))
print(np.cos(a5))
print(np.tan(a5))
print(np.exp(a5))
print(np.log2(a5))
print(np.log10(a5))
# arcsin, arccos and others exp, log