*a, = map(int, open('17.txt'))
mx = 0
for el in a:
    if 10 <= el < 100 and el > mx:
        mx = el
r = []
for x1, x2 in zip(a, a[1:]):
    if (10 <= x1 < 100) != (10 <= x2 < 100) and (x1 + x2) % mx == 0:
        r.append(x1 + x2)
print(len(r), max(r))