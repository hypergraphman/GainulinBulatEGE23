from functools import lru_cache


@lru_cache(None)
def f(n):
    pass

for i in range(0, 10000):
    f(i)
print(f(10000))