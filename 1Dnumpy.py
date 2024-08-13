import numpy as np

a = np.array([0, 1, 2, 3, 4])
print(a)

print("a[0]:", a[0])
print("a[1]:", a[1])
print("a[2]:", a[2])
print("a[3]:", a[3])
print("a[4]:", a[4])

print("/////")
print(np.__version__)

print("/////")

# Type: numpy.array
print(type(a))
# Type of data
print(a.dtype)

print("/////")

a[0] = 100
a[4] = 123

print(a)

print("/////")

print(a[1:4])

print("/////")

a[2:4] = 300, 400

print(a)

print("/////")

# We can also define the steps in slicing,
# like this: [start:end:step].

arr = np.array([1, 2, 3, 4, 5, 6, 7])

print(arr[1:5:2])

print("/////")

# If we don't pass start its considered 0

print(arr[:4])

print("/////")

print(a.size)

print("Dimensions: ",a.ndim)

print("Size each dimension: ", a.shape)

print("Average: ", a.mean())

print("Max: ", a.max())

print("Min: ", a.min())

print("/////")

for x in a:
  print(x)