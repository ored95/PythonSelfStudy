i = 2
while (i < 100):
    j = 2
    while (j <= (i/j)):
        if not(i % j): break
        j += 1

    if (j > (i/j)): print(i, "is a prime")
    i += 1

print('Good bye!')
