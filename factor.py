def factor(n):
    factor =[]

    divisor = 2

    while divisor <= n:
        if n % divisor == 0:
            factor.append(divisor)
            n /= divisor
        else:
            divisor+=1
    
    return factor

print(factor(13195))

print(max(factor(13195)))

        