def alg(n):
    s1 = f'{n:b}'
    s2 = s1 + str(sum(map(int, s1)) % 2)
    s3 = s2 + str(sum(map(int, s2)) % 2)
    r = int(s3, 2)
    return r


print(alg(28))
i = 1
while alg(i) <= 77:
    i += 1
print(i)

for i in range(1, 1000):
    s1 = f'{i:b}'
    s2 = s1 + str(sum(map(int, s1)) % 2)
    s3 = s2 + str(sum(map(int, s2)) % 2)
    r = int(s3, 2)
    if r > 77:
        print(i)
        break
