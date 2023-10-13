import math

def encryption(s):
    l = math.sqrt(len(s))
    r = round(l)
    c = math.ceil(l)
    s = list(s)
    res = []
    if r * c < l:
        r+=1
    for i in range(r):

        for j in range(c):
            a = s.pop()
            res.append(a)
        
    print(res)

a = "haveaniceday"
encryption(a)