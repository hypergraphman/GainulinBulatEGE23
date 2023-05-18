a = set()
for n in range(500, 5001):
    s1 = bin(n)[2:]
    s2 = s1[1:]
    s3 = int(s2, 2)
    s4 = n - s3
    print(s4)
    a.add(s4)
print(len(a))