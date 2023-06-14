def f(n):
    s1 = f'{n:b}'
    if n % 3 == 0:
        s2 = s1 + s1[-3:]
    else:
        s2 = s1 + f'{n%3*3:b}'
    return int(s2, 2)


for i in range(1, 100):
    if f(i) >= 76:
        print(i)