from itertools import product

alf = 'acgt'
k = 0
for letters in product(alf, repeat=5):
    if letters.count('a') == 2:
        print(letters)
        k += 1
print(k)
