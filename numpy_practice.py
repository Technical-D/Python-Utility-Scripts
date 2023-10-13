import numpy as np 

a = np.array([1, 2, 4, 5, 6])
b = np.array([2, 4, 6, 6, 7])
print(type(a))
print(a.dtype)
print(a.size)
print(a.ndim)
print(a, b)
# We can do addition of list usinf simple line using numpy
c = a + b # This is way faster than below code
print(c)
# To do it in basic we can use zip function
z = []
for n, m in zip(a, b):
    z.append(n + m)
print(z)
# Substracting array 
d = a - b
print(d)
# Multiplying array with scalar value
e = 2*a
print(e)
# In normal way
p = []
for i in a:
    p.append(2 * i)
print(p)
# Product of nupy array's
w = a * b
print(w)
# Using normal way
v = []
for n, m in zip(a, b):
    v.append(n * m)
print(v)
# Dor product
f = np.dot(a, b)
print(f)
# Using normat way
q = 0
for n, m in zip(a, b):
    q+=n*m
print(q)
# Adding constant value to numpy array
g = a + 3
print(g)
# Calculating mean
h = a.mean()
print(h)
# Max value
i = a.max()
print(i)
# Accessing pi value
pi = np.pi
j = np.array([1, pi/2, pi/6])
k = np.sin(j)
print(j,k)
# Linespace
l = np.linspace(-2, 2, num=9)
print(l)

m = np.linspace(0, 2*pi, 100)
n = np.sin(m)
# Plotting sin graph
# import matplotlib.pyplot as plt
# plt.plot(m,n)

# Two dimensional array
a1 = np.array([[1, 2, 3], [4, 5, 6], [7, 8,9]])
b1 = np.array([[5, 4, 3], [4, 1, 0], [2, 4,6]])

print(a1.ndim)
print(a1.size)
print(a1.shape)

# Adding two dimensional array
print(a1 + b1)

# Multiply my scalar
print(2 * a1)

# Product of array
print(a1 * b1)

# Matrix multiplication
# To perform matrix multiplication row of first array must be same as column of second array
a2  = np.array([[1, 2, 3], [4, 5,6]])
b2 = np.array([[1, 2], [1, 0], [0, 1]])

c2 = np.dot(a2, b2) 
print(c2)
