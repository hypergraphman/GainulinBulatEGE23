win = 129


# m = 1 это когда Петя выиграл 1 ходом
# m = 2 это когда Ваня выиграл 1 ходом
# m = 3 это когда Петя выиграл 2 ходом
# m = 4 это когда Ваня выиграл 2 ходом
def f(a, c, m):
    if a >= win:
        return c % 2 == m % 2
    if c == m:
        return False
    moves = [f(a + 1, c + 1, m),
             f(a * 2, c + 1, m)]
    return any(moves) if (c + 1) % 2 == m % 2 else all(moves)


for s in range(1, win):
    for m in range(0, 4 + 1):
        if f(s, 0, m):
            print(s, m)
            break