s = open('24.txt').read().strip()
cur_len = 1
max_len = 1
i_max_len = 0
for i in range(1, len(s)):
    if s[i - 1] != s[i]:
        cur_len += 1
        if cur_len > max_len:
            max_len = cur_len
            i_max_len = i
    else:
        cur_len = 1
print(s[i_max_len - max_len + 1: i_max_len + 1], max_len)