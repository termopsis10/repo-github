from itertools import cycle, count

n = 240
num_list = [el for el in range(10)]
counter = count()
cycler = cycle(num_list)
print([next(counter) for el in range(n)])
print([next(counter) for el in range(n)])
