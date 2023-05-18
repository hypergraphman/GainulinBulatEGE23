a = []
for n in range(20):
    s1 = bin(n)[2:]
    if n % 2 == 0:
        s2 = '11' + s1[:-2] + '10'
    else:
        s2 = s1 + '01'
    a.append(int(s2, 2))
print(max(a))