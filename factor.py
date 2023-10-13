def factor(n):
    factor =[]

    divisor = 2 # Starting with 2 

    while divisor <= n:
        if n % divisor == 0: # checking if num is divisible by divisor 
            factor.append(divisor)
            n /= divisor # If divisible divide the num by divisor
        else:
            divisor+=1 # If not than increased the divisior by 1 
    
    return factor # Return the factor in the form of list

num = int(input()) # Give the number 

print(f'Factors of {num} is {factor(num)}.')