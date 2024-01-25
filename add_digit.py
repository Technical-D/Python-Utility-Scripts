# The code calculates the digital root of a number by iteratively summing its digits until the result is a single-digit number.
num = int(input('Enter Number of your choice: '))

sum = 0

while num > 0:
    sum += num % 10
    num //= 10

    if num == 0 and sum > 9:
        num = sum 
        sum = 0
    

print(sum)
    