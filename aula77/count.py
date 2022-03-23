from itertools import count

contador = count(start=5, step=2)
print(contador)
for c in contador:
    print(c)
    if c > 30:
        break
