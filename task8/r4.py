from itertools import product

alf = 'егэ'
k = 0
for letters in product(alf, repeat=5):
    word = ''.join(letters)
    if word[0] != 'г':
        print(word)
        k += 1
print(k)