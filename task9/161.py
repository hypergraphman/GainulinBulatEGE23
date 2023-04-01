lines = open('9-161.txt').readlines()
data = []
for line in lines:
    data.append(list(map(int, line.split())))
print(data)