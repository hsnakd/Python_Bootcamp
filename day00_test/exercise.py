import numpy as np
P = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])
print(P[0, 1:3], P[0:2, 3])



x = [14, 15, 30][-1]
y = round(14.9, -1)
z = x/y

print(x)
print(y)
print(z)

numbers = (4, 7, 19, 2, 89, 45, 72, 22)
sorted_num = sorted(numbers)
print(type(sorted_num))