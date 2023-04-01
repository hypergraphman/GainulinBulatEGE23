with open('17-1.txt') as f:
    a = [int(x) for x in f.readlines()]
r = [1]
cur_len = 1
for i in range(0, len(a) - 1):
    if a[i] > a[i + 1]:
        cur_len += 1
        if cur_len > r[0]:
            r = [cur_len]
        elif cur_len == r[0]:
            r.append(cur_len)
    else:
        cur_len = 1
print(r[0], len(r))
