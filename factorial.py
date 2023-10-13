n = int(input()) # Give the number

def factorial(n):
    f = 1

    for i in range(1, n+1): # Looping from 1 to desired num
        f*=i # Multiplying num to f 

    return f

print(f'Factorial of {n} is {factorial(n)}.')





