"Day -1"
# 1. Write a Python program to calculate the area of a rectangle given its length and width
def area_of_rectangle(l, b):
    """l : Lenght b: Width"""
    area = l * b
    return area

# print(area_of_rectangle(12, 6))

# 2.Create a program that takes a user's name and age as input and prints a greeting message.
def greet():
    name = str(input('Please enter your name: '))
    age = int(input("and age: "))

    print(f"Greetings, {name}!!")

    return None

# greet()
    
# 3. Write a program to check if a number is even or odd
def odd_even_checker(num):
    if num % 2 == 0:
        return "Even"
    else:
        return "Odd"
    
# print(odd_even_checker(11))

# 4. Given a list of numbers, find the maximum and minimum values
from typing import List
def min_max_checker(input_list:List[int]):
    if not input_list:
        return "List provided is empty."
    
    max_num = input_list[0]
    min_num = input_list[0]

    for num in input_list:
        if num > max_num:
            max_num = num
        if num < min_num:
            min_num = num
    
    return max_num, min_num

# print(min_max_checker([]))

# 5. Create a Python function to check if a given string is a palindrome
def palindrome_checker(string:str):
    if not string.strip() or not isinstance(string, str):
        return "Please enter a word in a valid format or avoid entering an empty string."
    
    string = ''.join(char.lower() for char in string if char.isalnum())
    # reversed_string = string[::-1]

    reversed_string = ''
    for char in string:
        reversed_string = char + reversed_string

    if string == reversed_string:
        return "String is a palindrome."
    else:
        return "String is not a palindrome."
    
# Function to test palindrome_checker
def test_palindrome_checker():
    assert palindrome_checker("level") == "String is a palindrome."
    assert palindrome_checker("radar") == "String is a palindrome."
    assert palindrome_checker("hello") == "String is not a palindrome."
    assert palindrome_checker("") == "Please enter a word in a valid format or avoid entering an empty string."
    assert palindrome_checker("   ") == "Please enter a word in a valid format or avoid entering an empty string."
    assert palindrome_checker("A man, a plan, a canal, Panama!") == "String is a palindrome."
    assert palindrome_checker("Was it a car or a cat I saw?") == "String is a palindrome."

    print('All test case passed!')

# test_palindrome_checker()

# 6. Calculate the compound interest for a given principal amount, interest rate, and time period
import math
def compund_interest_cal(p:int, r:float, t:int):
    """
    p :principal amount
    r : interest rate(in decimal)
    t : time period (in year)
    """
    rate_in_deciamal = r / 100.0
    ci = p * math.pow(1+ rate_in_deciamal, t)

    return f'Compound Interest: {ci:.2f}'

# print(compund_interest_cal(500, 2.5, 4))


# 7. Write a program that converts a given number of days into years, weeks, and days

def days_to_year_week_day_converter(num_days:int):

    year = num_days // 365
    remaining_days = num_days % 365
    week = remaining_days // 7
    days = remaining_days % 7

    return f'{year} year, {week} week, {days} days'

# print(days_to_year_week_day_converter(732))

# 8.  Given a list of integers, find the sum of all positive numbers

def sum_positive_integer(int_list:List[int]):
    sum_of_integer = 0
    for n in int_list:
        if n > 0:
            sum_of_integer+=n

    return sum_of_integer

# print(sum_positive_integer([-4, 65, 7, 8, 9,-40]))

# 9.  Create a program that takes a sentence as input and counts the number of words in it

def word_counter(sentence:str):
    words = sentence.split()

    word_count = len(words)

    return word_count

print(word_counter('    Spaces before and after    '))
