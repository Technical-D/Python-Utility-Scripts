n = int(input())
s1 = 0
s2 = 0
for i in range(n+1):
    s1+=i**2

for i in range(n +1):
    s2+=i

diff = abs(s1 - s2 * s2)
print(diff)