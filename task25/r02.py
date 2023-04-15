def divs(n):
    res = {1, n}
    for d in range(2, int(n**0.5) + 1):
        if n % d == 0:
            res.add(d)
            res.add(n // d)
    return sorted(res)


for i in range(174457, 174505 + 1):
    t = divs(i)
    if len(t) == 4:
        print(t[1], t[2])