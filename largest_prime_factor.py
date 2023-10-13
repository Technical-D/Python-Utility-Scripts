n = int(input().strip())


largest_factor = 2  # Initialize the largest factor to 2

while largest_factor * largest_factor <= n:
    if n % largest_factor == 0:
        n //= largest_factor
    else:
        largest_factor += 1

print(n)
# The remaining number after the loop is the largest prime factor
# if n > largest_factor:
#     largest_factor = n
# print(n)