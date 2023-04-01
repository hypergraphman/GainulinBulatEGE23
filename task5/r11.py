def alg(n):
    s1 = f'{n:b}'
    r = int(s1[1:], 2)
    return n - r


print(alg(11))

m = set()
for i in range(500, 5000 + 1):
    m.add(alg(i))
print(m)