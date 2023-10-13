for i in range(2,41):
    n = i
    f = []
    fac = []
    l = []
    res = 1

    for i in range(2,n+1):
        divisor = 2
        f1 = []
        while divisor <= i:
            if i % divisor == 0:
                f1.append(divisor)
                i //= divisor
            else:
                divisor+=1
        f.append(f1)

    def is_prime(n):
        if n <= 1:
            return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True

    for i in range(2, max(f)[0] + 1):
        if is_prime(i):
            fac.append(i)

    for j in fac:
        a1 = []
        for i in f:
            a = i.count(j)
            a1.append(a)
        l.append(max(a1))


    for i in range(len(fac)):
            b = fac[i]**l[i]
            res *= b

    print(res)