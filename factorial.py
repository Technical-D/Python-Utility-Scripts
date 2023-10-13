n = int(input())
f = 1

for i in range(1, n+1):
    f*=i

f = str(f)
res = 0
for i in range(len(f)):
    res+=int(f[i])

print(res)

