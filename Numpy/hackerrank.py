# Enter your code here. Read input from STDIN. Print output to STDOUT
import numpy as np
the_input = input().split()
n = int(the_input[0])
m = int(the_input[1])
p = int(the_input[2])
a1 = np.zeros((n, p))
a2 = np.zeros((m, p))
for i in range(n):
    a1[i] = np.array(input().split())
for i in range(m):
    a2[i] = np.array(input().split())

print(np.array(np.concatenate((a1, a2)), dtype=np.int32))