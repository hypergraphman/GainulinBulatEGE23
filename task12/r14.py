a = []
for x in range(0, 100):
    for y in range(0, 100):
        for z in range(0, 100):
            if (2 * x + 3 * y + 6 * z == 186 and
               y + z == 26):
                a.append(x + y + z + 2)
print(min(a))
print(a)