print('x y z w')
for x in 0, 1:
    for y in 0, 1:
        for z in 0, 1:
            for w in 0, 1:
                f = (not x) and y or z and (not y) or (not z) and w
                if not f:
                    print(x, y, z, w)