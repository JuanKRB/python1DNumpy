import numpy as np

u = np.array([1, 0])
v = np.array([0, 1])

print(np.add(u, v))
print(np.subtract(u, v))
print(np.multiply(u, v))
# print(np.divide(u, v))

# it shows the similarity between 'em
print(np.dot(u, v))

print("////")

# it adds 1 all of 'em
u = u + 1
print(u)