def true_false(t):
    return all(t)

t1 = (True, True, True)
t2 = (True, False, True)
t3 = (1, 2, 3)
print(true_false(t1))
print(true_false(t2))
print(true_false(t3))