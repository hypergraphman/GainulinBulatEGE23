def n_to_p(n, p):
    r = ''
    while n > 0:
        d = '0123456789ABCDEF'[n % p]
        r = d + r
        n //= p
    return r


print(n_to_p(255, 16), hex(255))  # FF
print(n_to_p(194, 5))  # 1234
print(n_to_p(100, 2), bin(100))  # 1100100

print(n_to_p(36**10 + 6**25 - 15, 6).count('0'))