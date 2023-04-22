from fnmatch import fnmatch


def count_zero(n):
    k = 0
    while n > 0:
        if n % 10 == 0:
            k += 1
        n //= 10
    return k


for i in range(50068, 10**10, 50068):
    if fnmatch(str(i), '9?979*8') and count_zero(i) > 0:
        print(i, i // 50068)