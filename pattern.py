# Pyramid Pattern without space
n = int(input())

for i in range(n):

    for j in range(i+1):
        print("*", end="")
    print()

# Pyramid Pattern with space

n = int(input())

for i in range(n):

    for j in range(n - i - 1):
        print(" ", end="")

    for k in range(2 *i+1):
        print("*", end="")

    print()

# Pyramid Pattern without space descending
n = int(input())

for i in range(n):

    for j in range(n - i):
        print("*", end="")

    print()

# Pyramid Pattern with space descending
n = int(input())

for i in range(n, 0, -1):

    for j in range(n -i ):
        print(" ", end="")
    
    for k in range(2 * i - 1):
        print("*", end="")

    print()

# Asc + Desc pyramid without space

n= int(input())

for i in range(n):

    for j in range(i + 1):
        print("*", end="")

    print()
for i in range(n):

    for k in range(n - i - 1):
        print("*", end="")
    print()


# Asc + desc pyramid with space
n = int(input())

for i in range(n):

    for j in range(n - i):
        print(" ", end="")
    for k in range(2 * i + 1):
        print("*", end="")
    print()

for l in range(n-1, 0 , -1):

    for m in range(n - l + 1):
        print(" ", end="")

    for p in range(2 * l -1):
        print("*", end="")
    print()
