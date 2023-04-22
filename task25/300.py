from fnmatch import fnmatch

k = 1
for i in range(4546, 10**10, 4546):
    if fnmatch(str(i), '8*80*06'):
        if k % 60 == 1:
            print(k, i, i // 4546)
        k += 1