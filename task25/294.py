from fnmatch import fnmatch


def sum_digit(n):
    s = 0
    while n > 0:
        s += n % 10
        n //= 10
    # for c in str(n):
    #     s += int(c)
    return s


for i in range(2023, 10**10, 2023):
    if fnmatch(str(i), '1?1?1?1*1') and sum(map(int, str(i))) == 22:
        print(i, i // 2023)