for n in range(1, 77):
    s1 = bin(n)[2:]
    s2a = s1 + str(s1.count('1') % 2)
    s2b = s2a + '0'
    if int(s2b, 2) > 77:
        print(n)
        break