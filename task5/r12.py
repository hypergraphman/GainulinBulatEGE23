from itertools import permutations


def alg(n):
    b = []
    for e1, e2 in permutations(map(int, str(n)), r=2):
        t = e1 * 10 + e2
        if 10 <= t <= 99:
            b.append(t)
    return max(b) - min(b)


# print(alg(351))

# for i in range(100, 1000):
#     if alg(i) == 40:
#         print(i)

i = 100
while alg(i) != 40:
    i += 1
print(i)

i = 999
while alg(i) != 40:
    i -= 1
print(i)