# ZIP function
name = ['Dheeraj', 'Jayhind', 'Shubham', 'Anjali']
age = [20, 21, 20, 20]
gender = ['Male', 'Male', 'Male', 'Female']

all_details = list(zip(name, age, gender))
print(all_details)
print(type(all_details))

for n, a, g in all_details:
    print(n)
    print(a)
    print(g)

# Decorators in python
def decorator(func):
    def wrapper():
        print(f"Executing {func.__name__}")
        func()
    return wrapper

@decorator
def do_this():
    print('do_this')

@decorator
def do_that():
    print('do_that')

do_this()
do_that()

# How to iterate 3 or more iterable
"""
It can be done using zip function like shown below.
Note: It can also be done using range function but in the case of mismatcing list len it will give error.
"""
l1 = [1, 3, 5, 7, 8]
l2 = [5, 8, 0, 3, 5, 3, 5]
l3 = [5, 6, 7]

for i, j, k in zip(l1, l2, l3):
    print(i)
    print(j)
    print(k)
    #  it will print numbers till lowest len of list

# Some random question
letter = ""

while(len(letter) != 2):
    letter += 'a'
    print(letter)

# Adding sum of natural number using recursion
"""
5 = 5 + 4 + 3 + 2 + 1 = 15 example
"""
def adding_num(n):
    if n == 1:
        return 1
    else:
        return n + adding_num(n - 1)
s = adding_num(5)
print(s)