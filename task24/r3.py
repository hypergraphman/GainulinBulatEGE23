s = open('24.txt').read().strip()

temp = 'EAB'
cur_len = 0
max_len = 0
for char in s:
    if char == temp[cur_len % len(temp)]:
        cur_len += 1
        if cur_len > max_len:
            max_len = cur_len
    elif char == temp[0]:
        cur_len = 1
    else:
        cur_len = 0
print(max_len)