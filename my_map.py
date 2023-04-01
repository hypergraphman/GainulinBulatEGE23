def my_map(func, iter):
    r = []
    for el in iter:
        r.append(func(el))
    return r


def f(n):
    return n ** 3


a = [1, 2, 5, 10, 7]
r = my_map(f, a)
print(r)
