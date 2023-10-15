from itertools import permutations
def permut(w):
    p = permutations(w)
    for i in p:
        print(''.join(i))
w = input()
permut(w)