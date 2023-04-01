with open('17-1.txt') as f:
    a = [int(x) for x in f.readlines()]
r = []
mn = len(a)
for i in range(1, len(a) - 1):
    if a[i - 1] < a[i] > a[i + 1]:
        if r:
            mn = min(i - r[-1], mn)
        r.append(i)
print(len(r), mn)
