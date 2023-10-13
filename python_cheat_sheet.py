# Python Cheat Sheet

# Comments
# This is a single-line comment

"""
This is a
multi-line comment
"""

# Variables and Data Types
# Integer
age = 25
# Float
salary = 2500.50
# String
name = "John Doe"
# Boolean
is_student = True

# Basic Operations
x = 10
y = 5
addition = x + y
subtraction = x - y
multiplication = x * y
division = x / y
modulus = x % y
power = x ** y

# Conditional Statements
if condition:
    # code to execute if the condition is true
elif condition:
    # code to execute if the previous condition is false and this condition is true
else:
    # code to execute if all conditions are false

# Loops
# For loop
for item in iterable:
    # code to execute for each item

# While loop
while condition:
    # code to execute while the condition is true
    # don't forget to update the condition to avoid an infinite loop

# Functions
def function_name(parameters):
    # code to execute
    return value

result = function_name(arguments)

# Lists
my_list = [item1, item2, item3]
list_length = len(my_list)
first_item = my_list[0]
sliced_list = my_list[1:3]
my_list.append(new_item)
my_list.insert(index, item)
my_list.remove(item)
my_list.pop(index)
my_list.sort()
my_list.reverse()

# List Comprehension
squared_numbers = [num ** 2 for num in my_list if num % 2 == 0]

# Lambda Functions
multiply = lambda x, y: x * y
result = multiply(5, 3)

# Tuples
my_tuple = (item1, item2, item3)
tuple_length = len(my_tuple)
first_item = my_tuple[0]

# Dictionaries
my_dict = {"key1": value1, "key2": value2}
value = my_dict["key"]
my_dict["new_key"] = new_value
del my_dict["key"]

# Sets
my_set = {item1, item2, item3}
set_length = len(my_set)
my_set.add(new_item)
my_set.remove(item)
my_set.discard(item)
my_set.clear()

# String Manipulation
my_string = "Hello, World!"
string_length = len(my_string)
substring = my_string[7:12]
concatenation = "Hello" + ", " + "World!"
uppercase = my_string.upper()
lowercase = my_string.lower()
split_string = my_string.split(",")
replaced_string = my_string.replace("Hello", "Hi")
stripped_string = my_string.strip()

# File I/O
# Reading a file
file = open("filename.txt", "r")
content = file.read()
file.close()

# Writing to a file
file = open("filename.txt", "w")
file.write("Hello, World!")
file.close()

# Exception Handling
try:
    # code that may raise an exception
except ExceptionType:
    # code to handle the exception
finally:
    # code that will be executed regardless of whether an exception occurred or not

# Modules and Packages
import module_name
from module_name import function_name

# Classes and Objects
class MyClass:
    def __init__(self, parameter):
        self.property = parameter
    
    def method(self):
        # code to execute

my_object = MyClass(argument)
my_object.method()

# Importing Libraries
import library_name
from library_name import function_name
